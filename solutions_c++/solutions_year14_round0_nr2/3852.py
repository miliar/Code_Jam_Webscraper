#include<iostream>
#include<fstream>
#include<iomanip>

using namespace std;

int main ()
{
	ifstream fin ("B-Large.in" );
	ofstream fout ("out.txt");

	if ( !fin )
	{
		cout << "Error! File not found. " << endl;
		exit(0);
	}
	int cases;
	fin >> cases;

	for ( int c1 = 0 ; c1 < cases ; c1++ )
	{
		double c = 500 , f = 4 , x = 2000;
		fin >> c >> f >> x;
		double seconds = 0 , rate = 2 , cookies = 0 , est1 = x / rate , est2 = 0;
		est2 = seconds + x / rate;
		do
		{
			est1 = est2;
			seconds = seconds + c / rate;
			rate = rate + f;
			est2 = seconds + x / rate;
		}while ( est1 > est2 );
		seconds = seconds - c / ( rate - f );
		seconds = seconds + x / ( rate - f );

		fout << "Case #" << c1+1 << ": " << setprecision ( 7) << fixed <<seconds << endl;
	}
	return 0;
}
