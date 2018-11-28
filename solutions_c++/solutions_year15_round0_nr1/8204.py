#include <bits/stdc++.h>
#define _SPEED_ ios::sync_with_stdio(0);cin.tie(0);cout.tie(0);
#define ADJ vector< vector<int> > 
#define VI vector<int>
#define sz(x) (int)(x.size())
#define endl '\n'
#define pb push_back
#define mp make_pair
#define ll long long
#define ii pair<int,int>
#define F first
#define S second
#define all(x) (x).begin(),(x).end()
#define oo numeric_limits<int>::max()
#define OO numeric_limits<ll>::max()

using namespace std;

int main() {
	_SPEED_
	freopen("a.in" , "r" , stdin);
	freopen("a.out" , "w" , stdout);
	int t;
	cin >> t;
	for(int T = 1; T <= t; ++T) {
		int n;
		cin >> n;
		string s;
		cin >> s;
		int ans = 0 , out = 0;
		for(int i = 0; i < s.size(); ++i) {
			if(ans < i) {
				out += i - ans;
				ans = i;
			}
			ans += s[i]-'0';
		}
		cout << "Case #" << T << ": " << out << endl;
	}
}
