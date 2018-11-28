#include <string.h>       
#include <vector>       
#include <set>       
#include <map>       
#include <algorithm>       
#include <math.h>       
#include <sstream>       
#include <ctype.h>       
#include <queue>       
#include <stack>       
#include <iostream> 
#include <gmp.h>	// if GMP is not allowed, I apologize
#include <fstream>
using namespace std;


int main(int argc, char** argv)
{


string fName = argv[1];
fstream In((fName+".in").c_str(), ios::in);
fstream Out((fName + ".out").c_str(), ios::out);

int tests;

In >> tests;

int N, M;

int dx[8] = {-1, -1, -1, 0, 0, 1, 1,1};
int dy[8] = {-1, 0, 1, -1, 1, -1, 0,1};

for(int h=0; h<tests; h++)
{
	int R, C, M, temp;
	In >> R >> C >> M;
	Out << "Case #" << h+1 << ": " << endl;
	vector<string> board(R, string(C, '.'));
	vector<int> list(R*C, '.');
	for(int i=0; i<M; i++)
		list[i] = '*';
	int flag = 0;

	do
	{
		for(int i=0; i<R; i++)
			for(int j=0; j<C; j++)
				board[i][j] = list[i*C+j];
		//for(int i=0; i<R; i++)
		//	cout << board[i] << endl;
		for(int i=0; i<R && !flag; i++)
		for(int j=0; j<C && !flag; j++)
			if(board[i][j]=='.')
			{	//cout << i << " " << j << endl;
				queue<pair<int, int> > q;
				vector<vector<int> > visited(R, vector<int>(C, 0));
				int vc = 1;
				visited[i][j] = 1;
				q.push(make_pair(i, j));
				while(!q.empty() )
				{
					pair<int, int> p = q.front();
					q.pop();
					int x = p.first, y = p.second;
					int k;
					for(k=0; k<8; k++)
						if(x+dx[k] > -1 && x + dx[k] < R && y+dy[k] > -1 && y+dy[k] < C && board[x+dx[k]][y+dy[k]] != '.')
							break;
					if(k==8)
					{
						for(k=0; k<8; k++)
						if(x+dx[k] > -1 && x + dx[k] < R && y+dy[k] > -1 && y+dy[k] < C && visited[x+dx[k]][y+dy[k]]==0)
						{
							visited[x+dx[k]][y+dy[k]] = 1;
							vc++;
							q.push(make_pair(x+dx[k], y+dy[k]));
						}
					}
				}
				if(vc+M==R*C)
				{
					board[i][j] = 'c';
					flag = 1;
				}
			}
		if(flag)
			break;

	}
	while(next_permutation(list.begin(), list.end() ));

	if(flag)
		for(int i=0; i<R; i++)
			Out << board[i] << endl;
	else
		Out << "Impossible" << endl;

}

In.close();

Out.close();

return 0;

}
 
