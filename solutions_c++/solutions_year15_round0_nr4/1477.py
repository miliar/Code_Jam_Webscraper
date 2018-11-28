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

ifstream fin("D-small-attempt0.in");
ofstream fout("D-small-attempt0.out");


void print(string n, ll level) {
	cout << "Case #" << level << ": " << n << endl; 
	return;
}

ll T, ans, X, R, C;

int main() {
	ios_base::sync_with_stdio(false);
	cin >> T;
	for(ll level = 1; level <= T; level++) {
		cin >> X >> R >> C;
		if(X == 1)
			ans = 2;
		if(X == 2) {
			if(R * C % 2 == 0)
				ans = 2;
			else
				ans = 1;
		}
		if(X == 3) {
			if(R * C % 3 != 0)
				ans = 1;
			else {
				if(R * C == 3)
					ans = 1;
				else
					ans = 2;
			}
		}
		if(X == 4) {
			if(R < 4 && C < 4)
				ans = 1;
			else {
				if(R * C == 4 || R * C == 8)
					ans = 1;
				else
					ans = 2;
			}
		}
		string ans2;
		if(ans == 1)
			ans2 = "RICHARD";
		else
			ans2 = "GABRIEL";
		print(ans2, level);
	}
	return 0;
}