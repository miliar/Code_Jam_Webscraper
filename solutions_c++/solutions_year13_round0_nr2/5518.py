#include<iostream>
#include<string>
#include<fstream>
#include<math.h>
#include<vector>


using namespace std;



int main()
{
	ifstream inpFile;
	inpFile.open("input.txt");
	ofstream outFile;
	outFile.open("output.txt");
	int T;
	inpFile>>T;

	for(int i=0; i<T; i++)
	{
		int n,m;
		inpFile>>n>>m;
		if(n==1 || m==1)
		{
			outFile<<"Case #"<<i+1<<": YES"<<endl;

			int foo;
			for(int j=0; j<n; j++)
			{
				for(int k=0; k<m; k++)
				{
					inpFile>>foo;
				}
			}

			continue;
		}
		int grid[10][10];
		for(int j=0; j<n; j++)
		{
			for(int k=0; k<m; k++)
			{
				inpFile>>grid[j][k];
			}
		}

		bool flag = false;
		for(int j=0; j<n; j++)
		{
			for(int k=0; k<m; k++)
			{
				flag = false;
				if(grid[j][k]==1)
				{
					//check if it belongs to a horizontal line
					for(int t=0; t<m; t++)
					{
						if(grid[j][t]!=1)
						{
							flag = true;
							break;
						}
					}
					if(flag)
					{
						//check if it is belongs to a vertical line
						for(int t=0; t<n; t++)
						{
							if(grid[t][k]!=1)
							{
								outFile<<"Case #"<<i+1<<": NO"<<endl;
								flag = true;
								break;
							}
							if(t==n-1)
								flag = false;
						}
					}
				}
				if(flag)break;
			}
			if(flag)break;
			if(j == n-1)
				outFile<<"Case #"<<i+1<<": YES"<<endl;
		}	
	}
}