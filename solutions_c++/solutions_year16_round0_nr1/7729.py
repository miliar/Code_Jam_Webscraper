#include <iostream>
using namespace std;

int main() {
	long long int t,n,caseno=0;
	cin>>t;
	while(t--)
	{
		int num[10]={0};
		int flag=1;
		caseno++;
		cin>>n;
		long long int temp,i=2;
		if(n==0)
		{
			cout<<"Case #"<<caseno<<": "<<"INSOMNIA"<<endl;
			continue;
		}
		long long int temp2=n;
		while(1)
		{
			temp=temp2;
			
			int flag1=0,x;
		while(temp!=0)
		{
			x=temp%10;
			num[x]=1;
		    temp=temp/10;
		}
		for(long long int j=0;j<10;j++)
		{
			if(num[j]==0)
			{
				flag1=1;
				break;
			}
		}
		if(flag1==0)
		{
			break;
		}
		temp2=n*i;
		i++;
		}
	 cout<<"Case #"<<caseno<<": "<<temp2<<endl;
	}
	return 0;
}