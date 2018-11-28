#include <iostream>
#include <stdio.h>

using namespace std;

long long firstmeet(long long );

int main() {

	int T;
	cin >> T;

	for (int z = 1; z <= T; z++) {
		long long N;
		cin >> N;
		cout << "Case #" << z << ": ";
		if (N == 0) {
			cout << "INSOMNIA" << endl;
		}
		else {
			printf("%ld\n", firstmeet(N));
		}
	}
	return 0;
}

long long firstmeet(long long N)
{
	long long numb = 0;
	int bitmask = 0;
	int meet_bitmask = 1023;
	while (bitmask != meet_bitmask){
		numb += N;
		long long temp = numb;
		while (temp != 0) {
			bitmask |= (1 << (temp % 10));
			temp /= 10;
		}
	}
	return numb;
}