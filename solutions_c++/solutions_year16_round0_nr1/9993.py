#include <cstdio>
#include <vector>

using namespace std;

typedef unsigned int uint;

uint digits_presence = 0;

bool inc_digits(uint l) {

	while(l > 0) {
		uint dig = l%10;
		l /= 10;
		digits_presence |= (1 << dig);
	}

	// printf("digits_presence: %u\n", digits_presence);
	return digits_presence == 1023;
}

void solve(uint case_num) {

	digits_presence = 0;

	uint N, number = 0;
	scanf("%u", &N);
	
	bool START = true;

	if(N == 0) {
		START = false;
	}

	while(START) {
		number += N;
		if(inc_digits(number)) break;
	}

	if(START) printf("Case #%u: %u\n", case_num, number);
	else printf("Case #%ud: INSOMNIA\n", case_num);
}

int main() {

	uint t;
	scanf("%u", &t);
	for(uint i = 1; i <= t; i++) solve(i);

	return 0;
}