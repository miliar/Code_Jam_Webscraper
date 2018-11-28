#include "stdafx.h"
#include <iostream>
using namespace std;


int main()
{
	char *s[] = { "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE" };
	char *order = "ZWUGFRXSIN";
	int digit[10] = { 0,2,4,8,5,3,6,7,9,1 };
	int t;
	cin >> t;
	char s2[10000];
	for (int i = 0; i < t; i++) {
		cin >> s2;
		cout << "Case #" << i + 1 << ": ";
		int count[127];
		int digitCount[10];
		memset(count, 0, sizeof(int) * 127);
		memset(digitCount, 0, sizeof(int) * 10);
		for (int j = 0; j < strlen(s2); j++)
			count[s2[j]]++;
		for (int j = 0; j < 10; j++) {
			int c = count[order[j]];
			digitCount[digit[j]] = c;
			char *w = s[digit[j]];
			for (int k = 0; k < strlen(w); k++)
				count[w[k]] -= c;
		}
		for (int j = 0; j < 10; j++) {
			for (int k = 0; k < digitCount[j]; k++)
				cout << j;
		}
		cout << endl;
	}
	return 0;
}

