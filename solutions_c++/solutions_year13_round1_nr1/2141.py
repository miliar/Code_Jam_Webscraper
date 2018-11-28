#include<iostream>
#include<math.h>
#include<fstream>
using namespace std;
ifstream in;
ofstream out;

int main()
{
	in.open("A-small-attempt0.in");
	out.open("out.in");
	
	long double t,r,T,i,c;
	in>>T;
	
	for(i=1;i<=T;i++)
	{
		in>>r>>t;	
		for(c=0;;)
		{
				t=t-pow(r+1,2)+pow(r,2);
				if(t<0)
					break;
			//	cout<<t<<endl;
				
				r+=2;
				
			//	cout<<r<<endl;
				c++;		
		}	
		out<<"Case #"<<i<<": "<<c<<endl; 	//	cout<<endl<<endl;
	}
	
	return 0;
}
