#include<iostream>
using namespace std;
#include<stdio.h>
#include<stdlib.h>
int main()
 {
 
 	int test;
 	 cin>>test;
 	 int z=1;
 	   while(test--)
 	    {
 	    	  int ns,x,y;
 	    	    cin>>ns>>x>>y;
 	    	    if(ns==1)
 	    	     {
 	    	     	 cout<<"Case #"<<z++<<": GABRIEL"<<endl;
 	    	     }
 	    	     else if(ns==2)
 	    	      {
 	    	      	     if((x==1  && y==3 ) || (x==3  && y==1 ) || (x==1  && y==1 ) || (x==3  && y==3 ))
 	    	      	      {
 	    	      	      	  cout<<"Case #"<<z++<<": RICHARD"<<endl;
 	    	      	      }
 	    	      	      else
 	    	      	        cout<<"Case #"<<z++<<": GABRIEL"<<endl;
 	    	      }
 	    	      
 	    	      else if(ns==3)
 	    	       {
 	    	       	  if((x==2  && y==3 ) || (x==3  && y==2 ) || (x==3  && y==3 ) || (x==3  && y==4 ) || (x==4  && y==3 ) )
 	    	       	  cout<<"Case #"<<z++<<": GABRIEL"<<endl;
 	    	       	  else
 	    	       	  cout<<"Case #"<<z++<<": RICHARD"<<endl;
 	    	       	   
 	    	       }
 	    	       else
 	    	        {
 	    	        	if((x==3 && y==4 ) ||  (x==4 && y==3 ) || (x==4 && y==4 ))
 	    	        	cout<<"Case #"<<z++<<": GABRIEL"<<endl;
 	    	        	else
 	    	        	cout<<"Case #"<<z++<<": RICHARD"<<endl;
 	    	        	
 	    	        	  
 	    	        }
 	    }
 	    return 0;
 }
