#include <stdio.h>
#include <iostream>
#include <stdlib.h>
#include <cmath>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <deque>
#include <cstring>
#include <memory.h>
#include <bitset>
#include <time.h>
#define sf(x) scanf("%d", &x)
#define sff(x) scanf("%lf", &x)
#define sfc(x) scanf(" %c", &x)
#define pf(x) printf("%d ", x)
#define pff(x) printf("%lf", x)
#define pfc(x) printf("%c", x)
#define pfs(x) printf("%s", x)
#define sfl(x) scanf("%I64d", &x)
#define sfl2(x,y) scanf("%I64d %I64d", &x,&y)
#define ENDL printf("\n")
#define INF 2147483647
#define pf2(x,y) printf("%d %d", x,y)
#define sf2(x,y) scanf("%d %d", &x,&y)
#define pb(x) push_back(x)
#define ppb() pop_back()
#define mp(x,y) make_pair(x,y)
#define sf3(x,y,z) scanf("%d %d %d", &x,&y,&z)
#define print(x) puts(#x)
#define error(x) cerr<<#x<<' '<<x<<'\n'


using namespace std;

typedef long long ll; 
typedef unsigned int uint;
typedef unsigned long long ull;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef pair<double, double> pdd;
typedef vector<int> vec;




int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int t;
	sf(t);
	for(int T=1; T<=t; T++)
	{
		int n;
		sf(n);
		int a[10001];
		a[0]=0;
		int s=0;
		int delta=0;
		for(int i=1; i<=n; i++)
		{
			sf(a[i]);
			if(a[i-1]>a[i])
			{
				s+=a[i-1]-a[i];
				delta=max(delta,a[i-1]-a[i]);
			}
		}
		int s2=0;
		for(int i=1; i<n; i++)
		{
			s2+=min(delta, a[i]);
		}
		printf("Case #%d: %d %d\n",T,s,s2);
	}
    return 0;
}












