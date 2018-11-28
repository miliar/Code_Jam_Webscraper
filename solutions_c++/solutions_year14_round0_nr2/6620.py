#include<cstdio>
#include<algorithm>
#include<iostream>
#include<cstdlib>
#include<cassert>
#include<cstring>
#include<vector>
#include<string>
#include<cmath>
#include<ctime>
#include<set>
#include<map>
 
using namespace std;
 
#define sz(c) (int)(c).size()
 
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
 
#define forn(i,n) for( int i = 0 ; i < (n) ; i++ )
#define forit(it,c) for( __typeof((c).begin()) it = (c).begin() ; it != (c).end() ; it++ )
 
#ifdef WIN32
#define INT64 "%I64d"
#else
#define INT64 "%lld"
#endif
 
#define FNAME "1"

int T;
double c, f, x, ans, v, t;

int main()
{
    freopen(FNAME".in", "r", stdin);
    freopen(FNAME".out", "w", stdout); 
	scanf("%d", &T);
	for (int g = 0; g < T; g++)
	{
		scanf("%lf%lf%lf", &c, &f, &x);
		ans = 1e9;
		v = 2;
		t = 0;
		for (int i = 0; i < 1000000; i++)
		{
			ans = min(ans, t + x / v);
			t += c / v;
			v += f;
		}	
		printf("Case #%d: %.20lf\n", g + 1, ans);
	} 
    return 0;
}