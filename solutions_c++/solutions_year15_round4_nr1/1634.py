#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<cctype>
#include<algorithm>
#include<cstdlib>
#include<string>
#include<ctime>
#include<map>
#include<set>
#include<vector>
#include<list>
#include<stack>
#include<queue>
#include<utility>
using namespace std;
#define ULL unsigned long long
#define LL long long
#define INF 0x3f3f3f3f
#define MAXN 1
#define mod 1000000007
#define rep(i,n) for(int i = 0; i < n; ++i)
#define Rep(i,n) for(int i = 1; i <= n; ++i)

char s[1010][1010];
int row[1010],col[1010];
//int up[1010][1010],down[1010][1010],zuo[1010][1010],you[1010][1010];
bool vis[1010][1010];

int dx[]={0,1,0,-1};
int dy[]={1,0,-1,0};
int r,c,ans;

void dfs(int x0,int y0) {
	vis[x0][y0] = true;
	int d;
	if(s[x0][y0]=='>')d=0;
	else if(s[x0][y0]=='v')d=1;
	else if(s[x0][y0]=='<')d=2;
	else d=3;
	int x = x0 + dx[d], y = y0 + dy[d];
	while(x>0&&x<=r&&y>0&&y<=c&&s[x][y]=='.') x += dx[d], y += dy[d];
	if(x>0&&x<=r&&y>0&&y<=c) {
		if(vis[x][y]) return;
		dfs(x, y);
	}
	else ++ans;
}	

int main()
{
	int t,cas=0;
	cin>>t;
	while(cas++ < t){
		cin>>r>>c;
		Rep(i,r) scanf("%s",s[i]+1);
		memset(row,0,sizeof(row));
		memset(col,0,sizeof(col));
		Rep(i,r){
			Rep(j,c){
				if(s[i][j]!='.')++row[i],++col[j];
			}
		}
		bool ok = true;
		Rep(i,r){
			Rep(j,c){
				if(s[i][j]!='.') ok &= !(row[i]==1&&col[j]==1);
			}
		}
		printf("Case #%d: ", cas);
		if(!ok) {
			puts("IMPOSSIBLE");
			continue;
		}
		memset(vis,0,sizeof(vis));
		ans = 0;
		Rep(i,r) {
			Rep(j,c) if(s[i][j]!='.' && !vis[i][j]){
				dfs(i,j);
			}
		}
		printf("%d\n",ans);
	}
	return 0;
}

