
#include<bits/stdc++.h>
#include<iostream>
using namespace std;
int main()
 {
 	
 	int t;
 	 cin>>t;
 	 int k=1;
 	   while(t--)
 	    {
 	    	  int n,r,c;
 	    	    cin>>n>>r>>c;
 	    	    if(n==1)
 	    	     {
 	    	     	 cout<<"CASE #"<<k++<<": GABRIEL"<<endl;
 	    	     }
 	    	     else if(n==2)
 	    	      {
 	    	      	     if((r==1  && c==3 ) || (r==3  && c==1 ) || (r==1  && c==1 ) || (r==3  && c==3 ))
 	    	      	      {
 	    	      	      	  cout<<"CASE #"<<k++<<": RICHARD"<<endl;
 	    	      	      }
 	    	      	      else
 	    	      	        cout<<"CASE #"<<k++<<": GABRIEL"<<endl;
 	    	      }
 	    	      
 	    	      else if(n==3)
 	    	       {
 	    	       	  if((r==2  && c==3 ) || (r==3  && c==2 ) || (r==3  && c==3 ) || (r==3  && c==4 ) || (r==4  && c==3 ) )
 	    	       	  cout<<"CASE #"<<k++<<": GABRIEL"<<endl;
 	    	       	  else
 	    	       	  cout<<"CASE #"<<k++<<": RICHARD"<<endl;
 	    	       	   
 	    	       }
 	    	       else
 	    	        {
 	    	        	if((r==3 && c==4 ) ||  (r==4 && c==3 ) || (r==4 && c==4 ))
 	    	        	cout<<"CASE #"<<k++<<": GABRIEL"<<endl;
 	    	        	else
 	    	        	cout<<"CASE #"<<k++<<": RICHARD"<<endl;
 	    	        	
 	    	        	  
 	    	        }
 	    }
 	    return 0;
 }
