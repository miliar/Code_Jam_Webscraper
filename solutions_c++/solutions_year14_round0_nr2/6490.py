#include <iostream>
#include <fstream>
using namespace std;
int main() {
	ifstream fin;
	ofstream fout;
	fin.open("B-large.in");
	fout.open("B-large.out");
	
	int N;
	fin >> N;
	for (int TestCase = 1; TestCase <= N; TestCase++) {
		double C, F, X;
		fin >> C >> F >> X;
		double second = 0;

		double CurrentGetCookies = 2;

		cout << fixed;
		cout.precision(7);
		while (true) {
			double second1, second2;
			second1 = (C / CurrentGetCookies) + (X / (CurrentGetCookies + F));
			second2 = X / CurrentGetCookies;
			if (second1 < second2) {
				second += C / CurrentGetCookies;
				CurrentGetCookies += F;
			}
			else {
				second += second2;
				break;
			}
		}
		fout << fixed;
		fout.precision(7);
		fout << "Case #" << TestCase << ": " << second << endl;
	}
	return 0;
}