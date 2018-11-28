#include <cstdio>
#include <cstring>
#include <string>
using namespace std;
#define REP(i,n) for(int i=0;i<(n);i++)

int nextint()
{
	int t;
	scanf("%d",&t);
	return t;
}

int n,m;
int field[202][202];
int used[202][202];
int result[202][202];
int dx[4]={1,-1,0,0};
int dy[4]={0,0,1,-1};

int dfs(int i, int j, int h)
{
	if(used[i][j]) return 0;
	used[i][j]=1;
	int res=1;
	REP(k,4)
	{
		int nx, ny;
		nx=i+dx[k];
		ny=j+dy[k];
		if(0<=nx&&nx<n&&0<=ny&&ny<m && field[nx][ny]<=h)
			res+=dfs(nx,ny,h);
	}
	return res;
}

int main()
{
	int t;
	t=nextint();
	for(int test=1;test<=t;test++)
	{
		memset(field,0,sizeof(field));
		string res="YES";
		n=nextint();
		m=nextint();
		REP(i,n) REP(j,m)
			field[i+1][j+1]=nextint();
		n+=2;
		m+=2;
		REP(i,n) REP(j,m) result[i][j]=100;
/*		for(int i=1;i<100;i++)
		{
			memset(used,0,sizeof(used));
			int cnt=0;
			REP(j,n) REP(k,m) if(field[j][k]<=i) cnt++;
			if(dfs(0,0,i)!=cnt)
				res="NO";
		}*/
		REP(i,n)
		{
			int maxv=0;
			REP(j,m)
				maxv=max(maxv,field[i][j]);
			REP(j,m)
				result[i][j]=min(result[i][j],maxv);
		}
		REP(j,m)
		{
			int maxv=0;
			REP(i,n)
				maxv=max(maxv,field[i][j]);
			REP(i,n)
				result[i][j]=min(result[i][j],maxv);
		}
		REP(i,n) REP(j,m)
			if(result[i][j]!=field[i][j])
				res="NO";
		printf("Case #%d: %s\n",test,res.c_str());
	}
	return 0;
}
