#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <iomanip>

using namespace std;
int t;
int grid1[4][4];
int grid2[4][4];

string compute(double c, double f, double x) {
	double rate = 2.0;
	double totaltime = x / rate;
	double prevtotaltime = x;
	double currenttime = 0;
	while (totaltime < prevtotaltime) {
		prevtotaltime = totaltime;
		currenttime += c / rate;
		rate += f;
		totaltime = currenttime + x / rate;
	}
	stringstream ss;
	ss << fixed << setprecision(7) << prevtotaltime;
	return ss.str();
}

int main() {
	std::ifstream input("B-large.in");
	ofstream myfile;
	myfile.open("output.txt");

	input >> t;
	for (int i = 0; i < t; i++) {
		double c, f, x;
		input >> c >> f >> x;
		myfile << "Case #" << i + 1 << ": ";
		myfile << compute(c, f, x) << "\n";
	}
	myfile.close();
	return 0;

	/*
	 cin >> t;
	 for (int i = 0; i < t; i++) {
	 double c, f, x;
	 cin >> c >> f >> x;
	 cout << "Case #" << i + 1 << ": ";
	 cout << compute(c, f, x) << "\n";
	 }
	 return 0;*/
}
