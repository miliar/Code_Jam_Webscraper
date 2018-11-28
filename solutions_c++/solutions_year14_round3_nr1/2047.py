#include <iostream>

#include <stdio.h>

using namespace std;


int main()
 {



int t,i,cnt,s;

int p,q;

cin>>t;

for(i=0;i<t;i++)

{   
 cnt=0;
	
scanf("%i/%i",&p,&q);


	
if((p/q)>1 || ((q%p==0)&&!( !((q/p) == 0) && !((q/p) & ((q/p) - 1)))) || ((q%p!=0)&&!( !((q) == 0) && !((q) & ((q) - 1)))))
	
{
		
cout <<"Case #"<<i+1<<": impossible\n";
	
}
	

	else
	
{
	
if(q%p==0)
	
{  s=q/p;
	
   while(s!=1)
	   {
	   
	 s=s/2;
	   	 cnt++;
	  
 }
	   
 
   }
   
 else
    {
   
 while(q>=p)
	  
 {
	   	
 q=q/2;
	   	
 cnt++;
	  
 }	
   
 }
  
 cout <<"Case #"<<i+1<<": "<<cnt <<"\n";
	

	}
	
}

	
return 0;

}