#include<iostream>
#define MAX 100000
#include<algorithm>
using namespace std;
//-----------------------------------------

int main()
{
	//freopen("D-large.in","r",stdin);
	//freopen("game.txt","w",stdout);
	int t;
	cin>>t;
	for(int test=1;test<=t;test++)
	{
		int n;
		cin>>n;
		int arr1[n+1],arr2[n+1];
		double temp;
		int check[n+1];
		
		for(int i=0;i<n;i++)
		{
			cin>>temp;
			temp*=MAX;
			arr1[i]=temp;
			check[i]=-1;
		}
		
		for(int i=0;i<n;i++)
		{
			cin>>temp;
			temp*=MAX;
			arr2[i]=temp;
		}
		
		sort(arr1,arr1+n);
		sort(arr2,arr2+n);
		
		int count=0;
		for(int i=0;i<n;i++)
		{
			for(int j=0;j<n;j++)
			{
				if(arr2[i] < arr1[j] && check[j]==-1)
				{
					check[j]=0;
					count++;
					break;
				}
			}
		}
		cout<<"Case #"<<test<<": ";
		cout<<count<<" ";
		for(int i=0;i<n;++i)
			check[i]=-1;
		count=0;
		for(int i=0;i<n;i++)
		{
			for(int j=0;j<n;j++)
			{
				if(arr2[j] > arr1[i] && check[j]==-1)
				{
					check[j]=0;
					count++;
					break;
				}
			}
		}
		cout<<n-count<<endl;
	}
}
