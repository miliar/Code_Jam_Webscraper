#include<stdio.h>
int tcn,tc;
char ans[15][3][20000];
int ansd[15][3];
int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int i,j,k;
	ans[0][0][0]='P';
	ans[0][1][0]='R';
	ans[0][2][0]='S';
	ansd[0][0]=1;
	for(i=0;i<13;i++){
		for(j=0;j<3;j++){
			ansd[i+1][j]=ansd[i][j]+ansd[i][(j+2)%3];
			for(k=0;;k++){
				if(ans[i][j][k]!=ans[i][(j+1)%3][k])break;
			}
			if(ans[i][j][k]<ans[i][(j+1)%3][k]){
				for(k=0;k<(1<<i);k++){
					ans[i+1][j][k]=ans[i][j][k];
				}
				for(k=0;k<(1<<i);k++){
					ans[i+1][j][k+(1<<i)]=ans[i][(j+1)%3][k];
				}
			}
			else{
				for(k=0;k<(1<<i);k++){
					ans[i+1][j][k]=ans[i][(j+1)%3][k];
				}
				for(k=0;k<(1<<i);k++){
					ans[i+1][j][k+(1<<i)]=ans[i][j][k];
				}
			}
		}
	}
	scanf("%d",&tcn);
	for(tc=1;tc<=tcn;tc++){
		int n,a,b,c;
		scanf("%d%d%d%d",&n,&b,&a,&c);
		printf("Case #%d: ",tc);
		for(i=0;i<3;i++){
			if(a==ansd[n][i]&&b==ansd[n][(i+1)%3]&&c==ansd[n][(i+2)%3]){
				puts(ans[n][(3-i)%3]);
				break;
			}
		}
		if(i==3)puts("IMPOSSIBLE");
	}
	return 0;
}