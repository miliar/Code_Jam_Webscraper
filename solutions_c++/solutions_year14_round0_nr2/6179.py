#include <fstream>
#include <iostream>
#include <vector>

using namespace std;

string NL = "\n";

long double solve(long double farm_cost, long double farm_rate, long double goal) {
	vector<long double> times;
	times.push_back(goal / 2);

	for(int i = 1; true; ++i) {
		long double rate = 2.0;
		long double secs = 0;
		for(int j = 0; j < i; ++j) {
			secs += farm_cost / rate;
			rate += farm_rate;
		}

		secs += goal / rate;

		//
		// cout << i << ": " << secs << NL;
		//

		if(secs > times.back())
			break;

		times.push_back(secs);
	}

	return times.back();
}

int main() {
	int T;
	long double C;
	long double F;
	long double X;

	vector<long double> results;

	ifstream fin("B-large.in");
	fin >> T;
	for (int i = 0; i < T; ++i) {
		fin >> C;
		fin >> F;
		fin >> X;

		results.push_back(solve(C, F, X));
	}
	fin.close();

	ofstream fout("cookie-clicker-alpha.out");
	fout.precision(15);
	for(int i = 0; i < results.size(); ++i)
		fout << "Case #" << i + 1 << ": " << results[i] << NL;

	fout.close();

	return 0;
}