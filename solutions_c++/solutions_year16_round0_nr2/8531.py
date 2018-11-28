#include <bits/stdc++.h>
using namespace std;

#define sz(v)			(int)(v.size())
#define aint(v)			v.begin(),v.end()
#define mems(a , i)		memset(a , i , sizeof(a))
#define memc(a , b)		memcpy(a , b , sizeof(a))
#define mp(x , y)		make_pair(x , y)
#define pb(x)			push_back(x)
#define ansy			{cout << "-1" << endl;return 0;}
#define ansn			{cout << "No" << endl;return 0;}
#define IOS				ios_base::sync_with_stdio(0) , cin.tie(0) , cout.tie(0);
#define mod				10007
#define PI				3.14159265358979323846
#define fi				first
#define se				second
#define all(v)			v.begin(), v.end()
const double EPS = 1e-8;


int main() {
#ifndef ONLINE_JUDGE
	freopen("/home/momen/Downloads/B-large.in", "rt", stdin);
	freopen("output.txt", "wt", stdout);
#endif
	IOS;
	int t;
	cin >> t;
	string s;
	for(int tt = 1; tt <= t ; tt++){
		cin >> s;
		int ans = 0;
		for(int i = 1 ; i < sz(s) ; i++){
			ans += (s[i-1] != s[i]);
		}
		ans += (s.back() == '-');
		cout << "Case #"<< tt << ": " << ans << "\n";
	}

	return 0;
}

