#include <fstream>
#define MAXN 100
#define h 2
using namespace std;
int map[MAXN][MAXN];
const int d[4][2]={{0,1},{1,0},{0,-1},{-1,0}};
bool test(int a,int N,int M)
{
	int stack[MAXN*MAXN][2];
	int Flag[MAXN][MAXN];
	int top=-1;
	for(int x=0;x<N;x++)
		for(int y=0;y<M;y++)
		{
			Flag[x][y]=false;
			
		}
	for(int x=0;x<N;x++)
	{
		if(map[x][0]<=a)
		{
			int flag=true;
			//top++;
			//stack[top][0]=x;
			//stack[top][1]=0;
			for(int y=0;y<M;y++)
			{
				if(map[x][y]>a) flag=false;
			}
			if(flag)
			{
				Flag[x][0]=true;
				for(int y=0;y<M;y++)
				{
					Flag[x][y]=true;
				}
			}
		}
		if(map[x][M-1]<=a)
		{
			//top++;
			//stack[top][0]=x;
			//stack[top][1]=M-1;
			int flag=true;
			for(int y=0;y<M;y++)
			{
				if(map[x][y]>a) flag=false;
			}
			if(flag)
			{
				Flag[x][M-1]=true;
				for(int y=M-1;y>=0;y--)
				{
					Flag[x][y]=true;
				}
			}
		}
	}
	for(int y=0;y<M;y++)
	{
		if(map[0][y]<=a)
		{
			//top++;
			//stack[top][0]=0;
			//stack[top][1]=y;
			int flag=true;
			for(int x=0;x<N;x++)
			{
				if(map[x][y]>a) flag=false;
			}
			if(flag)
			{
				Flag[0][y]=true;
				for(int x=0;x<N;x++)
				{
					Flag[x][y]=true;
				}
			}
		}
		if(map[M-1][y]<=a)
		{
			//top++;
			//stack[top][0]=M-1;
			//stack[top][1]=y;
			int flag=true;
			for(int x=0;x<N;x++)
			{
				if(map[x][y]>a) flag=false;
			}
			if(flag)
			{
				Flag[M-1][y]=true;
				for(int x=N-1;x>=0;x--)
				{
					Flag[x][y]=true;
				}
			}
		}
	}
	/*while(top>=0)
	{
		int x=stack[top][0];
		int y=stack[top][1];
		top--;
		for(int i=0;i<4;i++)
		{
			int x1=x+d[i][0];
			int y1=y+d[i][1];
			if(x1>=0 && x1<N && y1>=0 && y1<N)
			{
				if(!Flag[x1][y1])
				{
					Flag[x1][y1]=true;
					top++;
					stack[top][0]=x1;
					stack[top][1]=y1;
				}
			}
		}
	}*/
	for(int x=0;x<N;x++)
		for(int y=0;y<M;y++)
		{
			if(!Flag[x][y] && map[x][y]<=a) return false;
			if(Flag[x][y] && map[x][y]>a) return false;
		}
	return true;
}
int main()
{
	ifstream fin("in.in");
	ofstream fout("out2.out");
	int T;

	fin >> T;
	for(int i=0;i<T;i++)
	{
		int N,M;
		fin >> N >> M;
		for(int x=0;x<N;x++)
			for(int y=0;y<M;y++)
			{
				fin >> map[x][y];
			}
		bool flag=true;
		for(int a=h-1;a>0;a--)
		{
			if(!test(a,N,M))
			{
				flag=false;
				break;
			}
		}
		if(flag) fout << "Case #" << i+1 << ": YES" << endl;
		else fout << "Case #" << i+1 << ": NO" << endl;
	}
	fin.close();
	fout.close();
	return 0;
}