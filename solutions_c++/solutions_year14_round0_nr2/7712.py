#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <map>


#define rep(i,n) for( int i = 0; i < n; i++ )

using namespace std;

int main()
{
	ofstream output("B-large.out");
	ifstream input("B-large.in");

	cin.rdbuf( input.rdbuf() );
	cout.rdbuf( output.rdbuf() );

	int T;
	cin >> T;

	rep(t,T)
	{
		double C,F,X;
		cin >> C >> F >> X;

		double curTime = 0;
		double curF = 2;

		while( true )
		{
			double secondsWithoutFarm = X / curF;
			double secondsWithFarm = ( C / curF ) + ( X / ( curF + F ) );

			if( secondsWithoutFarm > secondsWithFarm )
			{
				// buy farm.
				curTime += ( C / curF );
				curF += F;
			}
			else
			{
				curTime += secondsWithoutFarm;
				break;
			}
		}

		std::cout.setf(std::ios_base::fixed, std::ios_base::floatfield);
		std::cout.precision(7);
		cout << "Case #" << t+1 << ": " << curTime << endl;
	}

	return 0;
}