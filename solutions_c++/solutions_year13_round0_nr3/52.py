#include <iostream>
#include <string>
#include <cstring>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <bitset>
#include <queue>
#pragma comment (linker, "/STACK:256000000")

using namespace std;

bool isPalindrome(long long n) {
	long long m = 0, k = n;
	while (k) {
		m = m * 10LL + (k % 10LL);
		k /= 10LL;
	}
	return n == m;
}

const int maxN = 11000000;
bool nice[maxN];

void precalc() {
	for (long long i = 1; i < maxN; ++i) {
		if (isPalindrome(i) && isPalindrome(i * i)) {
			nice[i] = true;
			cout << i << endl;
		}
	}
}

const int maxL = 110;

struct number {
	int a[maxL];
	int len() const {
		for (int i = maxL - 1; i >= 0; --i) {
			if (a[i] != 0) {
				return i;
			}
		}
		return 0;
	}
	void print() const {
		int l = len();
		for (int i = l; i >= 0; --i) {
			printf("%d", a[i]);
		}
	}

	bool isPal() const {
		int l = len();
		for (int i = 0; i <= l; ++i) {
			if (a[i] != a[l - i]) {
				return false;
			}
		}
		return true;
	}

	void read() {
		string current;
		cin >> current;
		for (int i = 0; i < maxL; ++i) {
			a[i] = 0;
		}
		reverse(current.begin(), current.end());
		for (int i = 0; i < current.size(); ++i) {
			a[i] = current[i] - '0';
		}
	}
};

bool isLess(const number& A, const number& B) {
	int lA = A.len();
	int lB = B.len();

	if (lA < lB) {
		return true;
	}
	if (lA > lB) {
		return false;
	}

	for (int i = lA; i >= 0; --i) {
		if (A.a[i] < B.a[i]) {
			return true;
		}
		if (A.a[i] > B.a[i]) {
			return false;
		}
	}
	return false;
}

bool Equal(const number& A, const number& B) {
	int lA = A.len();
	int lB = B.len();

	if (lA != lB) {
		return false;
	}

	for (int i = lA; i >= 0; --i) {
		if (A.a[i] != B.a[i]) {
			return false;
		}
	}
	return true;
}

number operator - (number A, number B) {
	number C;
	for (int i = 0; i < maxL; ++i) {
		C.a[i] = A.a[i] - B.a[i];
	}
	for (int i = 0; i + 1 < maxL; ++i) {
		if (C.a[i] < 0) {
			C.a[i] += 10;
			--C.a[i + 1];
		}
	}
	return C;
}

number Square(const number& other) {
	number current;
	for (int i = 0; i < maxL; ++i) {
		current.a[i] = 0;
	}
	int l = other.len();
	for (int i = 0; i <= l; ++i) {
		for (int j = 0; j <= l; ++j) {
			current.a[i + j] += other.a[i] * other.a[j];
		}
	}

	for (int i = 0; i + 1 < maxL; ++i) {
		current.a[i + 1] += current.a[i] / 10;
		current.a[i] %= 10;
	}
	return current;
}

vector < number > buffer;

void gen(int n, int m, number& current) {
	if (m + m == n || m + m - 1 == n) {
		for (int i = 0; i < m; ++i) {
			current.a[n - 1 - i] = current.a[i];
		}
		number square = Square(current);
		if (square.isPal()) {
			buffer.push_back(current);
		}
		return ;
	}

	for (int i = (m == 0 ? 1 : 0); i < ((m == 0 || m + m + 1 == n) ? 3 : 2); ++i) {
		current.a[m] = i;
		gen(n, m + 1, current);
	}
}

int calculate(number n) {
	int left_bound = 0, right_bound = buffer.size() - 1;
	while (right_bound - left_bound > 1) {
		int middle = (left_bound + right_bound) / 2;
		if (isLess(buffer[middle], n) || Equal(buffer[middle], n)) {
			left_bound = middle;
		} else {
			right_bound = middle;
		}
	}

	int bound = -1;
	if (isLess(buffer[left_bound], n) || Equal(buffer[left_bound], n)) {
		bound = left_bound;
	}
	if (isLess(buffer[right_bound], n) || Equal(buffer[right_bound], n)) {
		bound = right_bound;
	}
	return bound + 1;
}

/*long long calculate(long long n) {
	if (n == 0) {
		return 0;
	}

	long long res = 0;
	for (long long i = 1; i * i <= n; ++i) {
		if (nice[i]) {
			++res;
		}
	}
	return res;
}*/

void solve(int test) {
	number A, B;
	A.read();
	B.read();
	number C;
	for (int i = 0; i < maxL; ++i) {
		C.a[i] = 0;
	}
	C.a[0] = 1;
	A = A - C;
	cout << "Case #" << test << ": " << calculate(B) - calculate(A) << endl;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	//precalc();

	// generates all requiered numbers in several minutes
	// after that just copy it from the file
	buffer.clear();
	/*number current;
	for (int length = 1; length <= 51; ++length) {
		for (int i = 0; i < maxL; ++i) {
			current.a[i] = 0;
		}
		gen(length, 0, current);
		cerr << length << endl;
	}

	for (int i = 0; i < buffer.size(); ++i) {
		buffer[i].print();
		printf("\n");
	}*/
	int total = 46228;
	buffer.resize(total);
	for (int i = 0; i < total; ++i) {
		buffer[i].read();
		buffer[i] = Square(buffer[i]);
	}

	int tests;
	scanf("%d\n", &tests);
	for (int i = 1; i <= tests; ++i) {
		solve(i);
		cerr << i << endl;
	}
	return 0;
}