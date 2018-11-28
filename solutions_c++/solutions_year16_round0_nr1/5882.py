#include <iostream>
#include <fstream>
#include <vector>
#include <stdlib.h>
#include <string.h>

using namespace std;

bool myfunction (pair<int, int> i,pair<int, int>j) { 
	return (abs(i.first) < abs(j.first)); 
}



int main() {
	
	int t, tst, i, k, ma = 0, j;
	char cif[10], d;
	unsigned long long rez, y, n, x;
	scanf("%d", &tst);
	
	for(t = 0; t < tst; t++) {
		scanf("%llu", &n);
		if (!n) {
			printf("Case #%d: INSOMNIA\n", t+1);
			continue;		
		}
					
	
		k = 0;	
		memset(cif, 0, sizeof(cif));
		x = 0;
		while (k < 10) {
			x += n;
			y = x;
			while (y) {
				d = y%10;
				y = y/10;
				if (!cif[d]) {
					k++;
					cif[d]++;				
				}			
			}
			
		}
		ma = max(ma, i);
		printf("Case #%d: %llu\n", t+1, x);

	}

	return 0;
}
