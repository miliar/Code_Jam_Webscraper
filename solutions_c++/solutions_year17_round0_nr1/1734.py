#include<bits/stdc++.h>
using namespace std;
typedef long long int ll;
typedef vector<int> vi;
typedef vector<char> vc;
typedef pair<int, int> pi;
const int mod = 1e9 + 7;
const double EPS = 1e-9;
const int INF = 1 << 29;
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

int cnt[1003];

int main(){
	freopen("ip.in", "r", stdin);
	freopen("op.out", "w", stdout);
	int t; in(t);
	for (int cs = 1; cs <= t; ++cs){
		string s; cin >> s;
		int k; in(k);
		Fill(cnt, 0);
		int n = s.length();
		for (int i = 0; i + k - 1 < n; ++i){
			cnt[i] = (i ? cnt[i - 1] : 0);
			int ptr = i - k;
			int num = cnt[i] - (ptr >= 0 ? cnt[ptr] : 0);
			char c = s[i];
			if (num & 1){
				c = (c == '+' ? '-' : '+');
			}
			cnt[i] += (c == '-');
		}
		printf("Case #%d: ", cs);
		int ans = cnt[n - k];
		for (int i = n - k + 1; i < n; ++i){
			cnt[i] = cnt[i - 1];
			int ptr = i - k;
			int num = cnt[i] - (ptr >= 0 ? cnt[ptr] : 0);
			char c = s[i];
			if (num & 1){
				c = (c == '+' ? '-' : '+');
			}
			if (c == '-'){
				puts("IMPOSSIBLE"); ans = -1; break;
			}
		}
		if (ans != -1){out(ans); el;}
	}
	return 0;
}