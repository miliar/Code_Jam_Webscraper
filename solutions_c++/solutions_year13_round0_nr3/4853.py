#include<iostream>
#include<fstream>
#include<math.h>
using namespace std;
int test(int x)
{
	int y=0,q,m;
	q=x;
	for(;x!=0;)
	{
		m=x%10;
		y=y*10+m;
		x=x/10;
	}
	if(y==q)
		return 1;
	else
		return 0;
}
int main()
{
	ifstream in;
	ofstream out;
  	in.open ("C-small-attempt0.in");
  	out.open("out.in");
 	double n,a,b,i,c;
	 double s,j;		
	in>>n;
	for(i=1;i<=n;i++)
	{
		c=0;
		in>>a>>b;   
		for(j=a;j<=b;j++)
		{
			if(test(j))   
			{
				
				
				s=sqrt(j);	
				if(s==int(s))  
					if(test(s))
					c++;
					
			}
		}	
			
		out<<"Case #"<<i<<": "<<c<<endl;	
	}			
	
	return 0;
}
