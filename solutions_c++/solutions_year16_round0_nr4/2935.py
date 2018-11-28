#include <bits/stdc++.h>
#define ll long long int 
using namespace std;

int main() {
	// your code goes here
	ll t,t1,i,c,k,s;
	cin>>t;
	t1=0;
	while(t--)
	{
	    cin>>k>>c>>s;
	    t1++;
	    cout<<"Case #"<<t1<<":";
	    for(i=1;i<=s;i++)
	    {
	        cout<<" "<<i;
	    }
	    cout<<"\n";
	}
	return 0;
}
