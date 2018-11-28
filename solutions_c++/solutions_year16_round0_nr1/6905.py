#include<bits/stdc++.h>
using namespace std;
int check(int arr[])
{
	int flag=0;
	for(int i=0;i<10;++i)
	if(arr[i]==0)
	{
		flag=1;
		break;
	}
	if(flag==1)
		return 1;
	else
		return 0;
}
int main(void)
{
	freopen("out.txt","w",stdout);
	freopen("in.txt","r",stdin);
	int t;
	cin>>t;
	int c=1;
	while(t--)
	{
		long long original;
		cout<<"Case #"<<c++<<": ";
		int arr[10]={0};
		long long int n;
		cin>>n;
		original=n;
		if(n==0)
		{
			cout<<"INSOMNIA\n";
			continue;
		}
		
		while(check(arr))
		{
			long long temp=n;
			while(temp)
			{
				arr[temp%10]=1;	
				temp=temp/10;				
			}
			n+=original;													
		}
		cout<<n-original<<endl;		
	}
	return 0;
}
