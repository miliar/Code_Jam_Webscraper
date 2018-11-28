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

int t,n;
double a[1005],b[1005];
bool fa[1005],fb[1005];

int main(){
	scanf("%d",&t);
	FOE(T,1,t){
		int y=0,z=0;

		scanf("%d",&n);
		FOR(i,0,n) scanf("%lf",&a[i]);
		FOR(i,0,n) scanf("%lf",&b[i]);

		sort(a,a+n); sort(b,b+n);

		//War
		CLR(fa); CLR(fb);
		FOR(i,0,n){
			int tar = -1;
			FOR(j,0,n){
				if (fb[j]) continue;

				if (tar == -1) tar = j;
				if (flt(a[i],b[j])){tar=j; break;}
			}

			fb[tar]=1;
			if (flt(b[tar],a[i])) ++z;
		}

		//D War
		CLR(fa); CLR(fb);
		FOR(i,0,n){
			int tar=-1,hi;
			FOR(j,0,n){
				if (fb[j]) continue;
				
				if (tar==-1) tar=j;
				hi=j;
			}

			if (flt(b[tar],a[i])) fb[tar]=1,++y;
			else fb[hi]=1;
		}

		printf("Case #%d: %d %d\n",T,y,z);
	}
	return 0;
}
