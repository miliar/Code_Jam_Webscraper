#include<stdio.h>
#include<iostream>

using namespace std;

int main()
{
	int n,x,y,same=0,samenum;
	int arr[2][4][4];
	cin>>n;
	for(int i=1;i<=n;i++)
	{
		same = 0;
		samenum = 0;
		cin>>x;
		for(int j=1;j<=16;j++)
		{
			cin>>arr[0][j/4][(j%4)-1];
		}
		
		cin>>y;
		for(int j=1;j<=16;j++)
		{
			cin>>arr[1][j/4][(j%4)-1];
		}

		for(int j=0;j<4;j++)
		{
			for(int k=0;k<4;k++)
			if (arr[0][x-1][j] == arr[1][y-1][k])
			{
				samenum = arr[0][x-1][j];
				same++;
			}
			
		}
				
		if(same == 0)
		{
			cout<<"Case #"<<i<<": "<<"Volunteer cheated!"<<endl;
		}
		else if(same == 1)
		{
			cout<<"Case #"<<i<<": "<<samenum<<endl;
		}
		else
		{
			cout<<"Case #"<<i<<": "<<"Bad magician!"<<endl;
		}
	}
}
