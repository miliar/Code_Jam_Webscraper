#include <iostream>
#include <vector>
#include <deque>
using namespace std;
struct cell
{
public:
	int x,y;
	cell(int x,int y):x(x),y(y){}
};
bool Permute(vector<vector<char>> &board, int R,int C, int M,int mines,int r=0,int c=0)
{
	if(c==C)
	{
		return Permute(board, R,C,M,mines,r+1,0);
	}
	if(r==R)
	{
		int empty;
		
		for(int i=0;i<R;i++)
		{
			for(int j=0;j<C;j++)
			{
				if(board[i][j] == '*')
				{
					continue;
				}
				empty=0;
				vector<vector<bool> > visited(R,vector<bool>(C,false));
				deque<cell> que;
				que.push_back(cell(i,j));
				while(!que.empty())
				{
					cell c=que.front();
					que.pop_front();
					if(visited[c.x][c.y]) 
						continue;

					visited[c.x][c.y]=true;
					empty++;
					bool flag=false;
					for(int m=max(0,c.x-1);m<=min(R-1,c.x+1);m++)
					{
						for(int n=max(0,c.y-1);n<=min(C-1,c.y+1);n++)
						{
							if(board[m][n]=='*')
							{
								flag=true;
								goto leave;
							}
						}
					}
leave:
					if(flag) continue;

					for(int m=max(0,c.x-1);m<=min(R-1,c.x+1);m++)
					{
						for(int n=max(0,c.y-1);n<=min(C-1,c.y+1);n++)
						{
							if(!visited[m][n])
							{
								que.push_back(cell(m,n));
							}
						}
					}
				}
				if(empty==R*C-mines)
				{
					board[i][j]='c';
					return true;
				}
			}
		}
		return false;
	}
	if(M>0){
		board[r][c]='*';
		if(Permute(board, R,C,M-1,mines,r,c+1))
		{
			return true;
		}
	}	
	if(M<(R-r)*(C-c))
	{
		board[r][c]='.';
		return Permute(board, R,C,M,mines,r,c+1);
	}	
	else
		return false;

}
int main()
{
	int T;
	cin>>T;
	for(int t=1;t<=T;t++)
	{
		int C,R,M;
		cin>>R>>C>>M;
		vector<vector<char>> board(R,vector<char>(C,'.'));
		bool found = Permute(board,R,C,M,M);
		cout<<"Case #"<<t<<": "<<endl;
		if(!found)
		{
			cout<<"Impossible"<<endl;
		}
		else
		{
			for(int i=0;i<R;i++)
			{
				for(int j=0;j<C;j++)
				{
					cout<<board[i][j];
				}
				cout<<endl;
			}
		}
	}
	return 0;
}