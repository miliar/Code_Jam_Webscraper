#include <cstdio>
#include <cstring>
char ans[3][15][4100];
int cnt[3][15][3];
int T;
int main(){
	scanf("%d",&T);
	for (int i=0;i<3;i++){
		for (int j=0;j<=12;j++){
			for (int k=0;k<3;k++){
				cnt[i][j][k]=0;
			}
		}
	}
	ans[0][0][0] = 'R';
	ans[1][0][0] = 'P';
	ans[2][0][0] = 'S';
	cnt[0][0][0]++;
	cnt[1][0][1]++;
	cnt[2][0][2]++;
	for (int j=1;j<=12;j++){
		for (int i=0;i<3;i++){
			if (i==0){
				char * t1 = ans[0][j-1];
				char * t2 = ans[2][j-1];
				if (strcmp(t1, t2)<0){
					strcpy(ans[i][j], t1);
					strcat(ans[i][j], t2);
					//ans[i][j] = ans[0][j-1]+ans[2][j-1];
				}
				else {
					//ans[i][j] = ans[2][j-1]+ans[0][j-1];
					strcpy(ans[i][j], t2);
					strcat(ans[i][j], t1);
				}
			}
			if (i==1){
				char * t1 = ans[1][j-1];
				char * t2 = ans[0][j-1];
				if (strcmp(t1, t2)<0){
					strcpy(ans[i][j], t1);
					strcat(ans[i][j], t2);
					//ans[i][j] = ans[0][j-1]+ans[2][j-1];
				}
				else {
					//ans[i][j] = ans[2][j-1]+ans[0][j-1];
					strcpy(ans[i][j], t2);
					strcat(ans[i][j], t1);
				}
			}
			if (i==2){
				char * t1 = ans[1][j-1];
				char * t2 = ans[2][j-1];
				if (strcmp(t1, t2)<0){
					strcpy(ans[i][j], t1);
					strcat(ans[i][j], t2);
					//ans[i][j] = ans[0][j-1]+ans[2][j-1];
				}
				else {
					//ans[i][j] = ans[2][j-1]+ans[0][j-1];
					strcpy(ans[i][j], t2);
					strcat(ans[i][j], t1);
				}
			}
			int slen = strlen(ans[i][j]);
			for (int x=0;x<slen;x++){
				if (ans[i][j][x]=='R')cnt[i][j][0]++;
				if (ans[i][j][x]=='P')cnt[i][j][1]++;
				if (ans[i][j][x]=='S')cnt[i][j][2]++;
			}
		}
	}
	for (int Case=1;Case<=T;Case++){
		int n,P,R,S;
		scanf("%d%d%d%d",&n,&R,&P,&S);
		bool check=false;
		for (int i=0;i<3;i++){
			if (cnt[i][n][0]==R && cnt[i][n][1] == P && cnt[i][n][2]==S){
				printf("Case #%d: %s\n",Case, ans[i][n]);
				check=true;
				break;
			}
		}
		if (!check)printf("Case #%d: IMPOSSIBLE\n",Case);
	}
	return 0;
}
