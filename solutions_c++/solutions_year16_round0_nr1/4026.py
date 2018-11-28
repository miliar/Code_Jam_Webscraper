#include<bits/stdc++.h>
#define f_in(st) freopen(st,"r",stdin);
#define f_out(st) freopen(st,"w",stdout);
using namespace std;
int main()
{
	f_in("large.in");
    f_out("largeout.txt");
	long long n,t,k,d,j=0,i;
	cin>>t;
	while(t--)
	{
		j++;
		cin>>n;
		cout<<"Case #"<<j<<": ";
		d=n;
		long long hash[10]={0};
		int flag=0;
		if(n==0)
		{
			cout<<"INSOMNIA"<<endl;
		}
		else
		{
		while(flag==0)
		{
			k=n;
			while(k)
			{
				hash[k%10]=1;
				k=k/10;
			}
			for(i=0;i<=9;i++)
			{
				if(hash[i]==0)
				{
					break;
				}
			}
			if(i>9)
			{
				flag=1;
			}
			else
			{
				n=n+d;
			}
		}
		 cout<<n<<endl;
	    }
	}
	return 0;
}
