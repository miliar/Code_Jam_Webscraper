#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <string.h>
#include <queue>
#include <stack>
#include <vector>
#include <algorithm>
#include <functional>
#include <iostream>

#define swap(a,b) ((a)^=(b)^=(a)^=(b));

using namespace std;

int i;

void func() {

	int input;
	int sheep;
	int t;
	int mul = 1;
	int save;
	bool check[10] = { false };

	scanf("%d", &input);
	if (input == 0) printf("Case #%d: INSOMNIA\n", i);
	else {
		while (1) {
			sheep = input*mul;
			save = sheep;
			mul++;
			while (sheep>0) {
				t = sheep % 10;
				sheep = sheep / 10;
				check[t] = true;
			}
			if (check[0] == true && check[1] == true && check[2] == true && check[3] == true && check[4] == true && check[5] == true && check[6] == true && check[7] == true && check[8] == true && check[9] == true) {
				printf("Case #%d: %d\n", i, save);
				break;
			}
		}
	}
}

int main() {

	int testcase;

	scanf("%d", &testcase);
	getchar();
	for (i = 1; i < testcase + 1; i++) {
		func();
	}

	return 0;

}