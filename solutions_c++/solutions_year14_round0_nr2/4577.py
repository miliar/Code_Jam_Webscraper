#include <iostream>
#include<fstream>
using namespace std;
 
int main() 
{
    ifstream fin("abc.txt");
    ofstream fout("ex.txt",ios::app);
    fout.precision(9);
	int loop;
	fin>>loop;
	long double C,F,X;
	for(int i=1;i<=loop;i++)
	{
		long double t=0.0;
		fin>>C>>F>>X;
		long double r=2;
		while(r<=F*((X/C)-1))
		{
			t=t+(C/r);
			r=r+F;
		}
		fout<<"Case #"<<i<<": "<<t+(X/r)<<"\n";
	}
	return 0;
}
