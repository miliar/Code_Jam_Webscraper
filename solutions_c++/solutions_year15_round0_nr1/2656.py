#include <bits/stdc++.h>

using namespace std;
typedef long long LL;
typedef pair<int,int> pii;

#define forup(i,a,b) for(int i=(a); i<(b); ++i)
#define fordn(i,a,b) for(int i=(a); i>(b); --i)
#define rep(i,a) for(int i=0; i<(a); ++i)

#define gi(x) scanf("%d ",&x)
#define gl(x) scanf("%lld",&x)
#define gd(x) scanf("%lf",&x)
#define gs(x) scanf(" %s",x)

#define fs first
#define sc second

#define pb push_back
#define mp make_pair

const int inf=numeric_limits<int>::max();
const LL linf=numeric_limits<LL>::max();

int t,n;
string s;

int main() {
	gi(t);
	rep(z,t) {
		printf("Case #%d: ", z+1);
		gi(n); n++;
		cin>>s;
		int ans=0,sum=0;
		rep(i,n) {
			if(s[i]>'0' and sum<i) {
				ans+=i-sum;
				sum=i;
			}
			sum+=s[i]-'0';
		}
		printf("%d\n", ans);
	}
	return 0;
}