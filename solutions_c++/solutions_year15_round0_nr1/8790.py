#include <bits/stdc++.h>
using namespace std;
 
#define rep(i, a, b) for(int i = a; i < int(b); i++)
#define trav(it, v) for(auto it = v.begin(); it != v.end(); it++)
#define all(x) x.begin(), x.end()
#define sz(x) (int) (x).size()
 
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<vector<int>> vvi; 

int solve() {
	int n;
	string s;
	cin >> n >> s;
	int c = 0, ans = 0;
	rep(i, 0, n+1) {
		if(s[i] > '0') {
			if(c < i) {
				ans += i-c;
				c = i;
			}
			c += s[i] - '0';
		}
	}
	return ans;
}

int main() {
	int T;
	cin >> T;
	rep(t, 1, T+1) {
		cout << "Case #" << t << ": " << solve() << endl;
	}
}

