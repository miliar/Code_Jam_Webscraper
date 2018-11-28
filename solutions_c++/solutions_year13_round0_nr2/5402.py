#include <stdio.h>

#define MX 120

int T,C;
int N,M;
int inp[MX][MX];

int MAX(int x, int y) { return x>y?x:y;}

int main()
{
	freopen("input.txt","r",stdin); freopen("output.txt","w",stdout);

	scanf("%d",&T);
	while(T) {
		
		int i,j,k,Flag=0;

		scanf("%d %d",&N,&M);
		for(i=0;i<MX;i++) for(j=0;j<MX;j++) inp[i][j]=0;
		for(i=0;i<N;i++) {
			for(j=0;j<M;j++) {
				scanf("%d",&inp[i][j]);
			}
		}

		for(i=0;i<N;i++) {
			for(j=0;j<M;j++) {

				int max=0, max2=0;
				for(k=0;k<N;k++) {
					max=MAX(max,inp[k][j]);
				}
				for(k=0;k<M;k++) {
					max2=MAX(max2,inp[i][k]);
				}

				if(inp[i][j]<max && inp[i][j]<max2) {
					Flag=1; break;
				}

			}
		}

		if(Flag) printf("Case #%d: NO\n",C+1);
		else printf("Case #%d: YES\n", C+1);

		T--; C++;
	}
}