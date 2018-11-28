#include <iostream>
#include <stdio.h>
#include <string>
#include <math.h>
#include <vector>
#include <stdlib.h>

using namespace std;

char flip(char a){
	if (a == '+') {
		return '-';
	}
	else {
		return '+';
	}
}


int compare (const void * a, const void * b)
{
	return ( *(int*)a - *(int*)b );
}

void * solve(){
	void * ans;
	string row;
	int i = 0, j, k, flo = 0, le;
	
	cin >> row >> k;
	le = row.length();
	
	while (i + k - 1 < le) {
		if (row[i] == '-') {
			flo++;
			for (j = 0; j < k; j++) {
				row[i+j] = flip(row[i+j]);
			}
		}
		i++;
	}
	
	while (i < le) {
		if (row[i] == '-') {
			i = le + 1;
		}
		i++;
	}
	
	if (i == le) {
		cout << flo;
	}
	else {
		cout << "IMPOSSIBLE";
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