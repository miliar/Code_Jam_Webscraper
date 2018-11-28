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
#define N 10
using namespace std;
const double pi=acos(-1);
const int d[4][2]={0,1, 0,-1, 1,0, -1,0};
int a[N][N],ans,n,m,T,tim,Ans[120][N][N];
bool work(){
	for(;;){
		bool flag=0;
		rep(i,1,n)
			rep(j,1,m)if(a[i][j]){
				int n1=0,n2=0;
				rep(k,0,3){
					int x=i+d[k][0],y=j+d[k][1];
					if(x<1 || x>n)continue;
					if(y>m)y=1;
					if(y==0)y=m;
					if(!a[x][y])n1++;
					if(a[x][y]==a[i][j])n2++;
				}
				if(a[i][j]<n2 || a[i][j]>n2+n1)return 0;
				if(a[i][j]==n1+n2){
					rep(k,0,3){
						int x=i+d[k][0],y=j+d[k][1];
						if(x<1 || x>n)continue;
						if(y>m)y=1;
						if(y==0)y=m;
						if(!a[x][y])a[x][y]=a[i][j],flag=1;
					}
				}
			}
		if(!flag)return 1;
	}
}
void dfs(){
	int b[N][N];
	memcpy(b,a,sizeof(b));
	bool flag=0;
	rep(i,1,n)
		rep(j,1,m)if(!a[i][j]){
			flag=1;
			rep(k,1,3){
				a[i][j]=k;
				if(work()){
					dfs();
				}
				memcpy(a,b,sizeof(b));
			}
			return;
		}
	if(!flag){
		ans++;
	/*	rep(i,1,n){
			rep(j,1,m)printf("%d ",a[i][j]);
			puts("");
		}
		puts("");*/
		memcpy(Ans[ans],a,sizeof(a));
	}
}
int main(){
	freopen("D.in","r",stdin);
	freopen("D.out","w",stdout);
	for(scanf("%d",&T);T--;){
		scanf("%d%d",&n,&m);
		memset(a,0,sizeof(a));
		ans=0;
		dfs();
		int p=0;
		rep(i,1,ans){
			bool flag=0;
			rep(j,1,i-1){
				rep(k,0,m-1){
					bool can=1;
					rep(x,1,n)
						rep(y,1,m)if(Ans[i][x][y]!=Ans[j][x][(y+k-1)%m+1])can=0;
					if(can)flag=1;
				}
			}
			if(!flag)p++;
		}
			
			
		printf("Case #%d: %d\n",++tim,p);
	}
}

