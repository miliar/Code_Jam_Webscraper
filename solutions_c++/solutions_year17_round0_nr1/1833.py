#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main() {
	int numCases;
	scanf("%d", &numCases);
	
	int width;
	char cakes[1001];
	for (int i = 0 ; i < numCases ; ++i) {
	    scanf("%s %d", &cakes, &width);
	    
	    int flips = 0;
	    int cakeSize = strlen(cakes);
	    for (int j = 0 ; j <= cakeSize - width ; ++j) {
	        if (cakes[j] == '-') {
	            ++flips;
	            for (int k = j ; k < j + width ; ++k) {
	                cakes[k] = (cakes[k] == '-') ? '+' : '-';
	            }
	        }
	    }
	    
	    
	    int isImpossible = 0;
	    for (int j = cakeSize - width + 1 ; j < cakeSize ; ++j) {
	        if (cakes[j] == '-') {
	            isImpossible = 1;
	            break;
	        }    
	    }
	    
	    if (isImpossible == 1) {
	        printf("Case #%d: IMPOSSIBLE\n", i+1);
	    }
	    else {
	        printf("Case #%d: %d\n", i+1, flips);
	    }
	}
	
	
	return 0;
}
