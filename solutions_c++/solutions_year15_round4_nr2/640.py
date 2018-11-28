#include <cstdio>
#include <cstring>

using namespace std;
#define rep(i,l,r) for (int i=(l);i<=(r);i++)

typedef double DO;
const DO eps=1e-8;
const int maxn=200;
int n;
DO V,X,R[maxn],C[maxn];

inline DO abs(DO a)
{return a > 0 ? a : -a;}
inline DO max(DO a,DO b)
{if (a > b) return a; return b;}

int main() {
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	int T;scanf("%d\n",&T);
	rep(t,1,T) {
		printf("Case #%d: ",t);
		scanf("%d%lf%lf\n",&n,&V,&X);
		rep(i,1,n) {
			scanf("%lf%lf\n",&R[i],&C[i]);
		}
		if (n==1) {
			if (abs(X-C[1])>eps) {
				puts("IMPOSSIBLE");
				continue;
			}
			else {
				printf("%.9f\n",V/R[1]);
				continue;
			}
		}
		if (n==2) {
			DO t1,t2,ans;
			if (C[1]>C[2]) {
				DO tt;
				tt=C[1];C[1]=C[2];C[2]=tt;
				tt=R[1];R[1]=R[2];R[2]=tt;
			}
			if (X>C[2]+eps || X<C[1]-eps) {
				puts("IMPOSSIBLE");
				continue;
			}
			if (abs(C[1]-C[2])<eps) {
				if (abs(X-C[1])>eps) {
					puts("IMPOSSIBLE");
					continue;
				} else {
					printf("%.9f\n",V/(R[1]+R[2]));
					continue;
				}
			}
			if (abs(C[1]-X)<eps) {
				printf("%.9f\n",V/R[1]);
				continue;
			}
			if (abs(C[2]-X)<eps) {
				printf("%.9f\n",V/R[2]);
				continue;
			}
			t1=V*(X-C[2])/(R[1]*(C[1]-C[2]));
			t2=V*(X-C[1])/(R[2]*(C[2]-C[1]));
			ans=max(t1,t2);
			//if (t1<-eps||t2<-eps) puts("IMPOSSIBLE");
			//else 
				printf("%.9f\n",ans);
			continue;
			//printf("%.8f %.8f\n",t1,t2);
		}
	}
	return 0;
}

