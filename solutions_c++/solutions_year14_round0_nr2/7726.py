#include<iostream>
#include<fstream>
using namespace std;
#include <iomanip>

ifstream fin("input.txt");
ofstream fout("output.out");

int main(void)
{
	int T;
	double C,F,X;
	

	fin>>T;
	

	for(int i=1; i<=T; i++)
	{
		int ok=1;

		double answer=0;
		double aux=0;
		double aux1=0;
		double ratio=2.0;
		double A;
		fin>>C>>F>>X;
		while(ok)
		{
			if(C>X)
			{
				answer=answer+X/ratio;
				ok=0;
			}
			else
			{
				aux=X/ratio;
				aux1=C/ratio + X/ (ratio+F);
				if(aux1<aux)
				{
					A=C/ratio;
					answer=answer+C/ratio;
					ratio=ratio+F;				
				}
				else
				{
					ok=0;
					answer=answer+X/ratio;
				}
			}
		}

		fout<<"Case #"<<i<<": "<<setprecision(10)<<answer<<endl;
	}

	return 0;
}