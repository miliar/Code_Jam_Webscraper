#define _USE_MATH_DEFINES

#include <iostream>
#include <cstdio>
#include <vector>
#include <cmath>
#include <list>
#include <iomanip>
#include <stack>
#include <map>
#include <set>
#include <queue>
#include <string>
#include <algorithm>
#include <iomanip>
#include <cstring>
#include <cstdlib>
#include <cassert>
#include <cstring>
#include <ctime>

#define all(a) a.begin(),a.end()
#define pb push_back
#define mp make_pair
#define forn(i,n) for(int i = 0; i < int(n); ++i)
#define sz(a) int(a.size())

using namespace std;

const int INF = 1e9;

typedef long long li;
typedef long double ld;

typedef pair<li, li> pt;
#define ft first
#define sc second
#define x first
#define y second

int n;
const int N = 2000;
int a[N];

bool read() {
	if (!(cin >> n))
		return false;
	forn (i, n)
		cin >> a[i];
	return true;
}

int f(int x) {
	int res = x;
	forn (i, n)
		res += (a[i] - 1) / x;
	return res;
}

void solve() {
	
	int fans = INF;
	int ans;
	for (int i = 1; i <= 1000; ++i)
		if (f(i) < fans)
			fans = f(i), ans = i;
	cout << fans << endl;
}

int main() {
#ifdef _DEBUG
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
	
	int t;
	cin >> t;
	forn (i, t) {
		read();
		cout << "Case #" << i + 1 << ": "; 
		solve();
	}
    
    return 0;
}