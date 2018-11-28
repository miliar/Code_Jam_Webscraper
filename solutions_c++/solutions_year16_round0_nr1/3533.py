#include <bits/stdc++.h>
#define ll long long int 
using namespace std;

int main() {
	// your code goes here
	ll t,n,n1,n2,d,c,cnt,t1;
	ll a[10],i;
	cin>>t;
	t1=0;
	while(t--)
	{
	    cin>>n;
	    t1++;
	    cout<<"Case #"<<t1<<": ";
	    if(n==0)
	    {
	        cout<<"INSOMNIA\n";
	        continue;
	    }
	    c=0;
	    for(i=0;i<=9;i++)
	    a[i]=0;
	    cnt=1;
	    while(1)
	    {
	    n1=cnt*n;
	    n2=n1;
	    while(n1!=0)
	    {
	        d=n1%10;
	        if(a[d]==0)
	        {
	            c++;
	            a[d]=1;
	        }
	        n1=n1/10;
	    }
	    if(c>=10)
	    {
	        break;
	    }
	    cnt++;
	    }
	    cout<<n2<<'\n';
	}
	return 0;
}
