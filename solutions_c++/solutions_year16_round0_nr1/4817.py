#include<iostream>
#include<string.h>
using namespace std;
int a[11];
int f()
{
	long long int i=0;
	while(i<10)
	{
		if(a[i]==1)
		i++;
		else
		break;
	}
	if(i==10)
	return 0;
	else
	return 1;
}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("output.txt","w+",stdout);
	long long int t,count=1,n,p,store=1;
	cin>>t;
	
	while(count<=t)
	{
		memset(a,0,sizeof(a));
		store=1;
		cin>>n;
		if(n==0)
		cout<<"Case #"<<count<<": INSOMNIA"<<endl;
		else
		{
			while(f())
			{
				p=store*n;
				while(p>0)
				{
					a[p%10]=1;
					p=p/10;
				}
		store++;
			}
			cout<<"Case #"<<count<<": "<<(store-1)*n<<endl;
		}
		count++;
	}
}
