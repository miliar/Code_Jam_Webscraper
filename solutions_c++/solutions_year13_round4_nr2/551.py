#include <iostream>

using namespace std;

typedef long long Int64;

int N;
Int64 P;
int win[1000];

void Solve(Int64 _P) {
	if (((Int64)1 << N) == _P) {
		cout << (_P - 1) << " " << (_P - 1) << endl;
		return;
	}

	Int64 half = (Int64)1 << (N - 1);
	Int64 P = _P + 1;
	for (int i = 0; i < N; i++) {
		if (P <= half) win[i] = 1;
		else {
			win[i] = 0;
			P -= half;
		}
		half /= 2;
		//cout << win[i];
	}
	//cout << endl;
	int sum = 0;
	for (int i = 0; i < N; i++)
		if (!win[i]) sum++;
		else {
			for (; i < N; i++)
				if (!win[i]) {
					sum++;
					break;
				}
			break;
		}
	//cout << sum << endl;
	cout << (((Int64)1 << sum) - 2) << " ";

	half = (Int64)1 << (N - 1);
	P = _P;
	for (int i = 0; i < N; i++) {
		if (P <= half) win[i] = 1;
		else {
			win[i] = 0;
			P -= half;
		}
		half /= 2;
		//cout << win[i];
	}
	//cout << endl;
	sum = 0;
	for (int i = 0; i < N; i++)
		if (win[i]) sum++;
		else {
			for (; i < N; i++)
				if (win[i]) {
					sum++;
					break;
				}
			break;
		}
	cout << (((Int64)1 << N) - (((Int64)1 << sum)));
	cout << endl;
}

int main() {
	int t;
	cin >> t;
	for (int i = 1; i <= t; i++) {
		cout << "Case #" << i << ": ";
		cin >> N >> P;
		Solve(P);
	}
	return 0;
}