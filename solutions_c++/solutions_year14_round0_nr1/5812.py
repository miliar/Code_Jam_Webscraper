#include <stdio.h>


int main()
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("output.txt","w",stdout);

	int T;
	scanf("%d",&T);
	for (int z=1; z<=T; z++) {
		int r1,r2,B1[5][5],B2[5][5];
		scanf("%d",&r1);
		for (int i=1; i<=4; i++) {
			for (int j=1; j<=4; j++) {
				scanf("%d",&B1[i][j]);
			}
		}
		scanf("%d",&r2);
		for (int i=1; i<=4; i++) {
			for (int j=1; j<=4; j++) {
				scanf("%d",&B2[i][j]);
			}
		}
		int cnt=0,n;
		for (int i=1; i<=4; i++) {
			for (int j=1; j<=4; j++) {
				if (B1[r1][i] == B2[r2][j]) {
					cnt++;
					n=B1[r1][i];
				}
			}
		}
		printf("Case #%d: ", z);
		if (cnt==0) { printf("Volunteer cheated!\n"); }
		else if (cnt==1) { printf("%d\n",n); }
		else { printf("Bad magician!\n"); }
	}

	
}
