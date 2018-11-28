#include <iostream>
#include <fstream>
using namespace std;

class CookieGame
{
private:
	double T, cF, C, F, X;
public:
	CookieGame(double iC, double iF, double iX)
	{
		T = 0.0;
		cF = 2.0;
		C = iC;
		F = iF;
		X = iX;
	}

	bool shouldBuildFarm()
	{
		double
			t1 = X / cF,
			t2 = C / cF,
			nF = cF + F;
		t2 += (X / nF);

		if( t1 > t2 )
			return true;
		else
			return false;

	}

	bool tick()
	{
		if( shouldBuildFarm() )
		{
			T += (C / cF);
			cF += F;

			return false;
		}
		else
		{
			T += (X / cF);
			return true;
		}
	}

	double getTime()
	{
		return T;
	}
};

int main(int argc, char **argv)
{
	int nCases;
	double C, F, X;
	ifstream inFile("B-large.in");
	
	cout << fixed;
	cout.precision(7);

	inFile >> nCases;
	for(int i=0; i<nCases; i++)
	{
		inFile >> C >> F >> X;
		CookieGame cg(C, F, X);

		while( !cg.tick() ) ;
		
		cout << "Case #" << i+1 << ": " << cg.getTime() << '\n';
	}

	inFile.close();
	return 0;
}