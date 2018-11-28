#include <bits/stdc++.h>
using namespace std;
 
int main()
{	
	int t,x,l,r,i=1;
	cin>>t;
	while(t--)
	{
		cin>>x>>l>>r;
		int cnt=1;
            if( x>=7 || r*l<x || (l*r)%x!=0 ){}
        	    else if(x==2 && l>1 && r>1)
        	    	cnt=0;
            else if(r>x-1 && l>x-2)
            	cnt=0;
            else if(r>x-2 && l>x-1)
            	cnt=0;
            if(cnt!=0) 
            	cout<<"Case #"<<i<<": RICHARD"<<endl;
            else 	
            	cout<<"Case #"<<i<<": GABRIEL"<<endl;
           	i++;
	}
	return 0;
}
