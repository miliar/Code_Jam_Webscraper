// GCJRound1AA.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <sstream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
	int T;
	string linein;
	stringstream ss;

	getline(cin,linein);
	ss.str("");
	ss.clear();
	ss.str(linein);
	ss >> T;

	for (int t = 0; t < T; ++t)
	{
		long long r;
		long long paint;
		long double mr1, mr2, ans;
		unsigned long long rad;

		getline(cin,linein);
		ss.str("");
		ss.clear();
		ss.str(linein);
		ss >> r >> paint;

		// Solve quadratic relationship to determine max 
		long long twor = 2*r - 1;
		rad = twor*twor + 8*paint;
		
		long double base = (long double)(rad / powl(10,floor(log10l(rad))));
		long double tenp = (long double)(floorl(log10l(rad)));
//		cout << "twor: " << twor << endl << rad << endl << base << endl << tenp << endl;

		mr1 = ((long double)(-1)*(twor) + sqrtl(base) * powl(10,tenp/2)) / 4;
		mr2 = ((long double)(-1)*(twor) - sqrtl(base) * powl(10,tenp/2)) / 4;
		mr1 = ((-1)*twor + sqrtl(rad))/4;
		mr2 = ((-1)*twor - sqrtl(rad))/4;
//		cout << "radius " << r << endl << "paint " << paint << endl;
//		cout << "top " << (sqrtl(base) * powl(10,tenp/2)) << endl;
//		cout << "guess: " << (paint / (twor)) << endl;

//		cout << mr1 << endl << mr2 << endl;
		ans = (mr1 < 0 ? mr2 : mr1);

		cout << "Case #" << (t+1) << ": " << (long long)(floorl(ans)) << endl;
	}

	return 0;
}
