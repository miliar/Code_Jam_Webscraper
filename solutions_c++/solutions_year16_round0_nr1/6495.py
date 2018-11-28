#define _CRT_SECURE_NO_WARNINGS
//#include <iostream>
#include <fstream>
#include <cstdio>
#include <string>
#include <cstring>
using namespace std;

ifstream cin("input.txt");
ofstream cout("output.txt");

int process(int n) {
	int result = 0;
	char buffer[70];
	for (int i = 1; i != 100000; ++i) {
		sprintf(buffer, "%d", n * i);
		int len = strlen(buffer);
		for (int j = 0; j != len; ++j) {
			int digit = buffer[j] - '0';
			result |= 1 << digit;
		}
		if (result == 0b1111111111) return n * i;
	}
	return -1;
}

int main() {
	int t;
	cin >> t;
	for (int i = 0; i != t; ++i) {
		int n;
		cin >> n;
		int res = process(n);
		if (res != -1) cout << "Case #" << i + 1 << ": " << res << endl;
		else cout << "Case #" << i + 1 << ": INSOMNIA" << endl;
	}
	return 0;
}