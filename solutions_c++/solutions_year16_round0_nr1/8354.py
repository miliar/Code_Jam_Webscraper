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
	ll n;
	cin >> n;
	if(n == 0) {
		cout << "case #" << test << ": INSOMNIA" << endl;
		return 0;
	}
	set<int> s;
	ll q = n;
	while(s.size() < 10) {
		ll x = n;
		while(x) {
			s.insert(x%10);
			x/=10;
		}
		if(s.size() == 10) {
			break;
		}
		
		n += q;
	}
	cout << "case #" << test << ": " << n << endl;
	return 0;
}

int main() {
	
freopen("A-large.in", "r", stdin);
freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	for(int i = 1; i <= t; i++) {
		solve(i);
	}

	return 0;
}

