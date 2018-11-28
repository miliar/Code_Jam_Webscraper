#include <iostream>
#include <algorithm>
#include <vector>
#include <cstring>
using namespace std;
int b,m;
bool su;
bool cy;
int mat[8][8];
int cnt = 0;
bool check[8];
void dfs(int t)
{
	if(cnt>m) return;
	if(cy) return;
	check[t] = true;
	if(t==b)
	{
		cnt++;
		check[t] = false;
		return;
	}
	for( int i = 1 ; i <= b ; i++ )
	{
		if(mat[t][i]>0&&check[i]==false)
		{
			dfs(i);
		}
		else if(mat[t][i]>0&&check[i]==true)
		{
			cy = true;
			return;
		}
	}
	check[t] = false;
	return;
}
void process(int x,int y)
{
	if(x==b&&y==b)
	{
		memset(check,false,sizeof(check));
		cnt = 0;
		cy = false;
		dfs(1);
		if(cnt==m && cy==false) su = true;
		return;
	}
	if(su) return;
	if(x!=b&&y!=1&&x!=y&&mat[y][x]!=1)
	{
		mat[x][y] = 1;
		if(x+1>b) process(1,y+1);
		else process(x+1,y);
		if(su) return;
		mat[x][y] = 0;
	}
	if(su) return;
	if(x+1>b) process(1,y+1);
	else process(x+1,y);
	return;
}
void solve()
{
	su = false;
	memset(mat,0,sizeof(mat));
	cin >> b >> m;
	process(1,1);
	if(su)
	{
		cout << "POSSIBLE" << endl;
		for( int i = 1 ; i <= b ; i++ )
		{
			for( int j = 1 ; j <= b ; j++ )
			{
				cout << mat[i][j];
			}
			cout << endl;
		}
	}
	else cout << "IMPOSSIBLE" << endl;
	return;
}
int main()
{
	freopen("B-small-attempt0.in","r",stdin);
	freopen("B-small-attempt0.out","w",stdout);
	int t; cin>>t;
	for( int i = 1 ; i <= t ; i++ )
	{
		printf("Case #%d: ",i);
		solve();
	}
	return 0;
}