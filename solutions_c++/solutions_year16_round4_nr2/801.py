#include <bits/stdc++.h>
using namespace std;
typedef double lf;
typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;
typedef pair<ll, int> pli;
typedef pair<int, ll> pil;
typedef pair<ll, ll> pll;
#define pb push_back
#define SZ(x) ((int)(x).size())
inline int ri() {
	int x=0, f=1, c=getchar();
	for(; c<48||c>57; f=c=='-'?-1:f, c=getchar());
	for(; c>47&&c<58; x=x*10+c-48, c=getchar());
	return x*f;
}
const int N=205;
lf p[N], d[N];
int main() {
	for(int _=1, T=ri(); _<=T; ++_) {
		printf("Case #%d: ", _);
		int n=ri(), k=ri();
		for(int i=0; i<n; ++i) {
			scanf("%lf", &p[i]);
		}
		lf ans=0;
		for(int s=0; s<1<<n; ++s) {
			int cnt=0;
			for(int i=0; i<n; ++i) {
				if(s>>i&1) {
					++cnt;
				}
			}
			if(cnt==k) {
				memset(d, 0, sizeof d);
				d[0]=1;
				cnt=0;
				for(int i=0; i<n; ++i) {
					if(s>>i&1) {
						++cnt;
						for(int j=cnt; j>=0; --j) {
							d[j]=d[j-1]*p[i]+d[j]*(1-p[i]);
						}
					}
				}
				ans=max(ans, d[k>>1]);
			}
		}
		printf("%.10f\n", ans);
	}
	return 0;
}
