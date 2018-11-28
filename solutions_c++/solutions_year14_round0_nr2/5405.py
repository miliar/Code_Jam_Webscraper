#include <iostream>
#include <algorithm>
#include <cmath>

const double eps = 1e-7;

using namespace std;


int main(int argc, char const *argv[])
{
	int cases; cin >> cases;

	for (int tc = 1; tc <= cases; ++tc)
	{

		cout << "Case #" << tc << ": ";

		double C, F, X;
		cin >> C >> F >> X;

		int Y = 0;

		double now = 0;
		int cnt = 1000000;

		while (true) {
			if (C / (2.0 + Y * F) + X / (2.0 + (Y + 1) * F) > X / (2 + Y * F)) 
				break;
			now += C / (2.0 + Y * F);
			Y ++;

			//cout << now << endl;
		}

		now += X / (2 + Y * F);

		printf("%.7lf\n", now);
		
	}
	return 0;
}