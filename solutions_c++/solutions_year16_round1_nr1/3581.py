#include <bits/stdc++.h>

#define  fi  first
#define  se  second
#define  pb  push_back
#define  pf  push_front
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

deque <char>  v;

int main() {
	freopen("file.in", "r", stdin);
	freopen("file.out", "w", stdout);
	int t;
	string s;
	char a;
	cin>>t;
	for (int i=1;i<=t;i++) {
		cin>>s;
		v.pb(s[0]);
		for (int j=1;j<s.size();j++) {
			a=v[0];
			if (int(s[j])>=int(a)) v.pf(s[j]);
			else v.pb(s[j]);
		}
		cout<<"Case #"<<i<<": ";
		for (int j=0;j<v.size();j++) cout<<v[j];
		cout<<endl;
		v.clear();
	}
}

