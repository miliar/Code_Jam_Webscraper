// Headers 
#include<bits/stdc++.h>
using namespace std;
// Global declarations
typedef long long int ll;
typedef vector<int> vi;
typedef vector<char> vc;
typedef pair<int, int> pi;
typedef pair<ll, ll> pll;
const int mod = 1e9 + 7;
const int INF = 1 << 29;
// Macros
#define mp make_pair
#define el putchar('\n')
#define sp putchar(' ')
#define Fill(a,val) memset(a,val,sizeof a)
#define all(a) a.begin(),a.end()
#ifndef ONLINE_JUDGE
#define tr(a, it) for (decltype(a.begin()) it = a.begin(); it != a.end(); ++it)
#else 
#define tr(a, it) for (typeof(a.begin()) it = a.begin(); it != a.end(); ++it)
#endif
#define in(n) scanf("%d",&n)
#define inl(n) scanf("%lld",&n)
#define out(n) printf("%d",n);
#define outl(n) printf("%lld",n);

string ans;
string s;

string g(vc &vv){
	string ret;
	tr(vv, it){
		ret += (*it);
	}
	return ret;
}

void f(vc &vv, int idx, int n){
	if (idx == n){
		if (ans == "#")
			ans = g(vv);
		else
			ans = max(ans, g(vv));
	}
	else {
		vv.insert(vv.begin(), s[idx]);
		f(vv, idx + 1, n);
		vv.erase(vv.begin(), vv.begin() + 1);
		vv.push_back(s[idx]);
		f(vv, idx + 1, n);
		vv.pop_back();
	}
}

int main(){
	freopen("ip.in", "r", stdin);
	freopen("op.out", "w", stdout);
	int t;
	in(t);
	int cs = 1;
	while (t--){		
		cin >> s;
		int n = s.length();
		vc vv;
		vv.push_back(s[0]);
		ans = '#';
			f(vv, 1, n);
		printf("Case #%d: ", cs++); cout << ans; el;
	}
	return 0;
}