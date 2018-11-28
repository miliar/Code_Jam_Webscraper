#include <bits/stdc++.h>
#define ll long long 
#define m 1000000007
using namespace std;

int main() {
	// your code goes here
	ll t,n,f=0,k,x,l,g,b,y=1,i,hash[10],pre;
	std::ios::sync_with_stdio(false);
	for(i=0;i<10;i++)
	hash[i]=0;
	cin>>t;
   while(t--)
{f=0;
	for(i=0;i<10;i++)
	hash[i]=0;
    cin>>n;
    if(n==0)
    f=1;
    else
    {
    	k=1;
    	x=n;
    while(1)
    {
    	pre=x;
    	while(x>0)
    	{l=0;
    	g=0;
    	
    		b=x%10;
    		hash[b]=1;
    		x=x/10;
    	}
    	for(i=0;i<10;i++)
    		{
    			if(hash[i]==0)
    			{
    				g=1;
    				break;
    			}
    			
    		}
    	if(g!=1)
    	break;
    		x=n*(k+1);
    		k++;
    	  
      }
    }
    if(f==1)
    cout<<"Case "<<"#"<<y<<": "<<"INSOMNIA"<<endl;
    else
     cout<<"Case "<<"#"<<y<<": "<<pre<<endl;
     y++;

}


	
	return 0;
}
