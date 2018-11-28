#include <iostream>
#include <iomanip>
#include <fstream>
using namespace std;

#define RATE 2.0

double processOneRound()
{
	double time = 0;
	int farmCount = 0;
	double cookies = 0.0;
	double C;	// Cost per farm
	double F;	// Extra cookies per farm
	double X;	// Goal
	cin >> C >> F >> X;

	if (X <= C)
		return X / RATE;

	while (true)
	{
		if (cookies < C)
		{
			double diff = C - cookies;
			cookies += diff;
			time += diff / (RATE + farmCount * F);
		}
		else // enough for a new farm
		{
			double noNewFarm = (X - cookies) / (RATE + farmCount * F);
			double withNewFarm = (X - cookies + C) / (RATE + (farmCount + 1) * F);

			if (noNewFarm < withNewFarm)
				return time + noNewFarm;
			else
			{
				++farmCount;
				cookies -= C;
			}
		}
	}

	return time;
}

int main()
{
	std::ifstream in("B-large.in");
	std::streambuf *cinbuf = std::cin.rdbuf(); //save old buf
	std::cin.rdbuf(in.rdbuf()); //redirect std::cin to in.txt!

	std::ofstream out("out.txt");
	std::streambuf *coutbuf = std::cout.rdbuf(); //save old buf
	std::cout.rdbuf(out.rdbuf()); //redirect std::cout to out.txt!

	int numCases = 0;
	cin >> numCases;
	cout << setprecision(12);
	for (int i = 0; i < numCases; ++i)
		cout << "Case #" << (i + 1) << ": " << processOneRound() << endl;

	return 0;
}