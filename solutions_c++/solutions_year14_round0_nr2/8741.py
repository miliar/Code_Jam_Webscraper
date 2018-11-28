#include <iostream>
#include <cstdio>
#include <iomanip>

using namespace std;

int main()
{
	int tc, m = 1;
	double c, f, x;
	double rate = 2;
	double time1, time2, time3;
	double sum = 0.000000;

	scanf("%d", &tc);

	while (tc--) {
		rate = 2;
		sum = 0;
		cin >> c;
		cin >> f;
		cin >> x;

		while (1) {
			time1 = c / rate;

			time2 = x / rate;
			time3 = x / (rate + f);
			
			rate = rate + f;
			
			if ((time1 + time3) > time2) {
				sum = sum + time2;
				break;
			}

			else {
				sum = sum + time1;
			}
		}

		cout << "Case #"<< m <<": "<< setprecision(7) <<fixed <<(double)sum << endl;
	m++;
	}

	return 0;
}
			


