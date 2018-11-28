#include <iostream>
#include <vector>
#include <sstream>
#include <algorithm>
#include <numeric>
#include <set>
#include <math.h>
using namespace std;




int board[11][11];
bool b[11][11];

string check(int N,int M)
{
	for(int i=0;i<N;i++)
	{
		for(int j=0;j<M;j++)
		{
			bool greater=false;
			if(!b[i][j])
			{
				for(int k=0;k<N;k++)
				{
					if(board[i][j]<board[k][j])
					{
						greater=true;
						break;
					}
				}
				if(!greater)
				{
					for(int k=0;k<N;k++)
					{
						if(board[i][j]==board[k][j])
						{
							b[k][j]=true;
						}
					}
				}
				else
				{
					greater=false;
					for(int k=0;k<M;k++)
					{
						if(board[i][j]<board[i][k])
						{
							greater=true;				
							break;
						}
					}
					if(!greater)
					{
						for(int k=0;k<M;k++)
						{
							if(board[i][j]==board[i][k])
							{
								b[i][k]=true;
							}
						}
					}
					else
						return "NO";
				}
			}
		}
	}




	return "YES";
}

#define SMALL
//#define LARGE


int main ()
{
//	freopen("a.txt", "rt", stdin);
#ifdef SMALL
	freopen("B-small-attempt0.in","rt",stdin);
	freopen("B-small-attempt0.out","wt",stdout);
#endif
#ifdef LARGE
	freopen("A-large.in","rt",stdin);
	freopen("A-large.out","wt",stdout);
#endif

	int T,N,M;
	cin>>T;
	
	
	for(int c=0;c<T;c++)
	{
		cin>>N>>M;
		memset(b,false,11*11);
		for(int i=0;i<N;i++)
		{
			for(int j=0;j<M;j++)
			{
				cin>>board[i][j];
			}
		}

		printf("Case #%d: ",c+1);
		cout<<check(N,M)<<endl;

	}
		

	
	

	return 0;
}