#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>

using namespace std;

int Case = 1, tc = 0, n = 0, j = 0;
vector<long long> nums;
void generate(long long currentNum, int size) {

	if (size == 0) {
		nums.push_back(currentNum);
		return;
	}
	generate(currentNum * 10L + 1L, size - 1);
	generate(currentNum * 10L, size - 1);
}
long long convertToDicimal(long long n, int radix) {

	long long res = 0, pow = 1;
	int i = 0;
	while (n) {
		int x = n % 10;
		res += x * pow;
		i++;
		n /= 10;
		pow *= radix;
	}
	return res;
}
long long getDivisor(long long num) {
	int sqrtN = (int) sqrt((double) num);
	for (int i = 2; i <= sqrtN; i++) {
		if (num % i == 0)
			return i;
	}
	return -1;
}
vector<int> divisors;
bool checkJamCoin(long long num) {
	divisors.clear();
	for (int r = 2; r <= 10; r++) {

		long long n = convertToDicimal(num, r);
		long long res = getDivisor(n);
		if(res == -1)
			return false;
		divisors.push_back(res);
	}

	return true;
}

int main() {
	freopen("test.in", "rt", stdin);
	freopen("test.out", "w", stdout);

	cin >> tc;

	while (tc--) {
		cin >> n >> j;
		cout << "Case #" << Case++ << ":" << endl;

		generate(1, n - 2);

		for (int i = 0; i < (int) nums.size(); i++) {
			nums[i] = nums[i] * 10 + 1;
		}
		int requiredNum = 0;

		for (int i = nums.size() - 1; i >= 0; i--) {
			bool res = checkJamCoin(nums[i]);

			if (res) {
				cout << nums[i] << " ";
				for (int x = 0; x < (int) divisors.size(); x++) {
					if (x) {
						cout << " ";
					}
					cout << divisors[x];
				}
				cout << endl;
				requiredNum++;
				if (requiredNum == j) {
					break;
				}
			}

		}

	}
	return 0;
}
//By : mohamed waleed
