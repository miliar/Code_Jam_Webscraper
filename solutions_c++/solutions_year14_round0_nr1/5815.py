// codejam1.cpp : Defines the entry point for the console application.
//


#include <iostream>
#include <math.h>
#include <stdlib.h>
#include <fstream> 

using namespace std;
int main()
{
	std::ofstream ofs ("out.txt", std::ofstream::out);

	int t;
	cin>>t;
	for(int q=1;q<=t;q++)
	{
		int mat1[4][4],mat2[4][4];
		int c1,c2;
		cin>>c1;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				cin>>mat1[i][j];
			}
		}
		cin>>c2;

		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				cin>>mat2[i][j];
			}
		}

		c1--;
		c2--;

		int ans = 0;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				if(mat1[c1][i] == mat2[c2][j])
				{
					if(ans == 0)
						ans = mat1[c1][i];
					else
						ans = -1;
				}
			}
		}
		if(ans==0)
			ofs<<"Case #"<<q<<": Volunteer cheated!\n";
		else if(ans==-1)
			ofs<<"Case #"<<q<<": Bad magician!\n";
		else
			ofs<<"Case #"<<q<<": "<<ans<<endl;
	}
	ofs.close();
	return 0;
}
