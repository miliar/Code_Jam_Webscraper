#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "stdio.h"

#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <sstream>

int main(void) {
	FILE *file = fopen ("input.txt","r");
	int test_cases =0;
	int k =0;
	char audience[1000];

	fscanf(file,"%d",&test_cases);
	for(int cases_executed=1;cases_executed<=test_cases;cases_executed++){

		fscanf(file,"%d %s",&k, audience);

		int total = 0;
		int aux = 0;
		for(int i=0;i<k;i++) {
			aux = aux + (audience[i] - '0'); 
			if(audience[i] == '0') {
				while (aux <= i ) {
					total = total + 1;
					aux = aux + 1;
				}

			}

		}

    	printf("Case #%d: %d\n",cases_executed,total);
	}

	fclose(file);
	return 1;
}
