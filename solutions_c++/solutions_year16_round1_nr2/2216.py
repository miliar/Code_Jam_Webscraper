#include<iostream>
using namespace std;

int main()
{
	int k,z;
	cin>>z;
for(k=0;k<z;k++) 
{

	int n;
	int hei[2500]={0};
	cin>>n;
	int arr[2*n-1][n];
	for(int i=0;i<2*n-1;i++)
	{
		for(int j=0;j<n;j++)
		{
			cin>>arr[i][j];
		}
	}

	for(int i=0;i<2*n-1;i++)
	{
		for(int j=0;j<n;j++)
		{
			hei[arr[i][j]]++;
		}
	}

	cout<<"Case #"<<k+1<<": ";
	for(int i=0;i<2500;i++)
	{
		if(hei[i]%2==1)
			cout<<i<<" ";
	}

	cout<<'\n';
}

}