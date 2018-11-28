#include<bits/stdc++.h>
#define scan(n) scanf("%d",&n)
#define scanll(n) scanf("%lld",&n)
#define For(i,a,b) for(i=a;i<b;i++)
#define fill(a,b) memset(a,b,sizeof(a))
#define swap(a,b) a=a+b;b=a-b;a=a-b;
#define ll long long int
#define pb push_back
#define MAX 1000000007
#define f_in(st) freopen(st,"r",stdin);
#define f_out(st) freopen(st,"w",stdout);
using namespace std;
int main()
{
//	f_in("A-large.in");
//	f_out("A-large.out");
	int test;
	scan(test);
	for(int t=1;t<=test;t++)
	{
		ll n;
		cin>>n;
		if(n==0)
		{
			cout<<"Case #"<<t<<": INSOMNIA"<<endl;
		}
		else{
		
			int i=1,flag=1;
			int hash[10];
			fill(hash,0);
			int hashCount = 0;
			while(flag)
			{
				ll a = n*i;
				while(a&&flag)
				{
					int k = a%10;
					a=a/10;
					if(hash[k]==0)
					{
						hashCount++;
						if(hashCount==10)
						{
							flag=0;
						}
						hash[k]++;
					}
				}
				a=n*i;
				i++;
			}
			cout<<"Case #"<<t<<": "<<n*(i-1)<<endl;
	}
}
 	return 0;
}


