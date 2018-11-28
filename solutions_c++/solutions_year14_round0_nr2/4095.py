#include <iostream>
#include <string>
#include <fstream>

using std::cin;
using std::cout;
using std::endl;
using std::string;
using std::ifstream;
using std::ofstream;
using std::ios;

int main()
{
	cout<<"Please input file name: ";
	string infilename;
	string number;
	cin >> infilename;
	ifstream infile(infilename.c_str());
	if(!infile)
	{
		cout<<"error: unable to open input file"<<endl;
		return -1;
	}
	ofstream outfile("out.txt");
	int T;
	infile>>T;
	double C, F, X;
	C=F=X=0.0;
	
	for(int i=1;i<=T;i++)
	{
		infile>>C>>F>>X;
		long n;
		double T0,T,A0,A,B;
		T0=X/2.0;
		A=A0=0.0;
		n=0;

		do{
			n=n+1;
			A0=A;
			if(n==1)
			{
				T0=X/2.0;
				
			}
			if(n>1)
			{
				T0=T;
				
			}

			A=A0+1.0/(2.0+(n-1)*F);
			B=1.0/(2.0+n*F);
			T=C*A+X*B;

		}while(T<=T0);
		
		outfile.setf(ios::showpoint);
		outfile.precision(7);
		outfile.setf(ios::fixed);

		outfile<<"Case #"<<i<<": "<<T0<<'\xA';

	}
	infile.close();
	outfile.close();


	return 0;
}