#include <iostream>
#include <iomanip>
#include <fstream>
using namespace std;

double c,f,x;

int main()
{
	ifstream cin("B-large.in");
	ofstream cout("B-large.out");
	int T;
	cin >> T;
	for( int s= 1; s<=T; ++s )
	{
		
		cin >> c >> f >> x;

		double curF = 2;
		double curX = 0;
		double t = 0;
		while(1)
		{
			double dt = x/curF;
			double dtBuy = c/curF+x/(curF+f);
			if( dt < dtBuy )
			{
				t += dt;
				break;
			}
			else
			{
				t += c/curF;
				curF+=f;
			}
		}

		cout << "Case #" << s << ": " << setprecision(7) <<  t << endl;
		
	}

	return 0;
}