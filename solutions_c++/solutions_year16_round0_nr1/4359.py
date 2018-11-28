#include <iostream>
#include <cstring>
#include <cmath>
using namespace std;

void function(int t, int n)
{
	int a[10],i,count,no_of_dig,temp1;
	temp1=n;
	count=0;
	no_of_dig=0;
	memset(a,0,sizeof(a));
	while(temp1!=0)
	{
		//cout<<"#";
		if(a[temp1%10]==0)
		{
			count=count+1;
			a[temp1%10]=1;
		}
		no_of_dig=no_of_dig+1;
		temp1=temp1/10;
	}
	//cout<<no_of_dig<<endl;
	for(i=2*n;i<=(pow(10,(no_of_dig+1))+n);i=i+n)
	{
		//cout<<i<<" ";
		temp1=i;
		while(temp1!=0)
		{
			if(a[temp1%10]==0)
			{
				count=count+1;
				a[temp1%10]=1;
			}
			temp1=temp1/10;
		}
		//cout<<count<<endl;
		if(count==10)
		{
			cout<<"Case #"<<t<<": "<<i<<endl;
			break;
		}
	}
	if(count!=10)
	    cout<<"Case #"<<t<<": INSOMNIA"<<endl;
}

int main()
{
	int j,n,t;
	cin>>t;
	for(j=0;j<t;j++)
	{
		cin>>n;
		if(n==0)
		{
			cout<<"Case #"<<(j+1)<<": INSOMNIA"<<endl;
		}
		else
		{
			function(j+1,n);
	    }
	}
	return 0;
}