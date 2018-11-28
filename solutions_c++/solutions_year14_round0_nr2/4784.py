#include<cstdio>
#include<algorithm>
#include<cstring>
#include<vector>
#include<queue>
#include<map>
#include<set>
using namespace std;
#define eps (1e-8)
#define INF (1<<29)
#define min(x,y) (((x)<(y))?(x):(y))
#define max(x,y) (((x)>(y))?(x):(y))
#define FOR(i,x,y) for(int i=(x);i<(y);++i)
#define FOE(i,x,y) for(int i=(x);i<=(y);++i)
#define CLR(i) memset(i,0,sizeof(i))
#define ll long long
#define flt(x,y) ((y-x) > eps)
#define feq(x,y) (fabs(x-y) < eps)

int t;
double c,f,x;

int main(){
	scanf("%d",&t);
	FOE(T,1,t){
		scanf("%lf%lf%lf",&c,&f,&x);

		double ans = x/2.0,r=2.0,tb=0.0;
		while (1){
			tb += c/r;
			r += f;

			double tmp = tb + x/r;

			if (flt(tmp,ans)) ans=tmp; else break;
		}
		printf("Case #%d: %.8lf\n",T,ans+eps);
	}
	return 0;
}
