#include "codejam.h"
#include "iostream"
#include "algorithm"
#include "cstring"

using namespace std;

typedef long long ll;

const size_t LIMIT = 800+5;
int N;
bool digit_found[17];

bool init(/* arguments */) {
	/* code */
	return 0;
}

bool read_input(/* arguments */) {
	/* code */
	cin >>N;
	memset(digit_found, false, sizeof digit_found);
	return true;
}

string solve(/* arguments */) {
	/* code */
	if(N == 0) {
		return "INSOMNIA";
	}
	int i{1}, cnt{0}, n{N};
	while( cnt < 10 ) {
		n = N*i;
		while( n != 0 ) {
			if(digit_found[ n%10 ] == false ) {
				cnt++;
			}
			digit_found[ n%10 ] = true;
			n /= 10;
		}
		i++;
	}
	return to_string((i-1)*N);
}
