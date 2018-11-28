#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cassert>
#include <cstring>
using namespace std;

int main() {

	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);

	int cases;
	char cakes[101];

	cin >> cases;	
	for (int c = 1; c <= cases; c++) {
		
		scanf("%s", cakes);
		
		int flipn = 0;
		char init = cakes[0];
		for (int i = 1; i < strlen(cakes); i++) {
			if (init != cakes[i]) {
				flipn++;
				init = cakes[i];
			}
		}
		if (init != '+') 
			flipn++;
		
		printf("Case #%d: %d\n", c, flipn);

	}
	


	return 0;
}