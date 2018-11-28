#include <iostream>

using namespace std;

int main()
{
	int t;
	cin>>t;

	int A[4][4];
	int B[4][4];

	for(int i=1;i<=t;i++)
	{

		int first;
		cin>>first;
		first-=1;

		for(int ctr1=0;ctr1<4;ctr1++)
		{
			for(int ctr2=0;ctr2<4;ctr2++)
			{
				cin>>A[ctr1][ctr2];
			}
		}	


		int second;
		cin>>second;
		second-=1;

		for(int ctr1=0;ctr1<4;ctr1++)
		{
			for(int ctr2=0;ctr2<4;ctr2++)
			{
				cin>>B[ctr1][ctr2];
			}
		}

		int ans=0;

		int answer=0;

		for(int j=0;j<4;j++)
		{
			for(int k=0;k<4;k++)
			{
				if(A[first][j]==B[second][k])
				{
						answer = A[first][j];
						ans++;
				}		
			}	
		}	


	
		if(ans==0)cout<<"Case #"<<i<<": "<<"Volunteer cheated!"<<endl;
		else if(ans==1)cout<<"Case #"<<i<<": "<<answer<<endl;
		else cout<<"Case #"<<i<<": "<<"Bad magician!"<<endl;
	}	
}