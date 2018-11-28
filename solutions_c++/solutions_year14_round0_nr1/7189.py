#include <stdio.h>

int main(){
	FILE *in=fopen("A-small-attempt4.in","r");
	FILE *out=fopen("A-small-attempt4.out","w");
	int t, tt;
	fscanf(in,"%d",&t);
	tt=t;
	while(t--){
		int line;
		int card[4][4];
		fscanf(in,"%d",&line);
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++)
				fscanf(in,"%d",&card[i][j]);
		}
		int line2;
		int card2[4][4];
		fscanf(in,"%d",&line2);
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++)
				fscanf(in,"%d",&card2[i][j]);
		}
		int cnt=0;
		int ans;
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				if(card[line-1][i]==card2[line2-1][j]){
					cnt++;
					ans=card[line-1][i];
				}
			}
		}
		if(cnt>1)
			fprintf(out,"Case #%d: Bad magician!\n",tt-t);
		else if(cnt==1)
			fprintf(out,"Case #%d: %d\n",tt-t,ans);
		else
			fprintf(out,"Case #%d: Volunteer cheated!\n",tt-t);
	}
	fclose(in);
	fclose(out);

	return 0;
}