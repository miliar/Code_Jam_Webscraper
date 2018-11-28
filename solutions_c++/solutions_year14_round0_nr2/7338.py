#include <iostream>
#include <fstream>
#include <iomanip>
using namespace std;

int T;
double C,F,X;
int k = 0;
ifstream fin;
ofstream fout;

int main()
{
	fin.open("input.in");
	fout.open("output.out");
	if( !fin ){ return -1;}
	double tmp1,tmp2,tmp3;

	fin >> T;
	for( int iter = 0; iter < T; ++iter )
	{
		fin >> C >> F >> X;
		tmp1 = tmp2 = tmp3 = 0;
		k = 0;
		while(true)
		{
			tmp3 = C/(2+k*F);
			tmp2 = X/(2+k*F);
			tmp1 = X/(2+(k+1)*F);
			if( tmp1-tmp2+tmp3 < 0 ) ++k;
			else 
				break;
		}
		for( int i = 0; i < k; ++i )
			tmp2 += C/(2+F*i);
		fout << "Case #" << iter+1 << ": " << fixed << setprecision(7) << tmp2 << '\n';
	}
}