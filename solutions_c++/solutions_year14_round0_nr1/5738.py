#include <iostream>
using namespace std;

int main() {
	int n,j;
	int arr[305][305];
	int a[100000][2];
	int b[100000][2];
	int i,q;
	cin>>n;
	for(i=1;i<=n;i++)
	{
		for(j=1;j<=n;j++)
		{
			cin>>arr[i][j];
		}
	}
	cin>>q;
	for(i=0;i<q;i++)
	{
		cin>>a[i][0];
		cin>>a[i][1];
			cin>>b[i][0];
		cin>>b[i][1];
		
	}
	

	for(i=0;i<q;i++)
	{
		int start=1;
		for(i=a[i][0];i<=b[i][0];i++)
		{
			
			for(j=a[i][0];j<=n;j++)
			{
				if((i==a[i][0]) && (j<a[i][1]))
				{
					continue;
				}
				if((i==b[i][0]) && (j==b[i][1]))
				{
					break;
				}
				cout<<arr[i][j]<<"\n";
						
			}
		}
	}
	
	return 0;
}