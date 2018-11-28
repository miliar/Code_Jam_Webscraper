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

int ok(string s){
	int n = s.length();
	int ret = -1;
	for (int i = 0; i < n; ++i){
		if (s[i] == '-')
			ret = i;
	}
	return ret;
}

int main(){
	freopen("ip.in", "r", stdin);
	freopen("op.out", "w", stdout);
	int t;
	in(t);
	int cs = 1;
	while (t--){
		string s;
		cin >> s;
		int n = s.length();
		printf("Case #%d: ", cs++);
		int ans = 0;
		int idx;
		while ((idx = ok(s)) != -1){
			ans += s[0] == '+';
			int pos = 0;
			while (pos < n and s[pos] == '+'){
				s[pos] = '-';
				++pos;
			}
			string temp;
			for (int i = 0; i <= idx; ++i){
				temp += (s[idx - i] == '+' ? '-' : '+');
			}
			for (int i = 0; i <= idx; ++i)
				s[i] = temp[i];
			++ans;
		}
		out(ans); el;
	}
	return 0;
}