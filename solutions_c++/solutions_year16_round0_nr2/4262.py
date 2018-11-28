#include <iostream>
#include <string>
#include <stdio.h>
#include <stdlib.h>

using namespace std;

int flipnumber(int lengt);

int bit[101];

int main() {

	int T;
	cin >> T;

	for (int z = 1; z <= T; z++) {
		string a;
		cin >> a;
		for (int i = 0; i < a.length(); i++) {
			if (a[i] == '+') bit[i] = 1;
			else bit[i] = 0;
		}
		cout << "Case #" << z << ": " << flipnumber(a.length()) << endl;
		
	}
	return 0;
}

int flipnumber(int lengt) {
	int ret = 0;
	int i = lengt - 1;
	int symbol = bit[i];
	if (symbol == 0) ret += 1;
	i--;
	while (i >= 0){
		if (symbol != bit[i]){
			symbol = bit[i];
			ret += 1;
		}
		i--;
	}
	return ret;
}
/*
int flipnumber(int lengt)
{
	int fflip = 0;
	int i = 0, j = lengt - 1;
	while (bit[i] == 1) i++;
	if (i == 0) {
		while (bit[j] == 1) j--;
		int temp;
		for (int k = 0; k < (j + 1 / 2); k++) {
			temp = bit[i + k];
			bit[i + k] = bit[j - k];
			bit[j - k] = temp;
		}
		for (int k = 0; k <= j; k++) {
			if (bit[k] == '+') bit[k] = '-';
			else bit[k] = '+';
		}
		fflip++;
	}
	else if (i == lengt) {
		return 0;
	}
	else {
		for (int k = 0; k < i; k++) {
			bit[k] = '-';
		}
		fflip++;
		while (bit[j] == 1) j--;
		int temp;
		for (int k = 0; k < ((j - i + 1) / 2); k++) {
			temp = bit[i + k];
			bit[i + k] = bit[j - k];
			bit[j - k] = temp;
		}
		for (int k = 0; k <= j; k++) {
			if (bit[k] == '+') bit[k] = '-';
			else bit[k] = '+';
		}
		fflip++;
	}
	return flipnumber(lengt) + fflip;
}
*/