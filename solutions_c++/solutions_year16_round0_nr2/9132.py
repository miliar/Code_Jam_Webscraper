#pragma comment(linker,"/STACK:64000000")
#include <iostream>
#include <vector>
#include <string>
#include <locale>
#include <set>
#include <cstdio>
#include <map>
#include <algorithm>
#include <ctype.h>
#include <cmath>
#include <cstdlib>
#include <utility>
#include <queue>
#include <iomanip>
#include <stack>
#include <bitset>
#include <functional>
#define _USE_MATH_DEFINES
#define mp make_pair
#define pb push_back      
#define F first
#define S second
#define SS stringstream
#define sqr(x) ((x)*(x))
#define CC(x) cout << (x) << endl
#define pw(x) (1ll<<(x))
#define buli(x) __builtin_popcountll(x)
#define forn(i, n) for(int i = 0 ; (i) < (n) ; ++i)
#define MAX_N 1000000007
#define LL long long
template <class T> T gcd(T a, T b) { return a ? gcd(b % a, a) : b; } 
using namespace std;

int f(string s, int pos) {
	if (pos < 0) return 0;
	int cnt = 0;
	while (pos >= 0 && s[pos] == '-') pos--;
	if (pos >= 0) {
		cnt += 1;
	}
	else {
		return 1;
	}
	while (pos >= 0 && s[pos] == '+') pos--;
	if (pos >= 0) {
		cnt += f(s, pos) + 1;
	}
	else {
		cnt += 1;
	}
	return cnt;
}
int  main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	

	LL t, p, k, res, n, j;
	cin >> t;
	
	
	for (int i = 1; i <= t; ++i) {	
		string s;
		cin >> s;
		int ans = 0;
		int left= 0, right= s.size()-1;
		while (right >= 0 && s[right] == '+') right--;
		ans = f(s, right);
		cout << "Case #" << i << ": " << ans << '\n';
	}

}