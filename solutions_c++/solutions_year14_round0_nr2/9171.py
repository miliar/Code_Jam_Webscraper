#include <iostream>
#include <fstream>
#include <vector>
#include <iomanip>
#include <queue>
#include <string>
#include <math.h>
#define DEBUG 1
#define LOG(x) if(DEBUG) cout << x << endl
using namespace std;

double time(int iter, double C, double F, double X) {
	double t = 0;
	double rate = 2;
	for(int i = 0; i < iter; i++) {
		t += (C / rate);
		rate += F;
	}
	t += X / rate;
	return t;
}

int main() {
	ifstream in;
	in.open("B-large.in", ios::in);
	ofstream out;
	out.open("B-large.out", ios::out);
	int T;
	in >> T;
	for(int t = 0; t < T; t++) {
		double C, F, X;
		in >> C >> F >> X;
		int iters = 0;
		double prev = 10000000000.;
		while(1) {
			double cur = time(iters, C, F, X);
			if(cur > prev) {
				goto exit;
			} else {
				iters++;
				prev = cur;
			}
		}
		exit:
		out << "Case #" << (t + 1) << ": " << fixed << setprecision(7) << prev << endl;
	}
	in.close();
	out.close();
}