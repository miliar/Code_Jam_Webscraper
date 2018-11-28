#include <iostream>
#define ll long long int
using namespace std;

int main() {
	ll t,n,k,c,s;
	cin>>t;
	for(ll i=1;i<=t;i++)
	{
	    cin>>k>>c>>s;
	    cout<<"Case #"<<i<<": ";
        if(s<k-1)
        {
            cout<<"IMPOSSIBLE"<<endl;
            continue;
        }
	    if(c==1 || k==1)
	    {
	        if(s<k)
	        {
	            cout<<"IMPOSSIBLE"<<endl;
	            continue;
	        }
	        for(ll x=1;x<=k;x++)
	            cout<<x<<" ";
	        cout<<endl;
	    }
	    else
	    {
	        for(ll x=2;x<=k;x++)
	            cout<<x<<" ";
	        cout<<endl;
	    }
	}
	
	return 0;
}

