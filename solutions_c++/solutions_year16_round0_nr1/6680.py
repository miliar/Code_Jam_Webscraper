#include "iostream.h"
#include "fstream"
using namespace std;
main()
{
	ifstream inn("A-large.in");
	ofstream out("output.txt");
	long n;
	long t;
	inn>>t;
	for(long tt=1;tt<=t;tt++){
		
	inn>>n;
	int a1[10]={0,1,2,3,4,5,6,7,8,9};
	long c,b=n;
	int counter=0;
	long z=n;
	

	int x=1;
	if(n==0)
		out<<"Case #"<<tt<<": INSOMNIA"<<endl;
		else
	while(true)
	{
		b=z;
		while(b!=0)
		{
			c=b%10;
			a1[c]=-1;
			b=b/10;	
		}//while
		counter=0;
		for(int k=0;k<10;k++){
			if(a1[k]==-1)
			counter++;
		}
		if(counter==10)
		{
			out<<"Case #"<<tt<<": "<<z<<endl;
			break;
		}//if
		
		
		x++;
		z= n*x;
	}//while true
	}//main loop
}//main