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
    int T, N, x;
    ll buff, r;
    getint(T); 
    loop(i, T) {
    	getint(N);
    	x = 1;

    	if (N == 0) {
    		pf("Case #%d: INSOMNIA\n", i+1);
    		continue;
    	}

    	map<int, int> m;
    	// map<int> v;
    	loop(j, 10) {
    		m[j] = 0;
    	}

    	while (m.SZ > 0) {
    		buff = N * x;
    		while (buff > 0) {
    			r = buff % 10;
    			buff /= 10;
    			if (m.find(r) != m.end()) m.erase(r);
    		}
    		x++;
    	}

        buff = N*(x-1);

    	pf("Case #%d: %lld\n", i+1, buff);
    }
    return 0;
}