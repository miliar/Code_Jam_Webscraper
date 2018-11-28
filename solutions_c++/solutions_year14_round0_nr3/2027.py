#include<iostream>
#include<cstdio>
#include<vector>
#include<queue>
#include<cstring>
#include<algorithm>
using namespace std;

int R,C,K;
char ans[16][16];
char tmp[16][16];
int dx[] = {0,0,1,-1,1,1,-1,-1};
int dy[] = {1,-1,0,0,-1,1,-1,1};

bool valid(int x,int y)
{
	if(x < 0 || y < 0 || x >= R || y >= C)
		return 0;
	return 1;
}

int dfs(int x,int y)
{
	if(!valid(x,y) || tmp[x][y] == '*')
		return 0;
	char t = tmp[x][y];
	tmp[x][y] = '*';
	int cnt = 1;
	if(t == '0')
		for(int i = 0 ; i < 8; i++)
		{
			int nx = x + dx[i];
			int ny = y + dy[i];
			cnt += dfs(nx,ny);
		}
	return cnt;
}

char count(int x,int y)
{
	int res = '0';
	for(int i = 0 ; i < 8; i++)
	{
		int nx = dx[i] + x, ny = y + dy[i];
		if(valid(nx,ny))
			res += ans[nx][ny] == '*';
	}
	return res;
}

bool check()
{
	int cnt = 0;
	for(int i = 0 ; i < R; i++)
		for(int j = 0 ; j < C; j++)
		{
			if(ans[i][j] == '*')
				tmp[i][j] = '*';
			else
				tmp[i][j] = count(i,j),cnt++;
		}

	for(int i = 0 ; i < R; i++)
		for(int j = 0 ; j < C; j++)
			if(tmp[i][j] == '0' || (tmp[i][j] != '*' && cnt == 1))
			{
				ans[i][j] = 'c';
				return dfs(i,j) == cnt;
			}
	return cnt == 1;
}

int main()
{

	freopen("in.in","r",stdin);
	freopen("out.out","w",stdout);
	int TEST = 1,T;
	cin >> T;
	while(T--)
	{
		cerr << TEST << endl;
		cin >> R >> C >> K;
		vector<char> v;
		for(int i = 0 ; i < R*C; i++)
			if(i<K)
				v.push_back('*');
			else
				v.push_back('.');
		bool flag = 0;
		cout << "Case #"<<TEST++<<":" << endl;
		do
		{
			int cnt = 0;
			for(int i = 0 ; i < R; ++i)
				for(int j = 0 ; j < C; ++j)
					ans[i][j] = v[cnt++];
			if(check() && flag == 0)
			{
				for(int i = 0 ; i < R; ++i)
				{
					for(int j = 0 ; j < C; ++j)
						cout << ans[i][j];
					cout << endl;
				}
				flag = 1;
				break;
			}
		}
		while(next_permutation(v.begin(),v.end()));
		if(!flag)
			cout << "Impossible" << endl;
	}
}
