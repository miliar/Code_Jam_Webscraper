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

void move01 (string & test) {
	
	if (test[0] == '0') {
		test[0] = '1';
		test[1] = '1';
	}
	else {
		int i = 0;
		while (test[i] == '1') {
			test[i] = '0';
			test[i + 1] = '0';
			i = i + 2;
		}
		test[i] = '1';
		test[i + 1] = '1';
	}
}

void * solve(){
	void * ans;
	int len, quant, i;
	scanf("%d %d", &len, &quant);
	
	i = (len - 4)/2;
	if (log2(quant) > i) {
		printf("YOU DONE GOOF!");
		return ans;
	}
	
	string ani = "";
	ani.resize(len - 4, '0');
	for (i = 0; i < quant; i++) {
		printf("11%s11 3 4 5 6 7 8 9 10 11\n", ani.c_str());
		move01(ani);
	}
	return ans;
}



int main (int argc, char * const argv[]) {
    int ncases, cases;
	scanf("%d\n", &ncases);
	for (cases = 0; cases < ncases; cases++) {
		cout << "Case #" << cases + 1 << ":\n";
		solve();
		cout << endl;
	}
    return 0;
}
