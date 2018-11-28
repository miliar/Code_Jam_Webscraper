#include <iostream>
#include <map>
#include <vector>
#include <cmath>
#include <algorithm>
#include <iostream>
#include <iomanip>
#include <limits>

using namespace std;

int main(int argc, char const *argv[])
{
	cout << setprecision(numeric_limits<long double>::digits10);

	int T;

	cin >> T;

	for(int i=0; i<T; i++)
	{
		double C, F, X, cookies = 0.0, t=0;
		double R = 2;

		cin >> C >> F >> X;

		// cout << C << " " << F << " " << X << endl;

		bool working = true;

		while(working)
		{
			if(C/R+X/(R+F)<X/R)
			{
				t += C/R;
				R += F;
			}
		 	else
		 	{
		 		t += X/R;
		 		working = false;
		 	}
		}

		cout << "Case #" << (i+1) << ": " << t << endl;
	}

	return 0;
}