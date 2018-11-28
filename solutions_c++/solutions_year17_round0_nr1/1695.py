#include <iostream>
#include <algorithm>
#include <cstring>
#include <vector>
#include <stdio.h>
using namespace std;
int tc, k;
char arr[1006];
int main(){
	freopen("A-large.in", "r", stdin);
	freopen("Aoutlarge.txt", "w", stdout);
	scanf("%d", &tc);
	for (int i = 0; i < tc; i++){
		scanf(" %s", &arr);
		scanf("%d", &k);
		int lenn = strlen(arr);
		int counter = 0;
		for (int j = 0; j < lenn; j++){
			if (arr[j] == '+') continue;
			if (j > lenn - k){
				counter = -1;
				break;
			}
			counter++;
			for (int kk = j; kk < j + k; kk++){
				if (arr[kk] == '-'){
					arr[kk] = '+';
				} else {
					arr[kk] = '-';
				}
			}
		}
		if (counter == -1) printf("Case #%d: IMPOSSIBLE\n", i + 1);
		else printf("Case #%d: %d\n", i + 1, counter);
	}
}
