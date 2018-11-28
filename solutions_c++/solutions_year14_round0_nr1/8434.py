#include <iostream>
#include <fstream>
using namespace std;
ifstream fin("A-small-attempt1.in");
ofstream fout("A.out");
int main()
{

	int t;
	fin>>t;
	for(int z=1;z<=t;z++)
	{
		int a1,a2,i,j,count=0,ans=0;
		int array1[4][4];
		int array2[4][4];
		fin>>a1;
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
				fin>>array1[i][j];
		}
		fin>>a2;
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
				fin>>array2[i][j];
		}
		
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				if(array1[a1-1][i]==array2[a2-1][j])
				{
					count++;
					ans=array1[a1-1][i];
				}	
			}	
		}
		
		if(count==1)
			fout<<"Case #"<<z<<": "<<ans<<endl;
		else if(count>1)
			fout<<"Case #"<<z<<": Bad magician!"<<endl;
		else if(count<1)
			fout<<"Case #"<<z<<": Volunteer cheated!"<<endl;
		
	}
	return 0;
}
