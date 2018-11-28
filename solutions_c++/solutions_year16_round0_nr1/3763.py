#include <iostream>

#define MAX_N 1000000

using namespace std;

long long N, R;
bool V[11];

void input()
{
	R = 0;
	for (int i = 0; i < 10; i++) V[i] = false;
	cin >> N;
}

void parseNum(long long num) {
	while (num > 0) {
		int temp = num % 10;
		if (!V[temp]) {
			V[temp] = true;
			R++;
		}
		num /= 10;
	}
}

void process() {
	if (N == 0) return;
	int num = N;
	while (R < 10) {
		parseNum(num);
		if (R >= 10) break;
		num += N;
	}
	N = num;
}

void output(int T) {
	cout << "Case #" << T << ": ";
	if (R == 0) cout << "INSOMNIA" << endl;
	else {
		cout << N << endl;
	}
}

int main()
{
	int T;
	cin >> T;
	for (int i = 1; i <= T; i++) {
		input();
		process();
		output(i);
	}
}