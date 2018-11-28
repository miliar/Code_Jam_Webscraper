#include<bits/stdc++.h>
#define ll long long int
using namespace std;
int main()
{
	freopen("abc.in", "r", stdin); 
 freopen("jam2_output.in", "w", stdout);
	int t,t1=1;
	cin>>t;
	while(t--)
	{
		ll x,n,i,c,j,p,y;
		int counter=1;
		bool flag=0,flag1=0;
		cin>>n;
		x=n;
		bool b[10]={0};
		if(n==0)
		cout<<"Case #"<<t1<<": "<<"INSOMNIA"<<endl;
		else
		{
		while(flag!=1)
		{
			if(n>=10000000000000000)
			{
				flag1=1;
				break;
			}
			p=0;
			y=n;
			while(n!=0)
			{
				c=n%10;
				b[c]=1;
				n/=10;
			}
			for(j=0;j<10;j++)
			{
				if(b[j]==1)
				p++;
				else
				break;
			}
			if(p==10)
			{
				flag=1;
				break;
			}
			else
			{
				counter++;
				n=x*counter;
			}
		}
		if(flag1==0)
		cout<<"Case #"<<t1<<": "<<y<<endl;
		else
		cout<<"Case #"<<t1<<": "<<"INSOMNIA"<<endl;
	}
	t1++;
	}
	return 0;
}
