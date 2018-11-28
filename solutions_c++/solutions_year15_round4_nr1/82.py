#include<bits/stdc++.h>
#define int64 long long
#define sqr(x) (x)*(x)
#define mk make_pair
#define pb push_back
#define fi first
#define se second
#define rep(i,x,y) for(int i=(x);i<=(y);++i)
#define VI vector<int>
#define VI64 vector<int64>
#define VS vector<string>
#define PII pair<int,int>
#define PDD pair<double,double>
#define VPII vector< PII >
#define SZ(x) ((int)(x).size())
#define N 120
using namespace std;
const double pi=acos(-1);
int T,tim,n,m,hang[N],lie[N];
char c[N][N];
int main(){
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	for(scanf("%d",&T);T--;){
		scanf("%d%d",&n,&m);
		rep(i,1,n)scanf("%s",c[i]+1);
		memset(hang,0,sizeof(hang));
		memset(lie,0,sizeof(lie));
		int ans=0;
		rep(i,1,n)
			rep(j,1,m)if(c[i][j]!='.'){
				int x=i,y=j,flag=0;
				hang[i]++;
				lie[j]++;
				for(;;){
					if(c[i][j]=='^')x--;
					if(c[i][j]=='<')y--;
					if(c[i][j]=='>')y++;
					if(c[i][j]=='v')x++;
					if(x<1 || x>n || y<1 || y>m)break;
					if(c[x][y]!='.'){
						flag=1;
						break;
					}
				}
				ans+=1-flag;
			}
		rep(i,1,n)
			rep(j,1,m)if(hang[i]==1 && lie[j]==1 && c[i][j]!='.'){
				printf("Case #%d: IMPOSSIBLE\n",++tim);
				goto fail;
			}
		printf("Case #%d: %d\n",++tim,ans);
		fail:;
	}
}
