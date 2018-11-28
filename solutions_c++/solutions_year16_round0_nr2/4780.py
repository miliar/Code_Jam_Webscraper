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
#define getstring(s) scanf("%s", s)
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
    int T, n, c, r;
    char s[100];
    char x, y;
    getint(T); 
    loop(i, T) {
    	getstring(s);
    	n = strlen(s);
    	c = 0;

    	if (n == 1) {
    		if (s[0] == '-') {
    			pf("Case #%d: 1\n", i+1);
    			continue;
    		} else {
    			pf("Case #%d: 0\n", i+1);
    			continue;
    		}
    	}

    	x = s[0];
    	FOR(j, 1, n) {
    		y = s[j];
    		if (x != y) c++;
    		x = s[j];
    	}

    	if (s[n-1] == '-') c++;

    	pf("Case #%d: %d\n", i+1, c);
    }
    return 0;
}