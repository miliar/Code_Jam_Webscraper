#include <iostream>
#include <fstream>
using namespace std;

int main() {
//	cout << "start" << endl; // prints Hello World!

//	ifstream in("input.txt");
//	ofstream out("output.txt");
	cout.precision(15);

	int T;
	cin >> T;

	int Nmax = 10000000;
	long double C, F, X;
	long double two = 2.0;
	for (int x = 1; x <= T; x++) {
		cin >> C;
		cin >> F;
		cin >> X;

		long double timeF = 0.0;
		long double min = X/2;
		long double newT;
		for (int N = 1; N < Nmax; N++) {
			timeF += C / (two + F * (N - 1));
			newT = timeF + X / (two + F * N);
			if (newT < min) {
				min = newT;
			} else {
				//cout << N << endl;
				break;
			}
		}

		cout << "Case #" << x << ": " << min << endl;
	}

//	in.close();
//	out.close();

//	cout << "finish" << endl;
	return 0;
}
