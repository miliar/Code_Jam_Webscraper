#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
 
#include <algorithm>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include <map>
 
#define FOR(i, s, e) for(int i=s; i<e; i++)
#define loop(i, n) for(int i=0; i<n; i++)
#define getint(n) scanf("%d", &n)
#define pb(a) push_back(a)
#define ll long long
#define SZ size()
#define read(filename) freopen(filename, "r", stdin)
#define write(filename) freopen(filename, "w", stdout)
#define mem(a, v) memset(a, v, sizeof(a))
#define all(v) v.begin(), v.end()
#define pi acos(-1.0)
#define INF 1<<29
#define mod(a) (a>0?a:-a)
#define pf printf
 
using namespace std;
 
int main()
{
    int T, K, C, S;
    getint(T); 

    long long x, pos;
    loop(i, T) {
    	getint(K);
    	getint(C);
    	getint(S);

    	x = 1;
    	pos = 1;

    	loop(j, C - 1) {
    		x *= K;
    	}

    	pf("Case #%d: ", i+1);
    	loop(j, K) {
    		pf("%lld ", pos);
    		pos += x;
    	}
    	pf("\n");
    }
    return 0;
}