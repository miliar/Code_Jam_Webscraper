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

int main(){
	freopen("ip.in", "r", stdin);
	freopen("op.out", "w", stdout);
	int t;
	in(t);
	int cs = 1;
	while (t--){
		int n;
		in(n);
		printf("Case #%d: ", cs++);
		if (n == 0){
			puts("INSOMNIA"); continue;
		}	
		bool d[10]; Fill(d, 0);
		int num = n;
		bool done = true;
		int mx = 10000000;
		while (mx--){
			int number = num;
			while (number){
				d[number % 10] = true;
				number /= 10;
			}
			done = true;
			for (int i = 0; i < 10; ++i){
				if (!d[i]){
					done = false; break;
				}
			}
			if (done)break;
			num += n;
		}
		if (done){
			out(num); el;
		}
		else puts("INSOMNIA");
	}
	return 0;
}