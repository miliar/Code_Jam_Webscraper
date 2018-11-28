#include <bits/stdc++.h>

#define  fi  first
#define  se  second
#define  pb  push_back
#define  pf  push-front
#define  ppb  pop_back
#define  ppf  pop_front
#define  all(v)  v.begin(),v.end()
#define  tr(i,c)  for(typeof((c).begin())i=c.begin();i!=c.end();i++)

using namespace std;

typedef long long ll;
typedef pair<int,int> PII;

template <class T> inline void umax(T &x,T y) {if (y > x) x = y;}
template <class T> inline void umin(T &x,T y) {if (y < x) x = y;}

const int N=1e5+9;
const int INF=2*1e9+9;
const int MOD=1e9+7;

ll t,n,ans=0;
bool vis[20];

void getDigits(int x) {
	if (vis[x%10]==0) vis[x%10]=1,ans++;
	if (x/10>0) getDigits(x/10);
}

int main() {
	freopen("file.in", "r", stdin);
	freopen("file.out", "w", stdout);
	cin>>t;
	for (int i=1;i<=t;i++) {
		cin>>n;
		ll q=n;
		if (n==0) cout<<"Case #"<<i<<": INSOMNIA"<<endl;
		else {
			while (ans<10) {
				getDigits(n);
				n+=q;
			}
			cout<<"Case #"<<i<<": "<<n-q<<endl;
			ans=0;
			memset (vis,0,sizeof(vis));
		}
	}
}

