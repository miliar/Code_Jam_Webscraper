#include <iostream.h>
#include <fstream.h>
#include<math.h>
int main()
{
  ofstream out("output.txt");
  ifstream inn("C-small-attempt0.in");
  int N,a,b;
  inn>>N;
  for(int k=1;k<=N;k++)	
   {
   	int c=0;
   	inn>>a;
   	inn>>b;
   	for(int i=a;i<=b;i++)
   	 {
   	 	int s=0,h=i,u;
 	   	while(h!=0)
	    	 {
 	   	 s=((s*10)+h%10);
			 h=h/10;	
	    	 }
	    	 
 	   	 u=sqrt(i);
 	   	 if(u*u==i&&s==i)
 	   	 {int s1=0,z=sqrt(i);
			 while(z!=0)
	    	 {
 	   	  s1=((s1*10)+z%10);
			 z=z/10;	
	    	 }
	    if(s1==sqrt(i))
		 c++;}	 
   	 }
   	 out<<"Case #"<<k<<": "<<c<<endl;
   	
   }
}