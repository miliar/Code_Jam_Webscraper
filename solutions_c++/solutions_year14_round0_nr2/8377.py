#include<iostream>
#include<fstream>
#include<iomanip>
using namespace std;
void main()
{
	int cases;
	long double C,F,X,s_t=0,f=2;
	ifstream filin("B-large.in",ios::in);
	ofstream filout("outputlarge.txt",ios::out);
	
	filin>>cases;

	for(int q=1;q<=cases;q++)
	{	f=2;s_t=0;
		filin>>C>>F>>X;
		
		while(((C/f)+(X/(f+F)))<(X/f))
		{	
			s_t=s_t+(C/f);
			f=f+F;
			
		}
	
		s_t=s_t+X/f;
		filout<<fixed<<setprecision(7);
		filout<<"\nCase #"<<q<<": "<<s_t;
		

	}
	filin.close();
	filout.close();
}

