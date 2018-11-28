#include<cstdio>
#include<algorithm>
#include<cstring>
#include<vector>
#include<queue>
#include<map>
#include<set>
using namespace std;
#define INF (1<<29)
#define min(x,y) (((x)<(y))?(x):(y))
#define max(x,y) (((x)>(y))?(x):(y))
#define FOR(i,x,y) for(int i=(x);i<(y);++i)
#define FOE(i,x,y) for(int i=(x);i<=(y);++i)
#define CLR(i) memset(i,0,sizeof(i))
#define ll long long

int N,T,X,s[10005];
int m;

struct node{
	int a,b;

	bool ok(int l){
		if (b != 0) return 0;
		if (a+l <= X){
			b=l;
			return 1;
		}
		return 0;
	}

} a[10005];

int main(){
	scanf("%d",&T);
	FOE(t,1,T){
		scanf("%d%d",&N,&X);
		FOR(i,0,N) scanf("%d",&s[i]);

		sort(s,s+N);
		m=0; CLR(a);

		for(int i=N-1;i>=0;--i){
			bool flag=1;
			//printf("START: %d\n",s[i]);
			FOR(j,0,m){
				//printf("TRY: %d %d\n",a[j].a,a[j].b);
				if (a[j].ok(s[i])){
					//puts("ok");
					flag = 0;
					break;
				}
			}

			if (flag){
				//puts("open");
				a[m].a = s[i];
				++m;
			}
		}

		printf("Case #%d: %d\n",t,m);
	}
	return 0;
}
