#include<iostream>
#include<stdio.h>
#include<queue>
#include<stack>
#include<stdlib.h>
#include<algorithm>
#include<math.h>
#include<string.h>
using namespace std;
int read_int(){
	char r;
	bool start=false,neg=false;
	long long int ret=0;
	while(true){
		r=getchar();
		if((r-'0'<0 || r-'0'>9) && r!='-' && !start){
			continue;
		}
		if((r-'0'<0 || r-'0'>9) && r!='-' && start){
			break;
		}
		if(start)ret*=10;
		start=true;
		if(r=='-')neg=true;
		else ret+=r-'0';
	}
	if(!neg)
		return ret;
	else
		return -ret;
}

int main()
 {
 	freopen("abc.txt","r",stdin);
 	freopen("out.txt","w",stdout);
 	int t;
 	 t=read_int();
 	 int numberoftestcase=1;
 	   while(t--)
 	    {
 	    	  int n;
			   int val1,val2;
 	    	    //cin>>n>>a>>b;
 	    	    n=read_int();
 	    	    val1=read_int();
 	    	    val2=read_int();
				 if(n==3)
 	    	       {
 	    	       	  if((val1==2  && val2==3 ) || (val1==3  && val2==2 ) || (val1==3  && val2==3 ) || (val1==3  && val2==4 ) || (val1==4  && val2==3 ) )
 	    	       	  cout<<"Case #"<<numberoftestcase++<<": GABRIEL"<<endl;
 	    	       	  else
 	    	       	  cout<<"Case #"<<numberoftestcase++<<": RICHARD"<<endl;
 	    	       	   
 	    	       }
				 
				 
				 
				 
				 
				 
				 else if(n==1)
 	    	     {
 	    	     	 cout<<"Case #"<<numberoftestcase++<<": GABRIEL"<<endl;
 	    	     }
 	    	     
				  
				  
				  
				  
				  
				  
				  else if(n==2)
 	    	      {
 	    	      	     if((val1==1  && val2==3 ) || (val1==3  && val2==1 ) || (val1==1  && val2==1 ) || (val1==3  && val2==3 ))
 	    	      	      {
 	    	      	      	  cout<<"Case #"<<numberoftestcase++<<": RICHARD"<<endl;
 	    	      	      }
 	    	      	      else
 	    	      	        cout<<"Case #"<<numberoftestcase++<<": GABRIEL"<<endl;
 	    	      }
 	    	      
 	    	      
 	    	       else 
 	    	        {
 	    	        	if((val1==3 && val2==4 ) ||  (val1==4 && val2==3 ) || (val1==4 && val2==4 ))
 	    	        	cout<<"Case #"<<numberoftestcase++<<": GABRIEL"<<endl;
 	    	        	else
 	    	        	cout<<"Case #"<<numberoftestcase++<<": RICHARD"<<endl;
 	    	        	
 	    	        	  
 	    	        }
 	    }
 	    return 0;
 }
