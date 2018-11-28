#include <iostream>
#include <stdio.h>
#include <string>
#include <math.h>
#include <vector>
#include <stdlib.h>

using namespace std;

int compare (const void * a, const void * b)
{
	return ( *(int*)a - *(int*)b );
}

void * solve(){
	void * ans;
	int d, i, j, d1, d2, seen, l;
	int appear[10];
	scanf("%d\n", &d);
	if (d == 0) {
		printf("INSOMNIA");
	}
	else {
		for (i=0; i < 10; i++) {
			appear[i] = 0;
		}
		seen = 0;
		for (j = 1; seen < 10; j++) {
			d1 = j * d;
			d2 = d1;
			for (i = 0; d2 > 0; i++) {
				l = d2%10;
				if (appear[l] == 0) {
					seen++;
					appear[l] = 1;
				}
				d2 = (d2 - l)/10;
			}
		}
		cout << d1;
	}
	return ans;
}


int main (int argc, char * const argv[]) {
    int ncases, cases;
	scanf("%d\n", &ncases);
	for (cases = 0; cases < ncases; cases++) {
		cout << "Case #" << cases + 1 << ": ";
		solve();
		cout << endl;
	}
    return 0;
}
