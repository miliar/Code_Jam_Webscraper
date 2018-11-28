#include <iostream>
#include <vector>
using namespace std;

#define MAXP 100000010

bool flag[MAXP] = {};
int primes[MAXP / 3] = {}, pi;

void getPrime() {
	int i, j;
	pi = 0;
	for (i = 2; i < MAXP; i++) {
		if (!flag[i]) primes[pi++] = i;
		for (j = 0; j < pi && i * primes[j] < MAXP; j++) {
			flag[i * primes[j]] = true;
			if (i % primes[j] == 0) break;
		}
	}
//	cout << pi << " primes found." << endl;
}

int findDiv(long long x) {
	if (x < MAXP && flag[x] == false) return -1;
	for (int i = 0; i < pi && 1ll * primes[i] * primes[i] <= x; i++) {
		if (x % primes[i] == 0)
			return primes[i];
	}
	return -1;
}

long long construct(string str, int base) {
	long long ret = 0, cube = 1;
	for (int i = str.size() - 1; i >= 0; i--) {
		if (str[i] == '1') ret += cube;
		cube *= base;
	}
	return ret;
}

void work(int N, int J) {
	int total = (1<<N);
	int arr[15] = {0};
	for (int pos = total / 2; pos < total && J > 0; pos++) {
		string str("");
		int x = pos;
		while (x > 0) {
			if (x % 2 == 0)	str.insert(0, "0");
			else			str.insert(0, "1");
			x /= 2;
		}
//		cout << "Current: " << str << endl;
		if (str.front() == '0' || str.back() == '0') continue;
		bool flag = true;
		for (int i = 2; i <= 10; i++) {
			long long number = construct(str, i);
			int div = findDiv(number);
			arr[i] = div;
			if (div == -1) {
				flag = false;
				break;
			}
		}
		if (flag) {
			J--;
			cout << str;
			for (int i = 2; i <= 10; i++)
				cout << " " << arr[i];
			cout << endl;
		}
	}
}

int main() {
	int cas, N, J;
	getPrime();
	cin >> cas;
	for (int i = 1; i <= cas; i++) {
		cin >> N >> J;
		cout << "Case #" << i << ":" << endl;
		work(N, J);
	}
	return 0;
}


