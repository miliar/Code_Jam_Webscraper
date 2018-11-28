#include <stdio.h>
#include <stdlib.h>

unsigned char cards[4][4];
unsigned char cards_two[4][4];

int main() {
	unsigned t, s_max;
	scanf("%d\n", &t);
	for (unsigned i = 0; i < t; ++i) {
		scanf("%d ", &s_max);
		unsigned *shy_array = (unsigned *) malloc(sizeof(unsigned) * s_max + 1);
		
		for(unsigned j = 0; j < s_max + 1; j++) {
			char shyness;
			scanf("%c",  &shyness);
			shy_array[j] = shyness - '0';
		}

		unsigned standing = 0;
		unsigned invited = 0;
		for(unsigned j = 0; j < s_max + 1; j++) {
			if(j <= standing) {
				standing += shy_array[j];
			}
			else {
				invited += j - standing;
				standing += j - standing + shy_array[j];
			}
		}
		printf("Case #%d: %d \n", i + 1, invited);
		free(shy_array);
	}

	return 0;

}