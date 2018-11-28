#include<iostream>
#include<fstream>
#include<vector>
using namespace std;
int mines(int i,int j,int n,int m,vector<vector<char> >&board)
{
	int ans=0;
	if(i!=n)
	{
		ans+=(board[i+1][j]=='*');
		if(j!=1)
			ans+=(board[i+1][j-1]=='*');    //bug
		if(j!=m)
			ans+=(board[i+1][j+1]=='*');
	}
	if(j!=1)
		ans+=(board[i][j-1]=='*');
	if(j!=m)
		ans+=(board[i][j+1]=='*');
	if(i!=1)
	{
		ans+=(board[i-1][j]=='*');
		if(j!=1)
			ans+=(board[i-1][j-1]=='*');
		if(j!=m)
			ans+=(board[i-1][j+1]=='*');
	}
	return ans;
}


void fill(int x,int y,int &n,int &m,vector<vector<char> >&board,vector<vector<bool> >&flag,int &count)
{
	
	if(flag[x][y]||board[x][y]=='*')return;
	flag[x][y]=true;
	count++;
	if(mines(x,y,n,m,board)!=0)return;
	if(x!=n)
	{
		fill(x+1,y,n,m,board,flag,count);
		if(y!=1)
			fill(x+1,y-1,n,m,board,flag,count);
		if(y!=m)
			fill(x+1,y+1,n,m,board,flag,count);
	}
	if(x!=1)
	{
     	fill(x-1,y,n,m,board,flag,count);
		if(y!=1)
			fill(x-1,y-1,n,m,board,flag,count);
		if(y!=m)
			fill(x-1,y+1,n,m,board,flag,count);
	}
	if(y!=m)
		fill(x,y+1,n,m,board,flag,count);
	if(y!=1)
		fill(x,y-1,n,m,board,flag,count);
}
bool test(int n,int m,int num,vector<vector<char> >&board)
{
	vector<vector<bool> >flag(n+1,vector<bool>(m+1,false));
	int count=0;
	fill(n,m,n,m,board,flag,count);
	if(count==n*m-num)
		return true;
	return false;
}
void dfs(int x,int y,int n,int m,int k,vector<vector<char> >&board,bool &flag,int num)
{
	if(x==n&&y==m&&k!=0)return;
	if(flag)return;
	if(k==0)
	{
		if(test(n,m,num,board))
			flag=true;
		return;
	}
	if(flag)return;
	board[x][y]='*';
	int xx=x,yy=y;
	if(yy==m)
	{
		yy=1;
		xx++;
	}
	else
		yy++;
	if(flag)return;
	dfs(xx,yy,n,m,k-1,board,flag,num);
	if(flag)return;
	board[x][y]='.';
	dfs(xx,yy,n,m,k,board,flag,num);
}
int main()
{
int T,n,m,x,v=0;
	ifstream fin("in.txt");
	ofstream fout("out3_2.txt");
	fin>>T;
	while(T--)
	{
		fin>>n>>m>>x;
		int total=n*m;
		int i=1,j=1,di=0,dj=1,k=x;
		bool flag=false;
		vector<vector<char> >board(n+1,vector<char>(m+1,'.'));
		dfs(1,1,n,m,k,board,flag,x);
		fout<<"Case #"<<++v<<":"<<endl;
		cout<<"Case #"<<v<<":"<<endl;
		if(flag){
			for(i=1;i<=n;i++)
			{
				for(j=1;j<=m;j++)
				{
					if(i==n&&j==m)
					{
						fout<<"c";
						cout<<"c";
					}
					else
					{
						fout<<board[i][j];
						cout<<board[i][j];
					}
				}
				fout<<endl;
				cout<<endl;
			}

		}
		else
		{
			fout<<"Impossible"<<endl;
			cout<<"Impossible"<<endl;
		}
	}
	return 0;
}
