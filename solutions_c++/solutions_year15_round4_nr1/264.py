#include<stdio.h>
#include<stdlib.h>
#include<algorithm>
#include<math.h>
#include<string.h>
#include<map>
#include<vector>
#include<set>
using namespace std;
#define RI(x) scanf("%d",&(x))
#define RII(x,y) scanf("%d %d",&(x),&(y))
#define RI64(x) scanf("%I64d",&(x))
#define RII64(x,y) scanf("%I64d%I64d",&(x),&(y))
#define RILL(x) scanf("%lld",&(x))
#define RIILL(x,y) scanf("%lld%lld",&(x),&(y))
#define FZ(i,n) for(int i=0;i<(n);i++)
#define PA(a,n) FZ(_1,n)printf("%d%c",(a)[_1],_1==(n)-1?10:32)
#define ePA(a,n) FZ(_2,n)fprintf(stderr,"%d%c",(a)[_2],_2==(n)-1?10:32)
#define SZ(x) ((int)x.size())
#define ALL(x) (x).begin(),(x).end()
#define pritnf printf
#define N 111
#define ID(x,y) ((x)*m+(y))
using namespace std;
typedef long long int lnt;
typedef double dou;
int n,m;
char mp[N][N];
int dx[4]={ 0, 0,+1,-1};
int dy[4]={+1,-1, 0, 0};
int isout(int x,int y){
	return x<0||x>=n||y<0||y>=m;
}
int mmp(char k){
	if(k=='^')return 3;
	if(k=='v')return 2;
	if(k=='>')return 0;
	return 1;
}
vector<int>e[N*N];
int bad[N][N];
int sol(int uuu){
	RII(n,m);
	FZ(i,n)scanf("%s",mp[i]);
	int ans=0;
	FZ(i,n)FZ(j,m)if(mp[i][j]!='.'){
		bad[i][j]=0;
		FZ(k,4){
			int nx=i+dx[k];
			int ny=j+dy[k];
			for(;isout(nx,ny)==0&&mp[nx][ny]=='.';){
				nx+=dx[k];
				ny+=dy[k];
			}
			if(isout(nx,ny)==0){
				e[ID(i,j)].push_back(ID(nx,ny));
			}
			if(k==mmp(mp[i][j])){
				if(isout(nx,ny)){
					bad[i][j]=1;
				}
			}
		}
		if(bad[i][j]){
			if(SZ(e[ID(i,j)])==0){
				return -1;
			}
			ans++;
		}
		e[ID(i,j)].clear();
	}
	return ans;
}
int main(){
	freopen("A-large.in","r",stdin);
	freopen("PA_l.txt","w",stdout);
	//while(RI(n)!=EOF)sol();
	int t;
	if(RI(t)!=EOF){
		for(int ti=1;ti<=t;ti++){
			int res=sol(ti);
			printf("Case #%d: ",ti);
			if(res==-1)puts("IMPOSSIBLE");
			else printf("%d\n",res);
		}
	}
	return 0;
}

