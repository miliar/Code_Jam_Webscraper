#include <iostream>
#include <vector>
#include <utility>
#include <string>
#include <unordered_map>
using namespace std;

long power(long base, long pow) {
	long ret = 1;
	for (int i = 0; i<pow; i++) ret *= base;
	return ret;
}

int sumDigits(long num) {
	int ret = 0;
	while (num > 0) {
		ret += num % 10;
		num /= 10;
	}
	return ret;
}
long canBeDivided(long num, int lastDigit) {
	if ((lastDigit != 1) && (lastDigit != 3) && (lastDigit != 7) && (lastDigit != 9)) {
		cout << "cannot be here" << endl;
		return -1;
	}
	//cout << "num = " << num << "  "<< "lastDigit="<< lastDigit << endl;
	long threshold = sqrt(num);
	for (long start = 0; start >= 0; start++) {
		long tmp = start*10 + 1;
		if (tmp > threshold) break;
		if (tmp != 1 && tmp <= threshold) {
			if (num % tmp == 0) return tmp;
		}
		tmp = start*10 + 3;
		if (tmp > threshold) break;
		if (tmp != 1 && tmp <= threshold) {
			if (num % tmp == 0) return tmp;
		}
		tmp = start*10 + 7;
		if (tmp > threshold) break;
		if (tmp != 1 && tmp <= threshold) {
			if (num % tmp == 0) return tmp;
		}
		tmp = start*10 + 9;
		if (tmp > threshold) break;
		if (tmp != 1 && tmp <= threshold) {
			if (num % tmp == 0) return tmp;
		}
	}
	return -1;

}
bool valid_and_output(long num, int length) {
	unordered_map<int, pair<long, long>> record;
	string str;
	for (int i = 2; i<=10; i++) record[i] = make_pair(0, 0);
	long start = 1L;
	for (int i = 0; i<length; i++) {
		if ((start & num) > 0) {
			for (int j = 2; j<=10; j++) {
				record[j].first += power(j, i);
			}
			str = "1" + str;
		} else {
			str = "0" + str;
		}
		start = start << 1;
	}
	//cout << "str = " << str << endl;

	//for (int i = 2; i<=10; i++) {
	//	cout << record[i].first << endl;
	//}
	for (int i = 2; i<=10; i++) {
		int lastDigit = record[i].first % 10;
		if (lastDigit % 2 == 0) {
			record[i].second = 2; continue;
		}
		if (lastDigit == 5) { 
			record[i].second = 5; continue;
		}
		if (sumDigits(record[i].first % 3 == 0)) {
			record[i].second = 3; continue;
		}
		auto ret = canBeDivided(record[i].first, lastDigit);
		if (ret < 0) return false;
		record[i].second = ret;
	}
	cout << str;
	for (int i = 2; i<=10; i++) {
		cout << " " << record[i].second;
	}
	cout << endl;
	return true;

}
void getResults(int length, int num) {
	long base = (1L << (length - 1)) + 1, variable = 0;
	int cnt = 0;
	while (variable <= (1L << (length - 2)) - 1) {
		long tmp = base + (variable << 1);
		auto ret = valid_and_output(tmp, length);
		//cout << "ret = " << ret << endl;
		if (ret) {
			cnt += 1;
			if (cnt == num) break;
		}
		variable += 1;
	}

}

int main() {
	//cout << canBeDivided(37, 7) << endl;
	int cases;
	cin >> cases;
	for (int i = 0; i<cases; i++) {
		int length, num;
		cin >> length >> num;
		cout << "Case #" << i+1 << ":" << endl;
		getResults(length, num);
	}
}