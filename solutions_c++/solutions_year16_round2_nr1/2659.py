#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include <ctype.h>

#include <iostream>

int findchar(char* str, char ch) {
	int i = 0;
	while (str[i]) {
		if (str[i] == ch) {
			str[i] += 32;
			return 1;
		}
		i++;
	}
	return 0;
}

void delchar(char* str) {
	int i = 0;
	while (str[i]) {
		if (islower(str[i])) {
			str[i] = 1;
		}
		i++;
	}
}

void upchar(char* str) {
	int i = 0;
	while (str[i]) {
		if (islower(str[i])) {
			str[i] -= 32;
		}
		i++;
	}
}

int main(void) {
	int T;

	//input var//
	char S[2001];
	/////////////

	//var//
	int result[10];
	int i, j;
	int digit;
	char* table[] = {
		"ZERO","ONE","TWO","THREE","FOUR","FIVE","SIX",
		"SEVEN","EIGHT","NINE"
	};
	int table2[] = {
		0,2,6,8,7,5,4,1,3,9
	};
	///////

	std::cin >> T;
	for (int _t = 1; _t <= T; _t++) {
		//input//
		std::cin >> S;
		/////////

		//process//
		for (i = 0; i < 10;i++) result[i] = 0;
		for (i = 0; i < 10;) {
			digit = table2[i];
			for (j = 0;; j++) {
				if (table[digit][j]) {
					if (!findchar(S, table[digit][j])) {
						upchar(S);
						i++;
						break;
					}
				}
				else {
					delchar(S);
					result[digit]++;
					break;
				}
			}
		}
		///////////

		std::cout << "Case #" << _t << ": ";
		//output//
		for (i = 0; i < 10; i++) {
			while (result[i]) {
				std::cout << i;
				result[i]--;
			}
		}
		//////////
		std::cout << std::endl;
	}

	return 0;
}