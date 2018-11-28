#include <fstream>
#include <algorithm>
#include <cmath>
#include <string>
#include <stack>
#include <queue>


using namespace std;
ifstream cin("s.in");
ofstream cout("1.out");

int arr[4][4];
int arr1[4][4];
int arr2[110][2];
int main()
{
	int t=0;
	int n=0,m=0;
	cin>>t;
	for(int i=0;i<t;i++)
	{
		cin>>n;
		for(int j=0;j<4;j++)
			for(int k=0;k<4;k++)
				cin>>arr[j][k];	
		cin>>m;
		for(int j=0;j<4;j++)
			for(int k=0;k<4;k++)
				cin>>arr1[j][k];	
		int c=0,d=0;	
		for(int j=0;j<4;j++)
			for(int k=0;k<4;k++)
				if(arr[n-1][j]==arr1[m-1][k])
				{	
					c++;			
					d=arr[n-1][j];
				}
		arr2[i][0]=c;
		arr2[i][1]=d;
	}			
	for(int i=0;i<t;i++)
	{
		cout<<"Case #"<<i+1<<": ";
		if(arr2[i][0]==0)
			cout<<"Volunteer cheated!";	
		else if(arr2[i][0]==1)
			cout<<arr2[i][1];	
		else
			cout<<"Bad magician!";
		cout<<endl;	
	}
	return 0;
}

