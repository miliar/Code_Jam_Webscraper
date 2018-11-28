#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <iostream>
#include <cmath>
#include <algorithm>

using namespace std;

int main(void) {
	int num_cases;
	
	cin >> num_cases;
	
	long N, P;
	int first_zero_bit, wins_bit;
	long po, g, c;
	for (int case_num=1; case_num<=num_cases; case_num++) {
		cin >> N >> P;
		
		if (P == (1<<N)) {	//everyone wins
			g = (1<<N)-1;
			c = g;
		}
		else {
			P--;
			first_zero_bit = N-1;
			po = 2;
			while (((P>>first_zero_bit)&1) && first_zero_bit>0) {
				first_zero_bit--;
				po *= 2;
			}
			g = po - 2;
			
			P++;
			wins_bit = N-1;
			po = 2;
			while (((P>>wins_bit)&1)==0 && wins_bit>0) {
				wins_bit--;
				po *= 2;
			}
			c = (1<<N)-po;
		}
	
		printf("Case #%d: ", case_num);
		printf("%ld %ld\n", g, c);
	}

	return 0;
}