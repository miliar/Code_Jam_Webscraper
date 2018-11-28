#include <iostream>
#include <algorithm>
#include <array>

using namespace std;

void do_case() {
	unsigned long long N;
	cin >> N;

	if( N == 0 ) {
		cout << "INSOMNIA";
		return;
	}

	array<bool,10> seen = {false};

	unsigned int mul = 1;
	do {
		unsigned long long N2 = N*mul;
		while( N2 > 0 ) {
			seen[N2%10] = true;
			N2 /= 10;
		}

		mul += 1;
	}
	while( !all_of(seen.begin(),seen.end(),[](bool i){return i;}) );

	cout << (mul-1)*N;
}

int main() {
	unsigned int T;
	cin >> T;

	for( unsigned int i=0; i<T; ++i ) {
		cout << "Case #" << (i+1) << ": ";
		do_case();
		cout << endl;
	}
}
