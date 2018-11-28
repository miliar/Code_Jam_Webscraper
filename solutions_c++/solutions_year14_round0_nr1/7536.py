#include <cstdio>
#include <iostream>

using namespace std;

int main() {
	int t, a1, a2, arr1[16], arr2[16], mask[16];
	
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	
	scanf("%d", &t);
	
	for(int cs = 1; cs <= t; ++cs) {
		scanf("%d", &a1);
		
		for(int i = 0; i < 16; ++i) {
			mask[i] = 0;
			scanf("%d", &arr1[i]);
		}
		
		scanf("%d", &a2);
		
		for(int i = 0; i < 16; ++i) {
			scanf("%d", &arr2[i]);
		}
		
		for(int i = (a1 - 1) * 4; i < a1 * 4; i++) {
			mask[arr1[i] - 1] = 1;
		}
		
		int count = 0;
		int card;
		
		for(int i = (a2 - 1) * 4; i < a2 * 4; i++) {
			if(mask[arr2[i] - 1] == 1) {
				count++;
				card = arr2[i];
			}
		}
		
		printf("Case #%d: ", cs);
		if(count == 1) {
			printf("%d\n", card);
		} else if(count == 0) {
			printf("Volunteer cheated!\n", card);
		} else {
			printf("Bad magician!\n", card);
		}
	}
	
	return 0;
}
