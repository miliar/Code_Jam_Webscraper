#include <stdlib.h>
#include <stdio.h>
#include <math.h>

#define min(a,b) (a<b?a:b)
#define max(a,b) (a>b?a:b)

int main(){
	int T,i;
	scanf("%d\n",&T);
	for(i=0;i<T;i++){
		printf("Case #%d: ",i+1);
		int tN,tM;
		scanf("%d %d",&tN,&tM);
		const int N=tN,M=tM;
		int lawn[N][M];
		int r,c;
		for(r=0;r<N;r++)
			for(c=0;c<M;c++)
				scanf("%d",&lawn[r][c]);
		int possible=1;
		int rows[N],cols[M];
		for(r=0;r<N;r++){
			rows[r]=0;
			for(c=0;c<M;c++){
				if(r==0)
					cols[c]=lawn[r][c];
				else
					cols[c]=max(cols[c],lawn[r][c]);
				rows[r]=max(rows[r],lawn[r][c]);
			}
		}
		for(r=0;r<N&&possible;r++)
			for(c=0;c<M&&possible;c++)
				if(lawn[r][c]<rows[r]&&lawn[r][c]<cols[c])
					possible=0;
		printf("%s\n",possible?"YES":"NO");
	}
}
