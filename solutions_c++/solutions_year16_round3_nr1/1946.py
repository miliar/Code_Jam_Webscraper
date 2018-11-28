#include<bits/stdc++.h>
#define ll long long
#define mod 1000000007
#define MAX INT_MAX
#define MIN INT_MIN
using namespace std;
int arr[30];

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	
	int test;
	cin>>test;
	for(int t=1;t<=test;t++)
	{
		for(int i=1;i<=26;i++)
		arr[i]=0;
		
		int n;
		cin>>n;
		
		int sum=0;
		for(int i=1;i<=n;i++)
		{
			cin>>arr[i];
			sum+=arr[i];
		}
		
		cout<<"Case #"<<t<<": ";
		
		if(n!=2)
		{
		
		while(sum!=n)
		{
			int max=0;
			int ind=0;
			for(int i=1;i<=n;i++)
			{
				if(arr[i]>max)
				{
					max=arr[i];ind=i;
				}
			}
			arr[ind]--;
			sum--;
			char temp;
			temp=64+ind;
			cout<<temp<<" ";
		}
		
		if(n&1)
		{
			cout<<"A ";
			n--;
			char temp;
			temp=65;
			for(int i=0;i<n;i++)
			{
				temp++;
				cout<<temp;
				i++;
				temp++;
				cout<<temp<<" ";
			}
		}
		else
		{
			char temp;
			temp=64;
			for(int i=0;i<n;i++)
			{
				temp++;
				cout<<temp;
				i++;
				temp++;
				cout<<temp<<" ";
			}
		}
	}
	else
	{
		for(int i=0;i<sum/2;i++)
		cout<<"AB"<<" ";
	}
		cout<<endl;
	}
	
	return 0;
}
