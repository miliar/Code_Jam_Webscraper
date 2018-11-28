#include<bits/stdc++.h>
typedef long long int ll;
using namespace std;
int xx=1;
int main()
{
	int t;
	cin>>t;
	while(t--)
	{
		ll n;
		cin>>n;
		if(n==0)
		{
		cout<<"Case #"<<xx<<":"<<" "<<"INSOMNIA"<<endl;
		xx++;
		}else
		{
		
		    ll i;
		    int a[10];
		    for(i=0;i<10;i++)
		    a[i]=0;
		    int count;
		    ll x=1;
		    ll p;
		    p=n;
		    count=10;
		    while(count>0)
		    {
			
			    n=(x)*p;
			    while(n>0)
			    {
				    int b=n%10;
			    	n=n/10;
			    	a[b]++;
			    }
			    count=0;
			    for(i=0;i<10;i++)
			    {
				    if(a[i]==0)
				    count++;
			    }
			    if(count!=0)
			    x++;
		    }
		    n=x*p;
		    cout<<"Case #"<<xx<<":"<<" "<<n<<endl;
            xx++;
		    
		}
	}
	return 0;
}
