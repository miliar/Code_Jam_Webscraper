#include<bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int,int> pii;

#define fi first
#define se second
#define sz(x) x.size()
#define pb push_back
#define mp make_pair
#define all(v) (v).begin(),(v).end()
#define forn(i,a,n) for(int i = a; i < n; i++)
#define dbg(a) cout << #a << " = " << a << endl


int solve(int test) {
	string s;
	cin >> s;
	string t = "";
	t += s[0];
	
	for(int i = 1; i < s.length(); i++) {
		if(s[i] != s[i-1]) {
			t += s[i];
		}
	}
	
	int c = t.length();
	if(t[t.length() - 1] == '+') {
		c--;
	}
	
	cout << "case #" << test << ": " << c << endl;
	
}

int main() {
	
freopen("B-large.in", "r", stdin);
freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	for(int i = 1; i <= t; i++) {
		solve(i);
	}

	return 0;
}

