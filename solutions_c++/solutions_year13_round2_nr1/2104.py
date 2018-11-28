#include <algorithm>
#include <stdio.h>
#include <iomanip>
#include <cstdlib>
#include <cmath>
#include <string.h>
#include <iostream>
#include <limits.h>
#include <cctype>
#include <cfloat>
#include <bitset>
#include <vector>
#include <queue>
#include <stack>
#include <deque>
#include <map>
#include <set>
using namespace std;

#define exit exit(0)
#define RESET(a) memset(a,0,sizeof(a))
#define fi first
#define EPS 1e-9
#define se second
#define pb push_back
#define mp make_pair
#define FOR(a,b,c) for(a=b; a<=c; a++)
#define FORR(a,b,c) for(a=b; a<c; a++)
#define FORD(a,b,c) for(a=b; a>=c; a--)
#define bugy int abdc; cin >> abdc
#define cbm(a) ( 1 << a )
#define ALL(a) a.begin(), a.end()

typedef vector <int> vi;
typedef queue <int> qi;
typedef pair <int,int> pii;
typedef pair <double,double> pdd;
typedef long long LL;
int myr[8] = {0, 0, -1,1,-1, 1, -1, 1};
int myc[8] = {1,-1, 0, 0, 1, -1, -1, 1};
int LMAX = 2147483647;
int LMIN = -2147483647;
//LL LLMAX = 9223372036854775807LL;
//LL LLMIN = -9223372036854775808LL;
int mo = 1000000007;

// ~~~~~~~~~~~~~~~~~~~~~~#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#~~~~~~~~~~~~~~~~ //
// ~~~~~~~~~~~~~~~~~~~~~~#~~~~~~~~~~@Willson Copyright@~~~~~~~~~~~~#~~~~~~~~~~~~~~~~ //
// ~~~~~~~~~~~~~~~~~~~~~~#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#~~~~~~~~~~~~~~~~ //

int tc,t,n;
int a;
int f[102];
int dp[12][12][2000];

int rek( int p , int l, int x )
{
	if ( p > l ) return 0;
	
	int &res = dp[p][l][x];
	if ( res != -1 ) return res;
	res = rek(p,l-1,x)+1;
	
	if ( f[p] < x ) res = min(res, rek(p+1,l,x+f[p]));
	else res = min(res, rek(p,l,x+x-1)+1);
	return res;
}

int main()
{
	scanf("%d",&t);
	FOR(tc,1,t)
	{
		printf("Case #%d: ",tc);
		scanf("%d%d",&a,&n);
		for ( int i = 1; i <= n; i++ ) scanf("%d",&f[i]);
		sort(f+1,f+1+n);
		memset(dp,-1,sizeof(dp));
		printf("%d\n",rek(1,n,a));
	}
	return 0;
}
