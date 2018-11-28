#include<bits/stdc++.h>

using namespace std;

#define FOR(i,a,b) for(int i = a; i < b; i++) 
#define FORR(i,b) FOR(i,0,b)
#define FORE(i, a, b) for(int i = a; i >= b; --i)
#define sz(x) (int)x.size()
#define all(x) x.begin(), x.end()
#define pb push_back
#define CLR(x,e) memset(x, e, sizeof x)

typedef long long ll;
typedef pair<int, int> ii;
typedef pair<ll, ll> pll;
typedef vector<int> vi;
typedef vector<vi> vvi;

ll gcd (ll a, ll b) { return (b ? gcd (b, a%b) : a); }
ll mmc (ll a, ll b) { return a / gcd (a, b) * b; }

int main () {
	ios_base::sync_with_stdio(false);
	cin.tie (NULL);
	
	int L; cin>>L;
	FORR (caso, L) {
		cout << "Case #" << caso+1 << ": ";
		string s;
		cin>>s;
		string last = "";
		FORR (i, sz(s)) {
			string tmp1 = "", tmp2 = "";
			tmp1 += s[i]; tmp1 += last;
			tmp2 += last; tmp2 += s[i];
			if (tmp1.compare (tmp2) < 0) last = tmp2;
			else last = tmp1;
		}
		cout << last << endl;
	}
}	
