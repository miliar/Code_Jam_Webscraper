#include <iostream>
#include <vector>
#include <unordered_set>
using namespace std;

bool isFull(unordered_set<int> &checker) {
	for (int i = 0; i<=9; i++) {
		if (checker.find(i) == checker.end()) return false;
	}
	return true;
}

void fill(long tmp, unordered_set<int>&checker) {
	while (tmp > 0) {
		int remain = tmp % 10;
		tmp = tmp / 10;
		checker.insert(remain);
	}
}

long getResult(long start) {
	if (start == 0) return -1;
	unordered_set<int> checker;
	long tmp, cnt = 1;
	while (tmp >= 0) {
		tmp = start*cnt;
		fill(tmp, checker);
		if (isFull(checker)) return tmp;
		cnt += 1; 
	}
	return -1;
}

int main() {
	int cases;
	cin >> cases;
	for (int i = 0; i<cases; i++) {
		int N;
		cin >> N;
		long ret = getResult(N);
		if (ret == -1) 
			cout << "Case #" << i + 1 << ": " << "INSOMNIA" << endl;
		else cout << "Case #" << i + 1 << ": " << ret << endl;
	}
}