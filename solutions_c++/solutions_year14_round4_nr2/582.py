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

int N,T,a[1005];

int main(){
	scanf("%d",&T);
	FOE(t,1,T){
		scanf("%d",&N);
		FOR(i,0,N) scanf("%d",&a[i]);

		int st=0,ed=N-1;
		int ans=0;
		FOR(i,0,N-1){
			int tar=-1;
			FOE(j,st,ed){
				if (tar == -1) tar = j;
				else if (a[j] < a[tar]) tar = j;
			}

			int d1 = tar - st, d2 = ed - tar;
			if (d1 < d2){
				for(int j=tar;j>=st+1;--j) a[j] = a[j-1];
				++st;
				ans+=d1;
			}
			else{
				for(int j=tar;j<=ed-1;++j) a[j] = a[j+1];
				--ed;
				ans+=d2;
			}
		}

		printf("Case #%d: %d\n",t,ans);
	}
	return 0;
}
