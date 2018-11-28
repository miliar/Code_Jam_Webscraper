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
	
	int t, tst, i, k, ma = 0, j, n, f;
	char s[101], d;
	unsigned long long rez, y, x;
	scanf("%d", &tst);
	
	for(t = 0; t < tst; t++) {
		scanf("%s", s);
		n = strlen(s);

		k = f = (s[0] == '-');
		for (i = 1; i < n; i++) {
			if (s[i] == '-' && s[i]!=s[i-1])
				k++;		
		}

		k += k;					
		if (f)
			k--;
		
		printf("Case #%d: %d\n", t+1, k);

	}

	return 0;
}
