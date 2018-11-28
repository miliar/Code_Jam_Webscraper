#include<iostream>
#include<fstream>
#include<string>

using namespace std;

int main()
{
	ifstream infile;
	infile.open("input.txt"); //the input file name here
	ofstream ofile;
	ofile.open("answer.txt");
	int t;
	infile>>t;

	int grid1[5][5];
	int grid2[5][5];  //first choice
	int r1,r2,x;

	

	for(int i=1;i<t+1;i++)
	{
		
		infile>>r1;
		for(int j=1;j<5;j++)
		{
			for(int k=1;k<5;k++)
				infile>>grid1[j][k];		
		}

		infile>>r2;
		for(int j=1;j<5;j++)
		{
			for(int k=1;k<5;k++)
				infile>>grid2[j][k];		
		}

		for(int j=1;j<5;j++)
		{
			for(int k=1;k<5;k++)
				cout<< grid1[j][k]<<" ";
			cout<<endl;
		}

		bool bad=false,cheated=true;

		for(int j=1;j<5;j++)
		{
			for(int k=1;k<5;k++)
			{
				if(grid1[r1][j]==grid2[r2][k] && cheated==true)
				{
						cheated=false;
						x=grid1[r1][j];
				}
				else if(grid1[r1][j]==grid2[r2][k] && cheated==false)
				{
						bad=true;
						break;
				}

			}
		
		}

		ofile<<"Case #"<<i<<": ";

		if(bad==false &&cheated==false)
			ofile<<x<<endl;
		else if(bad==true)
			ofile<<"Bad magician!"<<endl;
		else if(cheated==true)
			ofile<<"Volunteer cheated!"<<endl;
		
	}


cout<<"7alawa";
system("pause");

	return 0;
}

