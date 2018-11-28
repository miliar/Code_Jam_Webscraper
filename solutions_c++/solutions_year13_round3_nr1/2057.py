/*
 * 1.cpp
 *
 *  Created on: May 12, 2013
 *      Author: yura
 */

#include <iostream>
#include <fstream>
#include <string>
using namespace std;

ofstream out;

bool isConsonant(char c) {
	return (c != 'a' && c != 'e' && c != 'i' && c != 'o' && c != 'u');
}

int findNextStart(string name, int now);
long long calcPossible(string name, int prev, int now, int n);
bool checkPossible(string name, int now, int n);
long long calcCompPossible(string name, int now, int &bias, int n);

int main() {
	int testCase;
	out.open("out.txt");
	cin >> testCase;
	for (int t = 1; t <= testCase; ++t) {
		string name;
		int n;
		cin >> name >> n;
		long long res = 0;
		int now = 0, prev = -1, bias = 1;
		if (checkPossible(name, now, n)) {
			res += calcPossible(name, prev, now, n);
			bias = 1;
			res += calcCompPossible(name, now, bias, n);
			prev = now + bias - 1;
		}
		while (now < name.size()) {
			now = findNextStart(name, now);
			if (checkPossible(name, now, n)) {
				res += calcPossible(name, prev, now, n);
				bias = 1;
				res += calcCompPossible(name, now, bias, n);
				prev = now + bias - 1;
			}
		}
		out << "Case #" << t << ": " << res << endl;
		cout << "Case #" << t << ": " << res << endl;
	}
	out.close();

}

int findNextStart(string name, int now) {
	bool flag = false;
	while (name[now] != '\0') {
		if (flag && isConsonant(name[now])) {
			return now;
		}
		if (!isConsonant(name[now])) {
			flag = true;
		}
		++now;
	}
	return now;
}

long long calcPossible(string name, int prev, int now, int n) {
	long long res;
	int beforePossible = now - prev; //set prev = -1 first
	int endPossible = name.size() - now - n + 1;
	return res = beforePossible * endPossible;
}

long long calcCompPossible(string name, int now, int &bias, int n) {
	long long res = 0;
	while(now + bias + n - 1 < name.size()) {
		if(isConsonant(name[now+bias]) && isConsonant(name[now+bias+n-1])) {
			res += name.size() - now - n + 1 - bias;
			++bias;
		}
		else {
			break;
		}

	}
	return res;

}

bool checkPossible(string name, int now, int n) {
	for (int i = 0; i < n; ++i) {
		if (now + i >= name.size())
			return false;
		if (!isConsonant(name[now + i]))
			return false;
	}
	return true;
}
