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
LL LLMAX = 9223372036854775807LL;
LL LLMIN = -9223372036854775808LL;
int mo = 1000000007;

// ~~~~~~~~~~~~~~~~~~~~~~#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#~~~~~~~~~~~~~~~~ //
// ~~~~~~~~~~~~~~~~~~~~~~#~~~~~~~~~~@Willson Copyright@~~~~~~~~~~~~#~~~~~~~~~~~~~~~~ //
// ~~~~~~~~~~~~~~~~~~~~~~#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#~~~~~~~~~~~~~~~~ //

int n,m,tc,t;
int f[120][120];
int r[120], c[120];
bool yeah;

int main()
{
	scanf("%d",&t);
	FOR(tc,1,t)
	{
		scanf("%d%d",&n,&m);
		for ( int i = 1; i <= n; i++ )
			for ( int j = 1; j <= m; j++ )
				scanf("%d",&f[i][j]);
				
		yeah = true;
		
		RESET(r); RESET(c);
		for ( int i = 1; i <= n; i++ )
		{
			for ( int j = 1; j <= m; j++ )
				r[i] = max(r[i],f[i][j]);
		}
		
		for ( int j = 1; j <= m; j++ )
		{
			for ( int i = 1; i <= n; i++ )
				c[j] = max(c[j],f[i][j]);
		}
		
		for ( int i = 1; i <= n; i++ )
			for ( int j = 1; j <= m; j++ )
				if ( c[j] != f[i][j] && r[i] != f[i][j] )
				{
					yeah = 0;
					break;
				}
		
		printf("Case #%d: ",tc);
		if ( yeah ) printf("YES\n"); 
		else printf("NO\n");
	}
	return 0;
}