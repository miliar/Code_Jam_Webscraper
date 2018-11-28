#include <bits/stdc++.h>
using namespace std;

int main() {
	long long int t,j;
	cin>>t;
	
	
	for(j=1;j<=t;j++)
	{
	    long long int k,c,s,z,i;
	    cin>>k>>c>>s;
	    z=pow(k,c)/k;
	    cout<<"Case #"<<j<<": ";
	    for(i=0;i<pow(k,c);i++)
	    {
	        if(i*z>=pow(k,c))
	        break;
	        
	        cout<<(i*z)+1<<" ";
	        
	    }
	    cout<<endl;
	}
}

