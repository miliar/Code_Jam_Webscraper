#include <iostream>
#include <sstream>
#include <cstdio>
#include <vector>
#include <cmath>
#include <queue>
#include <string>
#include <cstring>
#include <cassert>
#include <iomanip>
#include <algorithm>
#include <set>
#include <map>
#include <ctime>
#include <cmath>

#define forn(i, n) for(int i=0;i<n;++i)
#define fore(i, l, r) for(int i = int(l); i <= int(r); ++i)
#define for1(i, n) for(int i=1;i<=n;++i)
#define forv(i, v) for(int i=0;i<v.size();++i)
#define sz(v) int(v.size())
#define all(v) v.begin(), v.end()
#define pb push_back
#define mp make_pair
#define x first
#define y second
#define ft first
#define sc second
#define pt pair<int, int>

typedef long long li;
typedef long double ld;


using namespace std;

const int N = 10 * 1000 + 13, INF = 1000*1000*1000;
const ld  eps = 1e-9;

int a[N];

bool solve(int test) {
	printf("Case #%d: ", test + 1);
	int n, c;
	scanf("%d%d", &n, &c);
	forn(i, n) {
    	scanf("%d", &a[i]);
    }

    sort(a, a + n);
    int i = 0; 
    int j = n - 1;
    int ans = 0;
    for(; i <= j; ) {
    	if (a[i] + a[j] <= c) {
    		ans++;
    		i++;
    		j--;
    	} else {
    		ans++;
    		j--;
    	}
    }
	printf("%d\n", ans);
	return false;
}

int main () {	
#ifdef IKAR
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
    int n;
    scanf("%d", &n);
    forn(i, n)
    	solve(i);
	cerr << "TIME: " << clock() << endl;
	return 0;
}