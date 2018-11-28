#include <iostream>
#include <cstdio>
#include <fstream>
#include <iomanip>

using namespace std;

int main()
{
	int t;
	scanf("%d", &t);
	double c, x, f, a, b;
	double rate;
	double time;

	//ofstream out("out1.txt");

	for (int i = 0; i < t; ++i) {
		scanf("%lf", &c);
		scanf("%lf", &f);
		scanf("%lf", &x);

		rate = 2.0;
		time = 0.0;
		
		while(1) {
			a = x/rate;
			b = c/rate;

			if(a < (b+(x/(rate+f)))) {
				printf("Case #%d: %.7lf\n", i+1, time+a);
				break;
			} else {
				time += b;
				rate += f;
			}
		}

	//	out<< "Case #" << i+1 << ": ";;
	//	out << std::fixed << std::setprecision(7) << time+a;
	//	out << "\n";
		
	}
	return 0;
}
