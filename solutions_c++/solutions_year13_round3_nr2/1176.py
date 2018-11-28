#include <iostream>
#include <algorithm>
#include <vector>
#include <fstream>
#include <map>
#include <queue>
using namespace std;

map <pair<int,int> , string> M;
int X, Y;

int dx[] = {0,0,1,-1};
int dy[] = {1,-1,0,0};
char d[] = {'N','S','E','W'};

bool valid(int x, int y)
{
	return M.count(make_pair(x,y)) == 0;
}

string BFS(){
	M[make_pair(0,0)] = "";
	queue < pair<int,int> > Q;
	Q.push(make_pair(0,0));
	int lvl = 0;
	while(!Q.empty())
	{

		int sz = Q.size();
		lvl ++;
		while(sz --)
		{
			int x = Q.front().first, y = Q.front().second;
			Q.pop();
			string str = M[make_pair(x,y)];
			if(x == X && y == Y)
				return str;
			for(int i=0; i<4; i++)
			{
				if(valid(x+(dx[i]*lvl),y+(dy[i]*lvl)))
				{
					string tmp = str; tmp += d[i];
					M[make_pair(x+(dx[i]*lvl),y+(dy[i]*lvl))] = tmp;
					Q.push(make_pair(x+(dx[i]*lvl),y+(dy[i]*lvl)));
				}
			}
		}
	}
	return "";
}

int main()
{

	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);

	int T;
	cin >> T;

	for(int t=1; t<=T; t++)
	{
		M.clear();
		cin >> X >> Y;
		cout << "Case #" << t << ": ";
		cout << BFS() << endl;
	}

	return 0;
}
