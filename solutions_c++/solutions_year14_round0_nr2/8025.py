#include<fstream>
#include<iostream>
#include<iomanip>
#include<string>

int main()
{
	std::ifstream fin("B-large.in");
	std::ofstream fout("B-large.out");

	int cases;

	double factoryPrice, factoryCps, goal, elapsedTime = 0, prevElapsedTime = 0, currentAmount = 0, cps = 2;

	fin >> cases;
	fout << std::setprecision(7) << std::fixed;

	for(int test = 1; test <= cases; ++test) {

		fin >> factoryPrice >> factoryCps >> goal;

		do {
			currentAmount += factoryPrice;
			prevElapsedTime = elapsedTime;
			elapsedTime += factoryPrice / cps;
			cps += factoryCps;
		} while(elapsedTime + goal / cps < prevElapsedTime + goal / (cps - factoryCps));

		fout << "Case #" << test << ": " << prevElapsedTime + goal / (cps - factoryCps) << '\n';

		elapsedTime = prevElapsedTime = currentAmount = 0;
		cps = 2;
	}

	return 0;
}
