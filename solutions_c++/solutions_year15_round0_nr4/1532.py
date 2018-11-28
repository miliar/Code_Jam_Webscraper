#include<iostream>
using namespace std;
#include<bits/stdc++.h>
int main()
 {
 	freopen("abc.txt","r",stdin);
 	freopen("pqr.txt","w",stdout);
 	int t;
 	 cin>>t;
 	 int tt=1;
 	   while(t--)
 	    {
 	    	  int n,a,b;
 	    	    cin>>n>>a>>b;
 	    	    if(n==1)
 	    	     {
 	    	     	 cout<<"Case #"<<tt++<<": GABRIEL"<<endl;
 	    	     }
 	    	     else if(n==2)
 	    	      {
 	    	      	     if((a==1  && b==3 ) || (a==3  && b==1 ) || (a==1  && b==1 ) || (a==3  && b==3 ))
 	    	      	      {
 	    	      	      	  cout<<"Case #"<<tt++<<": RICHARD"<<endl;
 	    	      	      }
 	    	      	      else
 	    	      	        cout<<"Case #"<<tt++<<": GABRIEL"<<endl;
 	    	      }
 	    	      
 	    	      else if(n==3)
 	    	       {
 	    	       	  if((a==2  && b==3 ) || (a==3  && b==2 ) || (a==3  && b==3 ) || (a==3  && b==4 ) || (a==4  && b==3 ) )
 	    	       	  cout<<"Case #"<<tt++<<": GABRIEL"<<endl;
 	    	       	  else
 	    	       	  cout<<"Case #"<<tt++<<": RICHARD"<<endl;
 	    	       	   
 	    	       }
 	    	       else
 	    	        {
 	    	        	if((a==3 && b==4 ) ||  (a==4 && b==3 ) || (a==4 && b==4 ))
 	    	        	cout<<"Case #"<<tt++<<": GABRIEL"<<endl;
 	    	        	else
 	    	        	cout<<"Case #"<<tt++<<": RICHARD"<<endl;
 	    	        	
 	    	        	  
 	    	        }
 	    }
 	    return 0;
 }
