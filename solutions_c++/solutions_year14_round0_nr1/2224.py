#include<iostream>
#include<fstream>

using namespace std;

int main()
{

	ifstream fin;
	fin.open("A-small-attempt0.in");
	
	ofstream fout;
	fout.open("output.txt");
	

	short int t;
	short int ans1;
	short int ans2;
	
	short int array1[4][4];
	short int array2[4][4];
	

	fin>>t;
	
	for(int i=0;i<t;i++)
	{
		fin>>ans1;
		
		for(int j=0;j<4;j++)
			for(int k=0;k<4;k++)
				fin>>array1[j][k];
				
		
		fin>>ans2;
		
		for(int j=0;j<4;j++)
			for(int k=0;k<4;k++)
				fin>>array2[j][k];
		
		
		
		ans1--;
		ans2--;
		
		short int counter =0;
		short int value;
		
		for(int j=0;j<4;j++)
			for(int k=0;k<4;k++)
			{
				if(array1[ans1][j]==array2[ans2][k])
				{
					counter++;
					value = array1[ans1][j];
				}
			}
		
		
		
		fout<<"Case #"<<i+1<<": ";
		
		if(counter==0)
		{
			fout<<"Volunteer cheated!";
		}	
		
		else if (counter>1)
		{
			fout<<"Bad magician!";
		}
		
		else
			fout<<value;
			
			
		fout<<endl;
	}
	
	
	
	
	
	
	fin.close();
	
}
