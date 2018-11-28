#include<iostream>
#include<stdio.h>
using namespace std;


int main()
{
	int grid[4][4],grid1[4][4];
	int row1[4];
	int row1ID,row2ID;
	int t;
	freopen("A-small-attempt1.in","r+",stdin);
	freopen("A-small-attempt1.out","w+",stdout);
	cin>>t;
	
	for(int i=0;i<t;i++)
	{
		cin>>row1ID;
		row1ID--;
		for(int j=0;j<4;j++)
			for(int k=0;k<4;k++)
				cin>>grid[j][k];

		for(int j=0;j<4;j++)
			row1[j]=grid[row1ID][j];

		cin>>row2ID;		
		row2ID--;
		for(int j=0;j<4;j++)
			for(int k=0;k<4;k++)
				cin>>grid1[j][k];

		int counter=0;
		int value=0;
			


		for(int j=0;j<4;j++)
			for(int k=0;k<4;k++)
				if(grid1[row2ID][j]==row1[k])
				{
					counter++;
					value=row1[k];
				}
		
		int comp=0;

		if(counter >1 || counter == 0)
		{
			for(int j=0;j<4;j++)
				for(int k=0;k<4;k++)
					if(grid1[j][k]!=grid[j][k])
					{
						comp=1;
						break;
					}

			if(comp!=1 && (row1ID == row2ID))
			{
				cout<<"Case #"<<i+1<<": Bad magician!"<<endl;
			}
			else if(comp!=1 && (row1ID != row2ID))
			{
				cout<<"Case #"<<i+1<<": Volunteer cheated!"<<endl;
			}
			else
			{
				int flag=0;
				for(int x=0;x<4;x++)
				{
					for(int y=0;y<4;y++)
					{
						if(grid[row1ID][x] == grid1[row2ID][y])
						{
							flag=1;
							break;
						}
					}
				}
				if(flag) cout<<"Case #"<<i+1<<": Bad magician!"<<endl;
				else cout<<"Case #"<<i+1<<": Volunteer cheated!"<<endl;
						
				//cout<<"Case #"<<i+1<<": Bad magician!"<<endl;
				//cout<<"i am here"<<endl;
			}
			
		}		


		if(counter==1)
			cout<<"Case #"<<i+1<<": "<<value<<endl;
	
		

	} //end for testcase
	
	return 0;

} //end main

