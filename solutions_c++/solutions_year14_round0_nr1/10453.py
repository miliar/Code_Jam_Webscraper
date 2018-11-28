#include <iostream>
#include <map>
#include <stdlib.h>
#include <string>

using namespace std;

int main() {
	int cases = 0;
	int test = 0;
	int row;
	map<int,int> store;
	string line;
	scanf("%d", &test);
	while(test--) {
		cases++;
		store.clear();
		int count = 0;
		int temp, number = 0;
		scanf("%d", &row);
		/* check the first ordering of cards */
		for(size_t i = 0; i < 4; i++) {
			/* code */
			for (int j = 0; j < 4; j++) {
				scanf("%d", &temp);
				
				if (i+1 == row) {
					if (!store[temp]) {
						store[temp] = 1;
					}
				}
			}
			
		}
		
		/* check the second ordering of cards */
		scanf("%d", &row);
		for(size_t i = 0; i < 4; i++) {
			/* code */
			for(size_t j = 0; j < 4; j++) {
				/* code */
				scanf("%d", &temp);
				if (i+1 == row) {
					if(store[temp]) {
						count++;
						number = temp;
					}
				}
			}
			
		}
		
		/* Print the results */
		if (count == 1) {
			/* code */
			printf("Case #%d: %d\n", cases, number);
		} else if (count > 1) {
			printf("Case #%d: %s", cases , "Bad magician!\n");
		} else if (count == 0) {
			printf("Case #%d: %s", cases, "Volunteer cheated!\n");
		}
		
	}
	
	
	return 0;
}
