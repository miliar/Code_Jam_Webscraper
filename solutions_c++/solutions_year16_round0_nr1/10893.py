#include <iostream>
#include <cstdio>

using namespace std;

#define FORR(i, a, b) for (int i = a; i < b; ++i)
#define FOR(i, a) FORR(i, 0, a)

int main(int argc, char const *argv[]) {

	int c;
	scanf("%i", &c);

	FOR(j, c) {
		int i = 0;
		bool keep_count = true;
		int ver[10] = {0};
		int n;
		scanf("%i", &n);	
		if (n != 0) {
			while ( keep_count ) {			
				int d = n * ++i, r;
				while (d != 0) {
					r = d % 10;
					ver[r]++;
					d/= 10;
				}
				
				bool all_counted = true;

				FOR(k, 10) {
					if ( ver[k] == 0 ) { all_counted = false; break; }
				}
				keep_count = !all_counted;
			}
			printf("Case #%i: %i\n", j + 1, n * i);
		} else {
			printf("Case #%i: INSOMNIA\n", j + 1);
		}
	}
	return 0;
}