#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#define MAX 101
using namespace std;  // since cin and cout are both in namespace std, this saves some text

char hold[MAX] = {'\000'};

int sol() {
	unsigned int flips = 0;
	unsigned int i = 0;
	unsigned char state = 0;

	state = hold[0] == '+' ? 0 : 1;

	while (hold[++i] != '\0')
		if (state) {
			if (hold[i] == '+') {
				++flips;
				state = 0;
			}
		} else {
			if (hold[i] == '-') {
				++flips;
				state = 1;
			}
		}

	return state ? flips + 1: flips;
}

int main() {
	unsigned int t;
	cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
	for (int i = 1; i <= t; ++i) {
		scanf("%s", hold);
		printf("Case #%d: %d\n", i, sol());
	}
	return 0;
}
