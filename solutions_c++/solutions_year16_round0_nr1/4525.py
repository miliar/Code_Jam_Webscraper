#include <iostream>
using namespace std;

bool hash[10];
int total;

int solve(int N)
{
	int i = 1;
	while (true) {
		int tmp = N * i;
		int buf = tmp;

		while (tmp) {
			int d = tmp % 10;
			if (!hash[d]) {
				hash[d] = true;
				total++;
				if (total == 10) return buf;
			}
			tmp /= 10;
		}
		i++;
	}
}

int main()
{
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		int N;
		cin >> N;

		for (int i = 0; i < 10; i++) hash[i] = false;
		total = 0;
		cout << "Case #" << t << ": ";
		if (N == 0)
			cout << "INSOMNIA" << endl;
		else {
			cout << solve(N) << endl;
		}
	}
}
