#include<stdio.h>
#include<algorithm>
#include<set>

#define maxn 10005

using namespace std;

int n;
int a[maxn];
multiset<int>S;

int main () {
	
	freopen("codejam.in","r",stdin);
	freopen("codejam.out","w",stdout);
	
	int tests;
	scanf("%d",&tests);
	
	for ( int ii = 1 ; ii <= tests ; ++ii ){
		
		int cap;
		scanf("%d %d",&n,&cap);
		for ( int i = 1 ; i <= n ; ++i ){
			scanf("%d",&a[i]);
			S.insert(a[i]);
		}
		
		int sol = 0;
		while ( !S.empty() ){
			int x = *(S.begin());
			multiset<int>::iterator itt = S.upper_bound(cap-x);
			++sol;
			if ( itt != S.begin() ){
				--itt;
				if ( itt != S.begin() ){
					S.erase(itt);
				}
			}
			S.erase(S.begin());
		}
		
		printf("Case #%d: %d\n",ii,sol);
	}
	
	return 0;
}
