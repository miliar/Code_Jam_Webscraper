#include <iostream>
#include <set>
#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <queue>
#include <algorithm>
#include <functional>
#include <cstring>
#include <cmath>
#include <cstdio>

using namespace std;

#define Clear(t) memset((t),0,sizeof(t))
#define For(i,a,b) for (int i=(int)(a),_t = (int)(b);i<=_t;i++)
#define Ford(i,a,b) for (int i=(int)(a), _t = (int)(b);i>=_t;i--)
#define Rep(i,n) for (int i=0, _t = (int)(n);i<_t;i++)
#define tr(it, c) for(typeof(c.begin()) it = c.begin(); it != c.end(); it++)
#define SZ(t) ((int)((t).size()))
#define All(v) (v).begin(),(v).end()
#define Sort(v) sort(All(v))
#define pb push_back

typedef vector<int> VI;
typedef long long ll;
typedef vector<ll> VL;
typedef vector<string> VS;

string i2s(int x) { ostringstream o; o<<x; return o.str(); }
string ll2s(ll x) { ostringstream o; o<<x; return o.str(); }
int s2i(string s) { int x; istringstream i(s); i>>x; return x; }

bool isPalin(string s) {
	int n = SZ(s);
	Rep(i,n/2) if (s[i] != s[n-i-1]) return false;
	return true;
}
bool isPalinLL(ll x) {
	return isPalin(ll2s(x));
}

bool isPalinI(int x) {
	return isPalin(i2s(x));
}

int main() {
	freopen("C-large-1.in","r",stdin);
	freopen("C-large-1.out","w",stdout);
	
	ll a[100];

	int cnt = 0;
	For(i,1,10000000) if (isPalinI(i)) {
		ll x = i;
		x*=i;
		if (isPalinLL(x)) a[cnt++] = x;
	}
	
	int st;
	cin>>st;
	For(ts,1,st) {
		ll x, y;
		cin>>x>>y;
		int res = 0;
		Rep(i,cnt) if (a[i] >= x && a[i] <=y) res++;
		
		cout<<"Case #"<<ts<<": "<<res<<endl;
	}

	return 0;
}
