#include <iostream>
#include <stdio.h>
#include <fstream>

int main()
{	
	int ch;
	std::ifstream file("A-small-attempt0.in");
	std::ofstream file2("output.txt");
	int t=0, a[5][5], b[5][5], num,temp=0;
	int row1, row2;

		int count=0;
		
		
		file>>t;
		std::cout<<t;
		for(int i=1;i<=t;i++)
		{
		
		file>>row1;
		for(int j=1;j<5;j++)
			for(int k=1;k<5;k++)
				{file>>a[j][k];
				}
		file>>row2;
		for(int j=1;j<5;j++)
			for(int k=1;k<5;k++)
				{file>>b[j][k];
				}
		for(int j=1;j<5;j++)
		{	
			temp=b[row2][j];
			for(int k=1;k<5;k++)
			{
				if(temp==a[row1][k])
				{
					count++;
					num=temp;
					break;
				}
			}

		}
		if(count==1)
			file2<<"Case #"<<i<<": "<<num<<"\n";
		else if(count>1)
			file2<<"Case #"<<i<<": Bad magician!\n";
		else if(count==0)
			file2<<"Case #"<<i<<": Volunteer cheated!\n";
		count=0;
		}

	
}

