/*
  /\     /\
  | ).|.( |
  |  >-<  |
  =========
It's AdilkhanKo miaaaaaau
*/
#include<bits/stdc++.h>

#define ll long long
#define pb push_back
#define endl "\n"
#define foreach(it, S) for(__typeof (S.begin()) it = S.begin(); it != S.end(); it++)
#define mp make_pair
#define f first
#define s second
#define name ""
#define _ ios_base::sync_with_stdio(false);cin.tie(0);

using namespace std;

const int MaxN = int (1e5);
const int INF = int(1e9);
const int mod = (int)(1e9) + 7;
const double pi = 3.1415926535897932384626433832795;
ll n, m, t, ans = -INF, a[11];

int main () { _
	#ifdef ONLINE_JUDGE
//		freopen (name".in","r",stdin);
//		freopen (name".out","w",stdout);
	#else
		freopen (".in","r",stdin);
		freopen (".out","w",stdout);
	#endif
	cin >> t;
	for(int T = 1; T <= t; T++){
		cout << "Case #" << T << ": ";
		ll x; cin >> x;
		int cnt = 0;
		ll i = 1;
		memset(a, 0, sizeof a);
		for(i = 1; i <= MaxN; i++){
			ll X = x * i;
			while(X){
				if(a[X % 10] == 0){
					cnt++;
					a[X % 10] = 1;
				}
				X /= 10;
			}
			if(cnt == 10)break;
		}       
		if(cnt == 10)cout << i * x << endl;
		else cout << "INSOMNIA" << endl;
	}
}
