#include<bits/stdc++.h>
using namespace std;
int main()
{
	int t, n,tt=0,a,b,k,i,j;  //<<>>
	cin>>t;
	
	while(t--)
	{ 
		tt++;
		int ct=0;
		int a,b,k;
		cin>>a>>b>>k;
		
		for(i=0;i<a;i++)
		{
			for(j=0;j<b;j++)
			{
				 if( (i & j) <k)
				  {   
					  //cout<<a<<" "<<b<<endl;
					  ct++;
				  }
			}	  
		}    
			  
			
	    cout<<"Case #"<<tt<<": "<<ct<<endl;
		
		
    }  	  
	return 0;
}		

