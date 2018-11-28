#include <bits/stdc++.h>
using namespace std;
#define ll long long
int main() 
{
	int test=1,test0;
	cin>>test0;
	while(test0--)
	{
		cout<<"Case #"<<test++<<": ";
		ll n,j,f=1;
		cin>>n;
		if(n==0){cout<<"INSOMNIA"<<endl;continue;}
		int h[12]={0};
		for(j=n;f==1;j+=n)
		{
			f=0;
			ll p=j;
			while(p)
			{
				h[p%10]=1;p/=10;
			}
			for(int k=0;k<=9;k++)if(h[k]==0){f=1;break;};
		}
		cout<<j-n<<endl;
	}
	return 0;
}