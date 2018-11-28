#include <bits/stdc++.h>

using namespace std;
typedef long long LL;
typedef pair<int,int> pii;

#define forup(i,a,b) for(int i=(a); i<(b); ++i)
#define fordn(i,a,b) for(int i=(a); i>(b); --i)
#define rep(i,a) for(int i=0; i<(a); ++i)

#define gi(x) scanf("%d",&x)
#define gl(x) scanf("%lld",&x)
#define gd(x) scanf("%lf",&x)
#define gs(x) scanf(" %s",x)

#define fs first
#define sc second

#define pb push_back
#define mp make_pair

const int inf=numeric_limits<int>::max();
const LL linf=numeric_limits<LL>::max();

const int max_n=1005;

int t,n;
int p[max_n];
int a[max_n];

int main() {
	gi(t);
	rep(z,t) {
		printf("Case #%d: ", z+1);
		gi(n);
		rep(i,n) gi(p[i]);
		sort(p,p+n);
		forup(i,1,10) {
			bool ok=false;
			rep(j,i) {
				int mxp=i-j;
				rep(k,n) a[k]=p[k];
				rep(k,j) {
					a[n-1]=max(mxp,a[n-1]-mxp);
					sort(a,a+n);
				}
				if(a[n-1]<=mxp) {
					ok=true;
					break;
				}
			}
			if(ok) {
				printf("%d\n", i);
				break;
			}
		}
	}
	return 0;
}