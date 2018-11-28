#include <iostream>
#include <string>

using namespace std;

int main() {
	int N;
	scanf_s("%d", &N);
	cout.precision(7);
	cout.setf(std::ios::fixed, std::ios::floatfield);
	for (int i = 0; i < N; i++) {
		double C, F, X;
		cin >> C >> F >> X;
		double cps = 2;
		double time = 0;
		while ((C/ cps) + (X / (cps + F)) < (X / cps)) {
			time += (C / cps);
			cps += F;
		}
		cout << "Case #" + to_string(i+1) + ": " << (time + (X / cps)) << endl;
	}
	return 0;
}