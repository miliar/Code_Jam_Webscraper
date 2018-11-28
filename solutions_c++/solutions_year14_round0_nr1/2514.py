	#include<iostream>
	using namespace std;
	int main()
	{
		int test,it=1;
		cin>>test;
		while(test--){
		int r1,r2;
		int g1[4][4],g2[4][4];
		cin>>r1;r1--;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			cin>>g1[i][j];
		}
		cin>>r2;r2--;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			cin>>g2[i][j];
		}
		int c=0,ans=-1;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			if(g1[r1][i] == g2[r2][j])
			{
				c++;
				ans=g1[r1][i];
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