#include <cstdio>
#include <algorithm>
using namespace std;

int T;
int main(){
	scanf("%d",&T);
	for(int t=1;t<=T;t++){
		printf("Case #%d: ",t);
		int r1,r2;
		int c1[4][4],c2[4][4];
		scanf("%d",&r1);
		for(int i=0;i<4;i++) for(int j=0;j<4;j++)
			scanf("%d",&c1[i][j]);
		scanf("%d",&r2);
		for(int i=0;i<4;i++) for(int j=0;j<4;j++)
			scanf("%d",&c2[i][j]);
		int n=0, ans=-1;
		for(int k=0;k<4;k++) for(int l=0;l<4;l++)
			if(c1[r1-1][k] == c2[r2-1][l]){
				n++; ans=c1[r1-1][k];
			}
		if(n==0)
			puts("Volunteer cheated!");
		else if(n>1)
			puts("Bad magician!");
		else
			printf("%d\n", ans);
	}
	return 0;
}

