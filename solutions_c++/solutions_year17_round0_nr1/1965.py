#include <bits/stdc++.h>

using namespace std;

#define endl '\n'

typedef long long int64;
typedef pair<int,int> pii;
typedef vector<int> vi;

const int oo = 0x3f3f3f3f;
const double eps = 1e-9;
const int maxn = 100000 + 10;

char flip(char c){
	return c == '-' ? '+' : '-';
}

void solve(string s, int k){
	int n = (int)s.length();

	int t = 0;

	for (int i = 0; i <= n - k; ++i){
		if (s[i] == '-'){
			t++;
			for (int j = 0; j < k; ++j)
				s[i + j] = flip(s[i + j]);
		}
	}

	for (int i = 0; i < k - 1; ++i)
		if (s[n - i - 1] == '-'){
			cout << "IMPOSSIBLE" << endl;
			return;
		}

	cout << t << endl;
}

int main(){
	ios_base::sync_with_stdio(0);
	cin.tie(0);

#ifdef MARX
	freopen("data.in", "r", stdin);
	freopen("data.out", "w", stdout);
#endif

	int t; cin >> t;

	int tc = 1;

	while (t--){
		string s;
		int k;

		cin >> s >> k;
		cout << "Case #" << tc++ << ": ";
		solve(s, k);
	}

	return 0;
}