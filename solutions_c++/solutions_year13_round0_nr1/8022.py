#include <stdio.h>
FILE *in = fopen("input.txt","r");
int solve(){
	int i,j;
	bool flag=false;
	char map[6][6];
	int row[5],col[5];
	for(i=1;i<=4;i++) col[i]=row[i]=0;
	for(i=1;i<=4;i++) {
		fscanf(in,"%s",&map[i][1]);
		for(j=1;j<=4;j++) {
			if(map[i][j]=='O'){
				col[j]+=1<<(i-1);
				row[i]+=1<<(j-1);
			}
			else if(map[i][j]=='X'){
				col[j]-=1<<(i-1);
				row[i]-=1<<(j-1);
			}
			else if(map[i][j]=='.') flag= true;
			else {
				if(col[j]>0) col[j]+=1<<(i-1);
				else col[j]-=1<<(i-1);
				if(row[i]>0) row[i]+=1<<(j-1);
				else row[i]-=1<<(j-1);
			}
		}
	}
	int cros1=0,cros2=0;
	for(i=1;i<=4;i++) {
		if(map[i][i]=='O') cros1+=1<<(i-1);
		else if(map[i][i]=='X') cros1-=1<<(i-1);
		else if(map[i][i]=='T') {
			if(cros1>0) cros1+=1<<(i-1);
			else cros1-=1<<(i-1);
		}
		if(map[i][5-i]=='O') cros2+=1<<(i-1);
		else if(map[i][5-i]=='X') cros2-=1<<(i-1);
		else if(map[i][5-i]=='T') {
			if(cros2>0) cros2+=1<<(i-1);
			else cros2-=1<<(i-1);
		}
	}
	for(i=1;i<=4;i++) {
		if(row[i]==15 || col[i]==15 || cros1==15 || cros2==15) return 1;
		else if(row[i]==-15 || col[i]==-15 || cros1==-15 || cros2==-15) return 0;
	}

	if(!flag) return 2;
	return 3;
}
int main(){
	int t;
	char st[5][30]={"X won","O won","Draw","Game has not completed"};
	fscanf(in,"%d",&t);
	
	FILE *out = fopen("output.txt","w");
	for(int i=1;i<=t;i++) {
		fprintf(out,"Case #%d: %s\n",i,st[solve()]);
	}
	fclose(out);
	return 0;
}