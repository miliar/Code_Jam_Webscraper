// GCJ.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"


#include <iostream>
#include <cstring>
using namespace std;
#define MX 1001
int main()
{
	int T;
	cin >> T;
	for (int c = 1; c <= T; c++) {
		char s[MX];
		int k;
		cin >> s >>k;
		int ret = 0;
		int len = strlen(s);
		for (int i = 0; i < len; i++) {
			if (s[i] == '-') {
				ret++;
				if (i + k > len) {
					ret = -1;
					break;
				}
				for (int j = i; j < i + k; j++) {
					if (s[j] == '+')
						s[j] = '-';
					else
						s[j] = '+';
				}
			}
		}
		cout << "Case #" << c << ": ";
		if(ret == -1) {
			cout << "IMPOSSIBLE" <<endl;
		}
		else {
			cout << ret << endl;
		}
	}

    return 0;
}

