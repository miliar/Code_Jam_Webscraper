#include <fstream>
using namespace std;

int main()
{
	fstream infile;
	fstream outfile;
	infile.open("c:\\B-small-attempt0.in",ios::in);
	outfile.open("c:\\B-small-attempt0-out.txt",ios::out|ios::trunc );
	int T;
	infile>>T;
	char lawn[101][101];
	char r[101];
	char c[101];

	for (int t=0;t<T;t++)
	{
		int N,M;
		infile>>N>>M;
		int result=1;
		
		for (int i=0;i<N;i++)
		{
			for (int j=0;j<M;j++)
			{
				infile>>lawn[i][j];
			}
		}
		for (int i=0;i<N;i++)
		{
			r[i]=1;
			for (int j=0;j<M;j++)
			{
				if (lawn[i][j]!='1')
				{
					r[i]=0;
					break;
				}
				
			}

		}

		for (int j=0;j<M;j++)
		{
			c[j]=1;
			for(int i=0;i<N;i++)
			{
				if (lawn[i][j]!='1')
				{
					c[j]=0;
					break;
				}
			}
		}

		for (int i=0;i<N;i++)
		{
			for (int j=0;j<M;j++)
			{
				if (lawn[i][j]=='1')
				{
					if (c[j]==0&&r[i]==0)
					{
						result=0;
						break;
					}
				}
			}
			if (result==0)
			{
				break;
			}
		}
		outfile<<"Case #1: ";
		if (result==0)
		{
			outfile<<"NO";
		}
		else
		{
			outfile<<"YES";
		}
		outfile<<endl;



	}

	infile.close();
	outfile.close();


	return 0;
}

