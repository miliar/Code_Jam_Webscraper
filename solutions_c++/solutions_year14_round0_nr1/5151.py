#include <iostream>
#include <cstdio>
#define lli long long int
using namespace std;

int main() {
	// your code goes here
	lli tcase,li,a1,a2,val,arr1[4][4],arr2[4][4],i,j,k,count;
	
	scanf("%lld", &tcase);
	
	for (li = 1; li <= tcase; ++li) {
		scanf("%lld", &a1);
		
		for (i = 0; i < 4; ++i) {
			for (j = 0; j < 4; ++j) {
				scanf("%lld", &arr1[i][j]);
			}
		}
		
		scanf("%lld", &a2);
		
		for (i = 0; i < 4; ++i) {
			for (j = 0; j < 4; ++j) {
				scanf("%lld", &arr2[i][j]);
			}
		}
		
		count = 0;
		
		for (j = 0; j < 4; ++j) {
			for (k = 0; k < 4; ++k) {
				if (arr1[a1-1][j] == arr2[a2-1][k]) {
					++count;
					val = arr1[a1-1][j];
				}
			}
		}
		
		if (count == 1)
			printf("Case #%lld: %lld\n", li, val);
		else if (count > 1)
			printf("Case #%lld: Bad magician!\n", li);
		else
			printf("Case #%lld: Volunteer cheated!\n", li);
	}
	return 0;
}