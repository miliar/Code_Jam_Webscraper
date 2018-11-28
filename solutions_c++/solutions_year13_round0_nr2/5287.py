// Lawnmower.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <fstream>
using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	fstream infile;
	fstream outfile;
	infile.open("c:\\B-large.in",ios::in);
	outfile.open("c:\\B-large-out.txt",ios::out|ios::trunc );
	int T;
	infile>>T;
	int lawn[111][111];
	char r[111];
	char c[111];

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
		for (int l=99;l>0;l--)
		{
			for (int i=0;i<N;i++)
			{
				r[i]=1;
				for (int j=0;j<M;j++)
				{
					if (lawn[i][j]>l)
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
					if (lawn[i][j]>l)
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
					if (lawn[i][j]==l)
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
			if (result==0)
			{
				break;
			}

		}
		

		outfile<<"Case #"<<t+1<<": ";
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

