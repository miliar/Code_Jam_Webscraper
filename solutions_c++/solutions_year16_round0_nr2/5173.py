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
typedef pair<int,string> ii;
const int N = 100005;
const ll mod = (ll) 1e9 + 7;

int main() {
	ios_base::sync_with_stdio(false);
	int test;
	cin >> test;
	fore(t,0,test) {
		string s;
		cin >> s;
		int n = s.size();
		ll res = 0;
		s += "$";
		bool p=0,m=0;
		fore(i,0,n) {
			if(s[i] == '-')
				m = 1;
			if(s[i] == '+' && m) {
				if(p)
					res += 2LL;
				else
					res++;
				m = 0;
				p = 1;
			} else if(s[i] == '+') {
				p = 1;
			}
		}
		if(m) {
			if(p)
				res += 2LL;
			else
				res++;
		}
		cout << "Case #" << t+1 << ": " << res << endl;
	
	
	}
}
