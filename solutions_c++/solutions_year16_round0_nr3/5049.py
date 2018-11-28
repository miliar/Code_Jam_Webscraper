#include<iostream>
#include<string>
#include<stdlib.h>

using namespace std;

//unsigned long long jamcoins[1000];

string binary[524288];

unsigned long id = -1;

char set[2] = { '0' , '1' };

void GenerateBinary(string prefix, int len) {
	if (len == 0) {
		int l = prefix.length();
		if (prefix[0] == '1' && prefix[l - 1] == '1')
			binary[++id] = prefix;
		return;
	}
	for (int i = 0; i < 2; ++i) {
		string newprefix = prefix + set[i];
		GenerateBinary(newprefix, len - 1);
	}
}

bool IsPrime(unsigned long long n, unsigned long long &div) {
	unsigned long long i = 0, sqn = sqrt(n);
	bool flag = true;
	for (i = 2; i <= sqn; ++i)
		if (n%i == 0) {
			div = i;
			flag = false;
			break;
		}

	return flag;
}

int main() {
	int tcase, lenJC, numJC;
	cin >> tcase;
	cin >> lenJC;
	cin >> numJC;

	cout << "Case #1: " << endl;

	GenerateBinary("", lenJC);

	int num = 0;
	for (unsigned long i = 0; i < id; i++) {
		bool valid = true;
		unsigned long long alldiv[9] = { 0 };
		for (int b = 2; b <= 10; b++) {
			unsigned long long div = 0;
			unsigned long long conv = stoull(binary[i], 0, b);
			if (IsPrime(conv, div)) {
				valid = false;
				break;
			}
			else
				alldiv[b - 2] = div;
		}
		if (valid) {
			num++;
			cout << binary[i] << " ";
			for (int j = 0; j < 9; j++)
				cout << alldiv[j] << " ";
			cout << endl;
		}
		if (num == numJC)
			break;
	}
	return 0;
}