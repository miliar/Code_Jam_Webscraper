	#include<iostream>
	using namespace std;
	int main()
	{
		int test,it=1;
		cin>>test;
		while(test--){
		int row1,row2;
		int grid1[4][4],grid2[4][4];
		cin>>row1;row1--;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			cin>>grid1[i][j];
		}
		cin>>row2;row2--;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			cin>>grid2[i][j];
		}
		int c=0,ans=-1;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			if(grid1[row1][i] == grid2[row2][j])
			{
				c++;
				ans=grid1[row1][i];
			}
		}
		cout<<"Case #"<<it++<<": ";
		if(c==1)	
		cout<<ans<<endl;
		else if(c>1)
		cout<<"Bad magician!"<<endl;
		else
		cout<<"Volunteer cheated!"<<endl;
		}
		return 0;
	}
