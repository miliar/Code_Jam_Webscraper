#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;
int countdigits(ll n,int arr[],int count)
{
	int d;
	while(n>0)
	{
		d=n%10;
		if(arr[d]==0)
		{
			arr[d]=1;
			count++;
		}
		n=n/10;
	}
	return count;
}
int main()
{
	ios::sync_with_stdio(0);;
	int t;
	cin>>t;
	for(int c=1;c<=t;c++)
	{
		ll n;int count=0;
		cin>>n;
		int arr[10];
		memset(arr,0,sizeof(arr));
		int i=1;int flag=0;ll temp;
		while(i<100)
		{
			temp=(ll)n*i;
			count=countdigits(temp,arr,count);
			if(count==10)
			{
				flag=1;
				break;
			}
			i++;
		}
		if(flag)
		{
			cout<<"Case #"<<c<<": "<<temp<<endl;
		}
		else
			cout<<"Case #"<<c<<": INSOMNIA"<<endl;
	}
	return 0;
}