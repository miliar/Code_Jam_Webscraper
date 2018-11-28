#include <iostream>
using namespace std;
typedef long long int ll;
int main() {
	ll t,l,pos,k,c,s,vals,it=0;
	cin>>t;
	for(ll i=1;i<=t;i++)
	{
	    cin>>k>>c>>s;
	    it=0;
	    cout<<"Case #"<<i<<": ";
	    if((k*1.0/c) - (k/c) != 0)
	        vals=(k/c)+1;
	    else
	        vals=k/c;
        if(s<vals)
        {
            cout<<"IMPOSSIBLE"<<endl;
        }
        else
	   {
	   for(l=0;it<vals-1;l=l+c,it++)
	   {
	       pos=l;
	       for(ll r=l+1;r<l+c;r++)
	       {
                pos=(pos*k)+r;	           
	       }
	       cout<<pos+1<<" ";
	   }
	   if(k%c==0)
	   {
	       pos=l;
	       for(ll r=l+1;r<l+c;r++)
	       pos=(pos*k)+r;
	   }
	   else
	   {
	       pos=l;
	       for(ll r=l+1;r<l+(k%c);r++)
	       pos=(pos*k)+r;
	       for(ll r=1;r<c-(k%c);r++)
	       pos=pos*k;
	   }
	
	   cout<<pos+1<<" ";
	   
	     cout<<endl;  
	    }
	}
	return 0;
}