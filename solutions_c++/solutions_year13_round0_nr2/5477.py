#include <iostream>
#include <fstream>
using namespace std;

int main()
{
	ifstream infile("B-small-attempt0.in");
	ofstream outfile("outfile.out");
	int count;
	infile>>count;
	int N,M;
	int A[101][101];

	for(int i=0;i<count;i++)
	{
		infile>>M>>N;

		for(int j=0;j<M;j++)
		{
			for(int k=0;k<N;k++)
			{
                infile>>A[j][k];
			}
		}
		bool flag=true;
		for(int m=0;m<M;m++)
		{
			bool r=true,c=true;
			for(int n=0;n<N;n++)
			{
				for(int k=0;k<N;k++)
				{
					if(A[m][k]>A[m][n]) c=false;
				}
				for(int h=0;h<M;h++)
				{
					if(A[h][n]>A[m][n]) r=false;
				}
				if((!c)&&(!r)) {flag=false;break;}
			}
		}
		if(flag) outfile<<"Case #"<<i+1<<": YES"<<endl;
		else outfile<<"Case #"<<i+1<<": NO"<<endl;
	}
    infile.close();
	outfile.close();
}
