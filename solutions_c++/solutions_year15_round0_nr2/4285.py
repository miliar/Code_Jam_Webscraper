#pragma warning(disable:4996)
#include <stdio.h>
void printTestcase(int x, int y){
	printf("Case #%d: %d\n", x, y);
}
int main(){
	int t;
	scanf("%d", &t);
	for (int i = 0; i < t; ++i){
		int d;
		scanf("%d", &d);
		int pancake[1000] = { 0 };
		int temp[1000] = { 0 };
		int max = 0;
		for (int j = 0; j < d; ++j){
			scanf("%d", &pancake[j]);
			temp[j] = pancake[j];
			if (pancake[j] > max){
				max = pancake[j];
			}
		}
		int minute;
		int MIN = 0x7fffffff;
		for (int div = 1; div <= max; ++div){
			minute = 0;
			for (int j = 0; j < d; ++j){
				while (pancake[j] > div){
					pancake[j] -= div;
					++minute;
				}
				pancake[j] = temp[j];
			}
			minute += div;
			if (minute < MIN){
				MIN = minute;
			}
		}
		printTestcase(i + 1, MIN);
	}
	return 0;
}