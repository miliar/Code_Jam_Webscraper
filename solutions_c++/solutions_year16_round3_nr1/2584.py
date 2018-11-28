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
	char letters[27];
	int parties[28];
	int i, par, m1, m2, i1, i2, go, sum;
	for (i = 0; i < 26; i++) {
		letters[i] = 'A' + i;
	}
	
	cin >> par;
	parties[0] = 0;
	for (i = 1; i < par + 1; i++) {
		cin >> parties[i];
	}


	go = 0;
	
	while (go == 0) {
		i1 = 0;
		i2 = 0;
		m1 = 0;
		m2 = 0;
		sum = 0;
		
		for (i = 1; i < par + 1; i++) {
			if (parties[i] > 0) {
				if (parties[i] >= m1) {
					m2 = m1;
					i2 = i1;
					i1 = i;
					m1 = parties[i];
				}
				else {
					if (parties[i] >= m2) {
						m2 = parties[i];
						i2 = i;
					}
				}
				sum++;
			}
		}
		
		if (sum == 3 && parties[i2] == 1) {
			parties[i1]--;
			printf("%c ", letters[i1 - 1]);
		}
		else {
			if (sum == 2 && parties[i1] == 1) {
				parties[i1]--;
				parties[i2]--;
				printf("%c%c", letters[i1 - 1], letters[i2 - 1]);
				go = 1;
			}
			else {
				parties[i1]--;
				parties[i2]--;
				printf("%c%c ", letters[i1 - 1], letters[i2 - 1]);
			}
		}
		
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
