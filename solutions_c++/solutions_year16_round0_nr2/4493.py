#include <bits/stdc++.h>
using namespace std;

int main() {
	long long int t,j;
	cin>>t;
	
	
	for(j=1;j<=t;j++)
	{
	    char s[101];
	    cin>>s;
	    long long int x,ans=0,z,i;
	    x=strlen(s);
	    for(i=0;i<x;i++)
	    {
	        z=i;
	        if(s[i]=='-')
	        {   i++;
	           while(s[i]=='-')
	           {
	               i++;
	           }
	           i--;
	           ans+=2;
	        }
	        if(z==0 && s[0]=='-')
	        ans-=1;
	        
	        z=-1;
	    }
	    
	    
	    cout<<"Case #"<<j<<": "<<ans<<endl;
	    
	}
}

