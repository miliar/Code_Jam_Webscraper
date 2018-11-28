//#include <cstdio>
#include <iostream>
#include <fstream>
using namespace std;

void main()
{
	int M,N,C;
	int **lawn;
	ifstream fin("B-large.in",ios_base::in);
	ofstream fout("B-large.out",ios_base::out);
	fin>>C;
	for(int c=0;c<C;c++)
	{
		fin>>M;
		fin>>N;
		lawn=(int **)malloc(M*sizeof(int *));
		for (int m=0;m<M;m++)
		{
			lawn[m]=(int *)malloc(N*sizeof(int));
			for (int k=0;k<N;k++)
			{
				fin>>lawn[m][k];
			}
		}
		bool possible=true;
		for (int m=0;m<M;m++)
		{
			for (int n=0;n<N;n++)
			{
				for (int i=0;i<M;i++)
				{
					if(lawn[i][n]>lawn[m][n])
					{
						for (int j=0;j<N;j++)
						{
							if(lawn[m][j]>lawn[m][n])
							{
								possible=false;
								goto print;
							}
						}
					}
				}
			}
		}
print:
		fout<<"Case #"<<c+1<<": "<<(possible ? "YES" : "NO")<<endl;
	}
	fin.close();
	fout.close();
	//getchar();
}