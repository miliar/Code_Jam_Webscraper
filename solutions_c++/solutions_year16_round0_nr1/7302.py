#include<iostream>
using namespace std;
int main()
{
	int t;long int x[100];
	cin>>t;
	
	for(int i=0;i<t;i++)
	  { 
	  	cin>>x[i];
      }
	for(int i=0;i<t;i++)
	  { 
	  	int yes[10]={0,0,0,0,0,0,0,0,0,0},dig,m=1,n=0;
		  long int a;	
		  if(x[i]==0)
		  {
		  	cout<<"Case #"<<i+1<<": INSOMNIA"<<"\n";
		  	continue;
						   }		     	
	  	loop: 
		  a=x[i]*m;	      
		  while(a!=0)
		  {
		  	dig=a%10;
		  	a=a/10;
		  	yes[dig]=1;
			  					
		  }
		  while(1)
		   {
		   	if(yes[n]==0)
		   	   {m++;		   	   
				goto loop;
			   }
			else
			   {
			    if(n==9)
			      {			  
			       cout<<"Case #"<<i+1<<": "<<x[i]*m<<"\n";
			       break;
		          }
			    n++;
				goto loop;   
			   }
			  
	       }
       }
}

