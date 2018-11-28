#include <iostream.h>
#include <fstream.h>
#include<math.h>
int test(int x);
int main()
{
  ofstream out("output.txt");
  ifstream inn("C-small-attempt0.in");
  int g,y,z;
  inn>>g;
  for(int f=1;f<=g;f++)	
   {
   	int s=0;
   	inn>>y>>z;
   	
   	for(int i=y;i<=z;i++)
   	 {int A=sqrt(i);	
		if(test(i)&&A*A==i)
		if(test(A))
		s++;
   	
     }  
   	 out<<"Case #"<<f<<": "<<s<<endl;
   	
  
  }
}
int test(int x)
{
	int f=0,a=x;
	while(a!=0)
	{
	  	 f=((f*10)+a%10);
	  a=a/10;	
	}
	if(f==x)
	return 1;
	return 0;
}