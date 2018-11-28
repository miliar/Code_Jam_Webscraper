#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <set>
using namespace std;
int test = 1;
const int mov[5][2] = {{0,0},{0,1},{1,0},{0,-1},{-1,0}};
int mapp[102][102];
int r,c;
bool check[102][102];
int res = 0;
set< pair<int,int> > ss;
bool dfs(int x,int y,int movv)
{
	if( x==0 || y==0 || x==r+1 || y==c+1 ) return false;
	if(mapp[x][y]==0&&movv==0) return true;
	if(check[x][y]) return true;
	check[x][y]=true;
	int xx,yy;
	if(mapp[x][y]==0)
	{
		int mm = movv+2;
		if(mm>4) mm%=4;
		bool bb=dfs(x+mov[mm][0],y+mov[mm][1],movv);
		check[x][y] = false;
		return bb;
	}
	else 
	{
		xx = x + mov[ mapp[x][y] ][0];
		yy = y + mov[ mapp[x][y] ][1];
		int mm = mapp[x][y]+2;
		if(mm>4) mm%=4;
		bool bb = dfs(xx,yy,mm);
		if(!bb)
		{
			/*
			if(movv==0)
			{
				if(mapp[x][y]==1) mapp[x][y]=3;
				else if(mapp[x][y]==2) mapp[x][y]=4;
				else if(mapp[x][y]==3) mapp[x][y]=1;
				else if(mapp[x][y]==4) mapp[x][y]=2;
			}
			else mapp[x][y] = movv;
			*/
			ss.insert(set<pair<int,int>>::value_type(make_pair(x,y)));
			check[x][y] = false;
			res++;
			return true;
		}
		else{ check[x][y]=false; return true;}
	}
}
void solve()
{
	cin >> r >> c;
	char temp;
	for( int i = 1 ; i <= r ; i++ )
	{
		for( int j = 1 ; j <= c ; j++ )
		{
			cin >> temp;
			if( temp == '.' ) mapp[i][j] = 0;
			else if( temp == '>' ) mapp[i][j] = 1;
			else if( temp == 'v' ) mapp[i][j] = 2;
			else if( temp == '<' ) mapp[i][j] = 3;
			else mapp[i][j] = 4;
		}
	}

	int cnt = 0;
	for( int i = 1 ; i <= r ; i++ )
	{
		cnt = 0;
		int jj;
		for( int j = 1 ; j <= c ; j++ )
		{
			if( mapp[i][j]!=0 ){ jj=j; cnt++; }
		}
		if(cnt==1)
		{
			int ccnt=0;
			for( int ii = 1 ; ii <= r ; ii++ )
			{
				if( mapp[ii][jj] != 0 ) ccnt++;
			}
			if(ccnt==1)
			{
				printf("Case #%d: IMPOSSIBLE\n",test++);
				return ;
			}
		}
	}

	for( int i = 1 ; i <= r ; i++ )
	{
		for( int j = 1 ; j <= c ; j++ )
		{
			dfs(i,j,0);
		}
	}
	printf("Case #%d: %d\n",test++,ss.size());
	return ;
}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int t;
	cin >> t;
	while(t--){
		ss.clear();
		res = 0;
		memset(mapp,0,sizeof(mapp));
		memset(check,false,sizeof(check));
		solve();
	}
	return 0;
}