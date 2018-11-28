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

int t,x,r,c;

int main() {
	gi(t);
	rep(z,t) {
		printf("Case #%d: ", z+1);
		gi(x); gi(r); gi(c);
		if(c>r) swap(r,c);
		if(x==1) printf("GABRIEL\n");
		else if(x==2) {
			if(r%2==0 or c%2==0) printf("GABRIEL\n");
			else printf("RICHARD\n");
		}
		else if(x==3) {
			if(r<3 or c<2) printf("RICHARD\n");
			else if((r*c)%x==0) printf("GABRIEL\n");
			else printf("RICHARD\n");
		}
		else {
			if(r<4 or c<3) printf("RICHARD\n");
			else printf("GABRIEL\n");
		}
	}
	return 0;
}