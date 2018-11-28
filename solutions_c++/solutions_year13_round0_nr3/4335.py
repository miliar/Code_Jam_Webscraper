#pragma comment(linker, "/STACK:64000000")
#include <iostream> 
#include <stdio.h> 
#include <cmath> 
#include <string> 
#include <vector> 
#include <algorithm> 
#include <queue> 
#include <sstream> 
#include <utility> 
#include <map> 
#include <set> 
#include <memory.h> 
using namespace std; 
 
#define forn(i, n) for(int i = 0; i < (int) (n); ++i) 
#define fore(i, a, b) for(int i = (int) (a); i < (int) (b); ++i) 
 
#define ll long long 
#define ld long double 
#define PLL pair <ld, ld> 
#define PII pair <int, int> 
#define pb push_back 
#define sz size

const ld EPS = 1e-7; 

const int MAXN = 510;

const int MAXS = int(1e6 + 1e-6 + 5);
const ll BASE = int(1e9 + 1e-1 + 9); 
const ld PI = 3.1415926535897932384626433832795; 
const int INF = 1e30;

vector <ll> q;

bool is_pal(ll x) {
	char tmp[16];
	sprintf(tmp, "%lld", x);
	string s = tmp;
	string s1 = s;
	reverse(s1.begin(), s1.end());

	return s == s1;
	vector <int> v;

	while (x) {
		v.pb(x % 10);
		x /= 10;
	}

	for(int i = 0, j = int(v.size()) - 1; i < j; ++i, --j) {
		if (v[i] != v[j]) return 0;
	}

	return 1;
}

int solve(ll x) {

	if (x < q[0]) return 0;

	int l = 0, r = (int)(q.size()) - 1;
	if (x > q[r]) return q.size();

	while (r - l > 1) {
		int m = (l + r) / 2;

		if (q[m] > x) r = m;
		else
			l = m;
	}

	return l + 1;
}

int main()  { 
     
    freopen("input.txt","rt", stdin); 
	freopen("output.txt", "wt", stdout);     
    
	q.clear();

	q.reserve((int)(1e3));

	fore(i, 1, (int)(1e7 + 1e-7 + 10)) {
		if (!is_pal(i)) continue;
		ll x = (ll)(i) * i;
		if (!is_pal(x)) continue;

		q.pb(x);
		//cout << x << endl;
	}
	
	//cout << "done\n" << endl;

	int tk;
	cin >> tk;

	fore(test, 1, tk + 1) {
		int ans = 0;

		ll x, y;
		cin >> x >> y;

		ans = solve(y) - solve(x - 1);

		printf("Case #%d: %d\n", test, ans);
	}


    return 0; 
}