#include <cstdio>


int main(int argc, char **argv) {

	unsigned T;
	scanf("%u",&T);
	for (unsigned i=0; i<T; ++i) {
		char pancakes[101];
		scanf("%s",pancakes);
		int j = 0;
		int changes = 0;
		while(pancakes[j+1]) {
			if (pancakes[j] != pancakes[j+1]) {
				++changes;
			}
			++j;
		}
		int turns = changes;
		if (pancakes[j] == '-') {
		    ++turns;
		}

		printf("Case #%u: %d\n",i+1,turns);
	}

	return 0;
}




