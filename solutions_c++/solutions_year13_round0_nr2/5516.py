#include<fstream>
#include<string>
using namespace std;
int map[10][10];
bool testrow(int N, int M, int r)
{
	//[r]
	for (int j=0;j<M;j++)
	{
		if (map[r][j]==2)//2
		{
			for (int i=0;i<N;i++)
				if (map[i][j]==1)//若2的列出现了1
				{
					for (int k=0;k<M;k++)//i行都必须是1
						if (map[i][k]==2)
						{
							return false;
						}
				}
		}
		else//1
		{
			//一列都是1或者一行都是1
			bool row = true;
			bool col = true;
			for (int i=0;i<N;i++)//一列
			{
				if (map[i][j]==2)
				{
					col = false;
					break;
				}
			}
			if (col)
				continue;
			else//一行
			{
				for (int i=0;i<M;i++)
					if (map[r][i]==2)
					{
						return false;
					}
			}
		}
	}
	return true;
}
bool testcol(int N, int M, int c)
{
	//[][c]
	for (int i=0;i<N;i++)
	//for (int j=0;j<M;j++)
	{
		if (map[i][c]==2)
		//if (map[r][j]==2)//2
		{
			for (int j=0;j<M;j++)
				if (map[i][j]==1)//若2的行出现了1
			//for (int i=0;i<N;i++)
				//if (map[i][j]==1)
				{
					for (int k=0;k<N;k++)
						if (map[k][j]==2)
					//for (int k=0;k<M;k++)//k列都必须是1
						//if (map[i][k]==2)
						{
							return false;
						}
				}
		}
		else//1
		{
			//一列都是1或者一行都是1
			bool row = true;
			bool col = true;
			for (int j=0;j<M;j++)//一hang
			{
				if (map[i][j]==2)
				{
					row = false;
					break;
				}
			}
			if (row)
				continue;
			else//一行
			{
				for (int j=0;j<N;j++)
					if (map[j][c]==2)
				//for (int i=0;i<M;i++)
					//if (map[r][i]==2)
					{
						return false;
					}
			}
		}
	}
	return true;
}
void main()
{
	ifstream _in("in.txt");
	ofstream _out("out.txt");
	if (_in && _out)
	{
		int T;
		_in >> T;
		for (int ii = 0; ii<T; ii++)
		{
			int N, M;
			_in >> N >> M;
			for (int i=0;i<N;i++)
			{
				for (int j=0;j<M;j++)
				{
					_in >> map[i][j];
				}
			}
			bool po1 = testrow(N,M,0);
			bool po2 = testrow(N,M,N-1);	
			bool po3 = testcol(N,M,0);
			bool po4 = testcol(N,M,M-1);
			string st = "";
			if (po1 && po2 && po3 && po4)
				st = "YES";
			else 
				st = "NO";
			_out << "Case #" << ii+1 << ": " << st << endl;
		}
	}
}