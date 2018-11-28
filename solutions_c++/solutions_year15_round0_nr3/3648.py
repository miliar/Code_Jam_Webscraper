#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "stdio.h"

#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <sstream>


char neg(char a){

	if (a == '2')
		return '1';
	if (a == 'l')
		return 'i';
	if (a == 'm')
		return 'j';
	if (a == 'n')
		return 'k';

	if (a == '1')
		return '2';
	if (a == 'i')
		return 'l';
	if (a == 'j')
		return 'm';
	if (a == 'k')
		return 'n';

	printf("Error in negative!\n");
return '!'; //should never happens
}

bool is_negative(char a) {
	return ((a == '2') || (a == 'l') || (a == 'm') || (a == 'n'));
}
char multiply(char a, char b) {
	//2 = -1
	//l = -i
	//m = -j
	//n = -k
	bool negative = false;

	if (is_negative(a)) {
		negative = true;
		a = neg(a);
	}

	//2 = -1
	//l = -i
	//m = -j
	//n = -k
	if ((a=='1') && (b=='1'))
			return negative? '2': '1';
	if ((a=='1') && (b=='i'))
			return negative? 'l':'i';
	if ((a=='1') && (b=='j'))
			return negative? 'm': 'j';
	if ((a=='1') && (b=='k'))
			return negative? 'n': 'k';
	if ((a=='i') && (b=='1'))
			return negative? 'l': 'i';
	if ((a=='i') && (b=='i'))
			return negative? '1': '2'; //-1
	if ((a=='i') && (b=='j'))
			return negative? 'n': 'k';
	if ((a=='i') && (b=='k'))
			return negative? 'j': 'm'; //-j
	if ((a=='j') && (b=='1'))
			return negative? 'm': 'j';
	if ((a=='j') && (b=='i'))
			return negative? 'k': 'n'; //-k
	if ((a=='j') && (b=='j'))
			return negative? '1': '2'; //-1
	if ((a=='j') && (b=='k'))
			return negative?  'l': 'i';
	if ((a=='k') && (b=='1'))
			return negative? 'n': 'k';
	if ((a=='k') && (b=='i'))
			return negative? 'm': 'j';
	if ((a=='k') && (b=='j'))
			return negative? 'i': 'l'; //-i
	if ((a=='k') && (b=='k'))
			return negative? '1': '2'; //-1

	printf("\nError!!!\n");
return '!';
}


char divide(char a, char b) {
//a div XXX = b

	//2 = -1
	//l = -i
	//m = -j
	//n = -k
	bool negative = false;

	if ((is_negative(a) && (is_negative(b)))) {
		a = neg(a);
		b = neg(b);
	} else {
		if (is_negative(a)) {
			a = neg(a);
			negative = true;
		}
		if (is_negative(b)) {
			b = neg(b);
			negative = true;
		}
	}
	//2 = -1
	//l = -i
	//m = -j
	//n = -k
	if ((a=='1') && (b=='1'))
			return negative? '1': '2';
	if ((a=='1') && (b=='i'))
			return negative? 'i':'l';
	if ((a=='1') && (b=='j'))
			return negative? 'j': 'm';
	if ((a=='1') && (b=='k'))
			return negative? 'k': 'n';
	if ((a=='i') && (b=='1'))
			return negative? 'i': 'l';
	if ((a=='i') && (b=='i'))
			return negative? '1': '2'; //-1
	if ((a=='i') && (b=='j'))
			return negative? 'n': 'k';
	if ((a=='i') && (b=='k'))
			return negative? 'j': 'm'; //-j
	if ((a=='j') && (b=='1'))
			return negative? 'j': 'm';
	if ((a=='j') && (b=='i'))
			return negative? 'k': 'n'; //-k
	if ((a=='j') && (b=='j'))
			return negative? '1': '2'; //-1
	if ((a=='j') && (b=='k'))
			return negative?  'l': 'i';
	if ((a=='k') && (b=='1'))
			return negative? 'k': 'n';
	if ((a=='k') && (b=='i'))
			return negative? 'm': 'j';
	if ((a=='k') && (b=='j'))
			return negative? 'i': 'l'; //-i
	if ((a=='k') && (b=='k'))
			return negative? '1': '2'; //-1

	printf("\nError!!!\n");
return '!';
}

int main(void) {
	FILE *file = fopen ("input.txt","r");
	int test_cases =0;
	int L =0;
	int X=0;
	char str[10001];

	fscanf(file,"%d",&test_cases);
	for(int cases_executed=1;cases_executed<=test_cases;cases_executed++){

		fscanf(file,"%d",&L);
		fscanf(file,"%d",&X);
		fscanf(file,"%s",str);

		char total_mult = '1';
		for(int i=0;i<L*X;i++) {
			str[i] = str[i%L];
			total_mult = multiply(total_mult, str[i]);
		}
		str[L*X] = '\x0';

		char itimesj = multiply('i', 'j');



		bool found = false;
		char curr = '1';
		int subi = 0;

		while ((!found) && (subi < (L*X))) {

			for(subi=0;subi<(L*X) && (!found);subi++) {
				curr = multiply(curr, str[subi]);
				if(curr == 'i' ) {
					curr = '1';
					for(int j=subi+1;j<(L*X) && (!found);j++) {
						curr = multiply(curr, str[j]);

						if(curr == 'j') {
							curr = divide(itimesj, total_mult);
							if (curr == 'k')
								found = true;
							curr = 'j';
						}
					}
					curr = 'i';
				}

			}
		}

		printf("Case #%d: %s\n",cases_executed,found? "YES" : "NO");

	}

	fclose(file);
	return 1;
}

