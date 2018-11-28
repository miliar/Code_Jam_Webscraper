#include<iostream>
using namespace std;
int main()
{
	int t;
	cin>>t;
	int a,b,arr[4][4],arr1[4][4];
	for(int k=1;k<=t;k++)
	{
		cin>>a;
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				cin>>arr[i][j];
		cin>>b;
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				cin>>arr1[i][j];
	int count=0,card;
	for(int i=0;i<4;i++)
		for(int j=0;j<4;j++)
			{if(arr[a-1][i]==arr1[b-1][j]){count++;card=arr[a-1][i];}}

	cout<<"Case #"<<k<<": ";
	if(count==1)cout<<card<<endl;
	else if(count>1)cout<<"Bad magician!"<<endl;
	else cout<<"Volunteer cheated!"<<endl;

	}
	return 0;
}