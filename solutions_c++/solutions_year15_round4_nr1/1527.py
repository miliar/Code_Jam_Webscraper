#include <iostream>
using namespace std;

struct Pos
{
	int x, y;
	Pos() {x = -1; y = -1;}
	Pos (int _x, int _y)
	{
		x = _x;
		y = _y;
	}
};

int n, m;
string s[128];
int arrows[128][128];

int dx[] = {+1, -1,  0,  0};
int dy[] = { 0,  0, +1, -1};
int dirs[300];

int used[128][128];
int res;

bool isOut(Pos pos)
{
	return pos.x < 0 || pos.x >= n || pos.y < 0 || pos.y >=m;
}

Pos getNext(int dir, Pos pos)
{
	Pos ret = pos;
	do
	{
		ret = Pos(ret.x + dx[dir], ret.y + dy[dir]);
	}
	while(!isOut(ret) && arrows[ret.x][ret.y] == -1);
	return ret;
}

int dfs(Pos pos, Pos last)
{
	//cout << pos.x << " " << pos.y << endl; getchar();
	Pos next = getNext(arrows[pos.x][pos.y], pos);
	//cout << "->" << next.x << " " << next.y << endl;
	if(isOut(next))
	{
		if(isOut(last))
		{
			// first move
			for(int i = 0; i < 4; i ++)
			{
				arrows[pos.x][pos.y] = i;
				next = getNext(arrows[pos.x][pos.y], pos);
				if(!isOut(next))
				{
					break;
				}
			}

			if(isOut(next))
			{
				return 0;
			}
			res ++;

		}
		else
		{
			used[pos.x][pos.y] = 1;
			res ++;
			return 1;
		}
	}

	used[pos.x][pos.y] = 1;

	if (used[next.x][next.y])
	{
		return 1;
	}

	return dfs(next, pos);

}

void solve()
{
	dirs['>'] = 2;
	dirs['<'] = 3;
	dirs['.'] = -1;
	dirs['^'] = 1;
	dirs['v'] = 0;
	res = 0;
	memset(used, 0, sizeof(used));

	scanf ("%d%d", &n, &m);

	int i, j;

	for(i = 0; i < n; i++)
	{
		//scanf("%s", s);
		//cout << s << endl;
		cin>>  s[i];
		//cout << s[i]<< endl;
		for(j = 0; j < m; j++)
		{
			arrows[i][j] = dirs[s[i][j]];
		}
	}
	//cout << "pass1" << endl;
	for(i = 0; i < n; i++)
		for(j = 0; j < m; j++)
		{
			//cout <<"dfs" << endl;
			if (arrows[i][j] == -1)
			{
				continue;	
			}
			if(used[i][j])
			{
				continue;
			}
			if(!dfs(Pos(i, j), Pos(-1, -1)))
			{
				printf("IMPOSSIBLE\n");
				return;
			}
		}

		printf("%d\n", res);
		//cout << "adass" << endl;
}


int main ()
{
	int t;
	scanf("%d", &t);

	for(int i = 1; i<=t; i++)
	{
		printf("Case #%d: ", i);
		solve();
	}
	return 0;
}