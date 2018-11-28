#include<stdio.h>
#include<algorithm>
#include<set>

#define maxn 1005
#define inf (1<<29)

using namespace std;

int n;
int a[maxn],p[maxn],D1[maxn],D2[maxn];
int solback,best_sol;
int x[maxn],used[maxn];

void back ( int niv ){
	
	if ( niv == n+1 ){
		
		int now = 0;
		for ( int i = 1 ; i <= n ; ++i ){
			if ( used[i] )	continue ;
			for ( int j = i+1 ; j <= n ; ++j ){
				if ( used[j] )	continue ;
				if ( a[j] > a[i] ){
					++now;
				}
			}
		}
		
		for ( int i = 1 ; i <= n ; ++i ){
			if ( !used[i] )	continue ;
			for ( int j = 1 ; j <= i ; ++j ){
				if ( !used[j] ){
					++now;
				}
			}
		}
		
		best_sol = min(best_sol,solback+now);
		
		return ;
	}
	
	used[niv] = 1;
	x[++x[0]] = niv;
	int add = 0;
	for ( int i = 1 ; i <= x[0] ; ++i ){
		if ( a[niv] < a[x[i]] ){
			++add;
		}
	}
	
	solback += add;
	back(niv+1);
	solback -= add;
	x[x[0]--] = 0;
	used[niv] = 0;
	
	back(niv+1);
}

inline int solve_small () {
	best_sol = 1<<30;
	back(1);
	return best_sol;
}

int main () {
	
	freopen("codejam.in","r",stdin);
	freopen("codejam.out","w",stdout);
	
	int tests;
	scanf("%d",&tests);
	
	for ( int ii = 1 ; ii <= tests ; ++ii ){
		
		scanf("%d",&n);
		for ( int i = 1 ; i <= n ; ++i ){
			scanf("%d",&a[i]);
		}
//		for ( int i = 1 ; i <= n ; ++i ){
//			int p = 0;
//			for ( int j = 1 ; j <= n ; ++j ){
//				if ( a[i] > a[j] )	++p;
//			}
//			printf("%d ",p+1);
//		}
//		printf("\n");
		
		D1[0] = D2[n+1] = 0;
		for ( int i = 1 ; i <= n ; ++i ){
			D1[i] = D1[i-1];
			for ( int j = 1 ; j < i ; ++j ){
				if ( a[i] < a[j] ){
					++D1[i];
				}
			}
		}
		for ( int i = n ; i >= 1 ; --i ){
			D2[i] = D2[i+1];
			for ( int j = i+1 ; j <= n ; ++j ){
				if ( a[i] < a[j] ){
					++D2[i];
				}
			}
		}
		
		int sol = (1<<30);
		for ( int i = 0 ; i <= n ; ++i ){
			sol = min(sol,D1[i]+D2[i+1]);
		}
		
		int sol2 = solve_small();
//		if ( sol != sol2 )
		printf("Case #%d: %d\n",ii,sol2);
	}
	
	return 0;
}
