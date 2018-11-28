#include <iostream>
#include <fstream>

using namespace std;

/**
	Google Code Jam
	Qualification Round 2014
	Problem B. Cookie Clicker Alpha

	https://code.google.com/codejam/contest/2974486/dashboard#s=p1
*/

double calc(double C, double F, double X, double rate) {
	double wait_time = X / rate, buy_time = C / rate;
	if (wait_time < 0.1)
		return wait_time;

	double buy = buy_time + calc(C, F, X, rate + F);
	return min(wait_time, buy);
}

void solve_next_testcase(ifstream &in, ofstream &out, int case_nr) {
	double C, F, X;
	in >> C >> F >> X;

	double sol = calc(C, F, X, 2);
	// cout << showpoint << "Case #" << case_nr << ": " << sol << endl;
	out  << showpoint << "Case #" << case_nr << ": " << sol << endl;
}

int main () {
	ifstream in;
	ofstream out;
	in.precision(20);
	out.precision(20);
	cout.precision(20);

	// in.open("i2.txt");
	in.open("B-small-attempt5.in");
	out.open("output-small.txt");
	// in.open("A-large-practice.in");
	// out.open("output-large.txt");

	int T;
	in >> T;
	int case_nr = 0;
	while (case_nr ++ < T)
		solve_next_testcase(in, out, case_nr);

    in.close();
    out.close();
	return 0;
}