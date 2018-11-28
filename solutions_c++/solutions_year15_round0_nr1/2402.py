#include <bits/stdc++.h>
#include <fstream>
#define X first
#define Y second
#define pb push_back
#define popb pop_back
#define mp make_pair
#define cin fin
#define cout fout
using namespace std;
typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef pair<ld, ld> point;

ifstream fin("A-large.in");
ofstream fout("A-large.out");


void print(ll n, ll level) {
	cout << "Case #" << level << ": " << n << endl; 
	return;
}

ll T, ans, maxs, up;
string s;

int main() {
	ios_base::sync_with_stdio(false);
	cin >> T;
	for(ll level = 1; level <= T; level++) {
		ans = up = 0;
		cin >> maxs >> s;
		for(ll i = 0; i <= maxs; ++i) {
			if(s[i] == '0') continue;
			if(up < i) ans += (i - up);
			up = max(up + s[i] - '0', i + s[i] - '0');
		}
		print(ans, level);
	}
	return 0;
}