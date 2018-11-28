#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <iostream>
#include <algorithm>
const int dx[9]={0,1,1,0,-1,-1,-1,0,1};
const int dy[9]={0,0,1,1,1,0,-1,-1,-1};
using namespace std;
struct sta{
	int x,y;
}st[200000];
int n,m,c,flag,v[50][50],B[50][50],b[50][50];
int pd(int x,int y)
{
	int sum=0;
	for (int i=1;i<=8;i++) {
		int nx=x+dx[i],ny=y+dy[i];
		if (nx<1 || nx>n || ny<1 || ny>m) continue;
		sum+=v[nx][ny];
	}
	return sum;
}
bool check()
{
	int s=0,t=0;
	for (int i=1;i<=n;i++)
		for (int j=1;j<=m;j++) {
			B[i][j]=0;
			if (!v[i][j]) {
				b[i][j]=pd(i,j);
				if (!b[i][j]) s=i,t=j;
			}
		}
	if (!s && !t) 
		return n*m-c==1;
	int h,r;
	h=r=0;
	st[r=1].x=s,st[r=1].y=t;
	B[s][t]=1;
	for (;h<r;) {
		sta ne=st[++h];
		if (b[ne.x][ne.y]) continue;
		for (int i=1;i<=8;i++) {
			sta na;
			na.x=ne.x+dx[i],na.y=ne.y+dy[i];
			if (na.x<1 || na.x>n || na.y<1 || na.y>m) continue;
			if (v[na.x][na.y]) continue;
			if (B[na.x][na.y]) continue;
			st[++r]=na,B[na.x][na.y]=1;
		}
	}
	return n*m-c==r;
}
void getout()
{
	int s=0,t=0;
	for (int i=1;i<=n;i++)
		for (int j=1;j<=m;j++)
			if (!b[i][j] && !v[i][j]) s=i,t=j;
	for (int i=1;i<=n;i++) {
		for (int j=1;j<=m;j++) {
			if (v[i][j]) printf("*");
			else if (s==i && t==j) printf("c");
			else if (!s && !t) {
				printf("c");
			}
			else printf(".");
		}
		printf("\n");
	}
}
void dfs(int x,int y,int c)
{
	//cout<<x<<' '<<y<<' '<<c<<endl;
	if (!c) {
		if (check()) {
			getout();
			flag=1;
		}
		return ;
	}
	if (m-y+1+(n-x)*m<c) return ;
	v[x][y]=1;
	if (y!=m) dfs(x,y+1,c-1);
	else dfs(x+1,1,c-1);
	if (flag) return ;
	v[x][y]=0;
	if (y!=m) dfs(x,y+1,c);
	else dfs(x+1,1,c);
}
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T;
	cin>>T;
	for (int Case=1;T;T--,Case++) {
		printf("Case #%d:\n",Case);
		scanf("%d%d%d",&n,&m,&c);
		for (int i=1;i<=n;i++)
			for (int j=1;j<=m;j++) v[i][j]=0;
		flag=0;
		if (n*m>=c) dfs(1,1,c);
		if (!flag) {
			printf("Impossible\n");
		}
	}
	return 0;
} 
