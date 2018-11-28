#include <bits/stdc++.h>

#define debug(x) cout << #x << " = " << x << endl
#define fori(i, ini, lim) for(int i = int(ini); i < int(lim); i++)
#define ford(i, ini, lim) for(int i = int(ini); i >= int(lim); i--)

using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair<int, int> ii;

ll f_exp(ll n, ll exp) {
	if(exp > 1) {
		if(exp & 1) {
			return n * f_exp(n, exp - 1);
		}
		else {
			return f_exp(n * n, exp / 2);
		}
	}
	return !exp ? 1LL : n;
}

int K, C, S;
ll roll(ll i, ll c) {
	if(c == -1) {
		return 0LL;
	}
	return roll(i, c - 1) + (i - 1) * f_exp(K, c);
}

int main() {
	ios_base::sync_with_stdio(false);
	
	int kase = 1;
	int t;
	cin >> t;
	while(t--) {
		cin >> K >> C >> S;
		
		cout << "Case #" << kase++ << ":";
		if(C == 1) {
			fori(i, 1, K + 1) {
				cout << " " << i;
			}
			cout << '\n';
		}
		else {
			for(int i = 1; i < K; i += 2) {
				cout << " " << roll(i, C - 1) + 2;
			}
			if(K & 1) {
				cout << " " << f_exp(K, C);
			}
			cout << '\n';
		}
	}

	return 0;
}
