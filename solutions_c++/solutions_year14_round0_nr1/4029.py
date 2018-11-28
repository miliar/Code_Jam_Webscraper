#include<iostream>
using namespace std;

int main()
{
	int arr1[4][4];
	int arr2[4][4];
	int ans1, ans2;
	int resCount, resCard;
	int t;
	cin>>t;
	for(int cases=1;cases <=t; cases++)
	{
		cin>>ans1;
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				cin>>arr1[i][j];
		
		cin>>ans2;
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				cin>>arr2[i][j];
				
		ans1--;
		ans2--;		
		resCount=0;
		
		for(int j=0;j<4;j++)
		{
			int number1 = arr1[ans1][j];
			for(int k=0;k<4;k++)
			{
				int number2 = arr2[ans2][k];
				if(number1 == number2)
				{
					resCount ++;
					resCard = number1;
				}
			}
		}
		
		cout<<"Case #"<<cases<<": ";
		if(resCount == 0)
			cout<<"Volunteer cheated!"<<endl;
		else if(resCount == 1)
			cout<<resCard<<endl;
		else
			cout<<"Bad magician!"<<endl;		
	}
}
