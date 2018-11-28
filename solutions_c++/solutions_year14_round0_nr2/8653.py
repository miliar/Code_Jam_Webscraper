#include <iostream>
#include <fstream>
#include <iomanip>

using namespace std;
int main() 
{	double c, f, x;
	double regi, uj;
	
	ifstream f1;
	f1.open("in.txt");
	
	ofstream f2;
	f2.open ("out.txt");
	
	int nt;
	f1 >> nt;

	
	for (int t=0; t<nt; t++)
	{
		f1 >> c;
		f1 >> f;
		f1 >> x;

		regi=x/2;

		int nf=1;
		double ksz=c/2;
		uj=ksz+x/(2+nf*f);
		
		while (uj<regi)
		{
			regi=uj;
			ksz=ksz+c/(2+nf*f);
			nf++;
			uj=ksz+x/(2+nf*f);
		}

		f2 <<"Case #"<< t+1 <<": "<<setprecision(10) << regi <<"\n";
			
	}
	
	f1.close();
	f2.close();
    return 0; 
}