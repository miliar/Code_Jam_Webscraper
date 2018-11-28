#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef vector<vi> vvi;
typedef pair<int, int> pii;
typedef vector<pii> vii;
typedef vector<bool> vb;
typedef vector<string> vs;
const int MOD = 1e9 + 7;
const int di[] = { -1,0,1,0 };
const int dj[] = { 0,1,0,-1 };
#define INF 1000000000
#define mp make_pair
#define x first
#define y second

int main() {
	ios::sync_with_stdio(false), cin.tie(0);
	ifstream cin("A-large.in");
	ofstream cout("output.txt");
	int t, tt = 0; cin >> t;
	while (t--) {
		string s; int k; cin >> s >> k;
		int r = 0;
		for (int i = 0; i < s.length() - k + 1; i++)
			if (s[i] == '-') {
				r++;
				for (int j = i; j < i + k; j++)
					s[j] = s[j] == '-' ? '+' : '-';
			}
		bool imp = false;
		for (int i = 0; i < s.length(); i++)
			if (s[i] == '-') {
				imp = true;
				break;
			}
		cout << "Case #" << ++tt << ": ";
		if (imp)
			cout << "IMPOSSIBLE" << endl;
		else
			cout << r << endl;
	}
	//cin.ignore(), cin.get();
}
