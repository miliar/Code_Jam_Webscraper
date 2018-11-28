#include <bits/stdc++.h>
#define all(v) v.begin(),v.end()
#define fore(i,a,n) for(int i=a;i<n;i++)
#define rev(i,n) for(int i = n-1; i>= 0; i--)
#define pb push_back
#define mp make_pair
#define dprint(v) cerr << #v " = " << v << endl
#define endl '\n'
#define fill(m,v) memset(m,v,sizeof m)
using namespace std;

typedef long long ll;
typedef pair<int,int> ii;
const int N = 1000005;
const ll mod = (ll) 1e9 + 7;


int main() {
	int t,caso=0;
	cin >> t;
	while(t--) {
		ll a;
		int flag = 0;
		cin >> a;
		if(a == 0) {
			cout << "Case #" << ++caso <<": " << "INSOMNIA" << endl;
			continue;
		} else {
			ll cur,res=0;
			for(ll i = 1LL; i<N;i++) {
				cur = a * i;
				while(cur) {
					int tmp = cur%10;
					cur/=10;
					flag |= 1 << tmp;
				}
				if(flag == (1 << 10)-1) {
					res = a * i;
					break;
				}
			}
			if(res)
				cout << "Case #" << ++caso <<": " <<  res << endl;
			else
				cout << "Case #" << ++caso <<": " <<  "INSOMNIA" << endl;
		
		}
	}
}
