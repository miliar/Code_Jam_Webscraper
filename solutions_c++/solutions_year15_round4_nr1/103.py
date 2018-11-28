#include<cstdio>
#include<algorithm>
#include<cstring>
#include<iostream>
#include<cstdlib>
#include<cmath>
#include<vector>
#include<map>
#include<set>
#include<queue>
#include<bitset>
using namespace std;
typedef long long ll;
typedef double db;
const db pi=acos(-1);
void gn(int &x){
	int sg=1;char c;while(((c=getchar())<'0'||c>'9')&&c!='-');
	if(c=='-')sg=-1,x=0;else x=c-'0';
	while((c=getchar())>='0'&&c<='9')x=x*10+c-'0';
	x*=sg;
}
void gn(ll &x){
	int sg=1;char c;while(((c=getchar())<'0'||c>'9')&&c!='-');
	if(c=='-')sg=-1,x=0;else x=c-'0';
	while((c=getchar())>='0'&&c<='9')x=x*10+c-'0';
	x*=sg;
}
const int mo=1000000007;
int qp(int a,ll b){int ans=1;do{if(b&1)ans=1ll*ans*a%mo;a=1ll*a*a%mo;}while(b>>=1);return ans;}
int n,m;

char a[111][111];
int cr[111],cc[111];
int ned[111][111];
int dx[4]={1,0,-1,0};
int dy[4]={0,1,0,-1};
char ch[4]={'v','>','^','<'};
int main()
{
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	int tes;scanf("%d",&tes);
	for (int tt=1;tt<=tes;tt++){
		scanf("%d%d",&n,&m);
		printf("Case #%d: ",tt);
		for (int i=1;i<=n;i++)scanf("%s",a[i]+1);
		memset(cr,0,sizeof(cr));
		memset(cc,0,sizeof(cc));
		memset(ned,0,sizeof(ned));
		for (int i=1;i<=n;i++)
			for (int j=1;j<=m;j++)if(a[i][j]!='.')cr[i]++,cc[j]++;
		int bo=1;
		for (int i=1;i<=n && bo;i++)
			for (int j=1;j<=m && bo;j++)if(a[i][j]!='.' && cr[i]==1 && cc[j]==1){
				printf("IMPOSSIBLE\n");
				bo=0;
			}
		if(!bo)continue;
		int cnt=0;
		for (int i=1;i<=n;i++)
			for (int j=1;j<=m;j++)if(a[i][j]!='.'){
				int k=0;
				for (int jj=0;jj<4;jj++)if(a[i][j]==ch[jj]){k=jj;break;}
				int bo=0;
				for (int x=i+dx[k],y=j+dy[k];x>=1 && x<=n && y>=1 && y<=m;x+=dx[k],y+=dy[k]){
					if(a[x][y]!='.'){
						bo=1;
						break;
					}
				}
				if(!bo)cnt++;
			}
		printf("%d\n",cnt);
	}
	return 0;
}


