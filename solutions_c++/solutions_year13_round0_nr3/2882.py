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

int tc,t,n,m;

bool ispalin( string s) 
{
	int l = 0, r = s.size()-1;
	
	while ( l < r )
	{
		if ( s[l] != s[r] ) return 0;
		l++; r--;
	}
	
	return 1;
}

bool con( int a )
{
	string s = "";
	if ( a == 0 ) s = "0";
	while ( a > 0 )
	{
		int x = a % 10;
		a /= 10;
		s = (char)(x+'0') + s;
	}
	
	return ispalin(s);
}

bool p( int x) 
{
	for ( int i = 1; ; i++)
	{
		if ( i * i > x ) return 0;
		if ( i * i == x ) return 1;
	}
}

int main()
{
	scanf("%d",&t);
	FOR(tc,1,t)
	{
		int res = 0;
		scanf("%d%d",&n,&m);
		for ( int i = n; i <= m; i++ ) 
			if ( con(i) && p(i) && con(floor(sqrt(i))) ) 
			{
				//cout << i << endl;
				res++;
			}
		
		printf("Case #%d: %d\n",tc,res);
	}
	
	return 0;
}
