#include <cstdio>
#include <algorithm>

using namespace std;

bool tbl[20][20];

int main(){
	int T;
	scanf("%d",&T);
	for(int cc = 1 ; cc <= T ; cc++){
		int R,C,N;
		scanf("%d %d %d",&R,&C,&N);
		int k = R*C;
		int sol = -1u/2;
		// printf("-------- %d\n",1<<k);
		for(int c = 0 ; c < (1<<k) ; c++){
			int ans = 0, ch = 0;
			for(int d = 0 ; d < k ; d++)
				ch += ((c&(1<<d)) > 0);
			if(ch!=N)continue;
			for(int d = 0 ; d < R ; d++){
				for(int e = 0 ; e < C ; e++){
					int idx = d*C+e;
					bool occ = (c&(1<<idx))>0;
					tbl[d][e] = occ;
				}
			}
			for(int d = 0 ; d < R ; d++)
				for(int e = 0 ; e < C-1 ; e++)
					if(tbl[d][e] and tbl[d][e+1])ans++;
			for(int d = 0 ; d < R-1 ; d++)
				for(int e = 0 ; e < C ; e++)
					if(tbl[d][e] and tbl[d+1][e])ans++;
			sol = min(sol,ans);
			// for(int d = 0 ; d < R ; d++){
			// 	for(int e = 0 ; e < C ; e++){
			// 		printf("%d ",tbl[d][e]);
			// 	}
			// 	printf("\n");
			// }
			// printf(">> %d %d %d\n",c,ans,ch);
		}
		printf("Case #%d: %d\n",cc,sol);
	}
}