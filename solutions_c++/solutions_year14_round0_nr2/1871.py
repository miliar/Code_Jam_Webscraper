#include <fstream>
#include <iostream>
#include <iomanip>
#include <cstring>
#include <cstdio>
#include <cstdlib>
using namespace std;

const string input = "b.in",
			 output = "b.out";

int main()
{
	int T;
	ifstream fin(input.c_str());
	ofstream fout(output.c_str());
	fout.setf(ios::fixed);
	
	fin >> T;
	for (int time = 0; time < T; ++time) {
		double C, F, X;
		fin >> C >> F >> X;
		int n = X + 1;
		double ans = X / 2.0, base = 0, x = 2;
		for (int i = 0; i <= n; ++i) {
			base += C / x;
			x += F;
			double tmp = base + X / x;
			if (tmp < ans) ans = tmp;
		}
		fout << "Case #" << time + 1 << ": ";
		fout << setprecision(7) << ans << endl;
	}
	return 0;
}