#include <iostream>
#include <vector>
#include <list>
#include <algorithm>

using namespace std;

double go()
{
	double C,F,X;
	double p = 2.0;
	double sec = 0.0;

	cin >> C >> F >> X;

	double upper = X / p;

	do {
		double buy = C / p;
		double remain = X / (p+F);
		double now = sec + buy + remain;

		if (now > upper)
			return upper;
		sec += buy;
		upper = now;
		p += F;
	} while (true);
}

int main(int ac, char**av)
{
	int T;

	cin >> T;
	std::cout.setf( std::ios::fixed, std:: ios::floatfield );
	std::cout.precision(7);
	for (int i = 1; i <= T; i++) {
		cout << "Case #" << i << ": " << go() << endl;
	}
	return 0;
}

