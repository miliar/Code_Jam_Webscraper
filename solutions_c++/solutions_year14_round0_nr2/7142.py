#include <fstream>
#include <vector>
#include <iostream>
#include <limits>

int main(int argc, char* argv[])
{
	std::ifstream fin(argv[1]);

	int T;
	fin >> T;
	for (int t=0; t<T; t++) {
		double C, F, X;
		fin >> C >> F >> X;

		double result_time = std::numeric_limits<double>::max();
		double start_time = 0;
		for (int i=0; ; i++) {
			const double rate = 2 + F * i;
			const double time = X / rate + start_time;
			if (time > result_time) {
				break;
			}
			result_time = time;
			start_time += C / rate;
		}

		printf("Case #%d: %.7f\n", t+1, result_time);
	}

	return 0;
}
