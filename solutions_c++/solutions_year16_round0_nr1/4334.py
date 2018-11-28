#include <stdio.h>
#include <iostream>
using namespace std;


bool allTrue(bool *arr, int size) {
	for (int i = 0; i < size; i++) {
		if (!arr[i])
			return false;
	}
	return true;
}

int main(int argc, char const *argv[])
{
	int t;
	scanf("%d", &t);
	for (int i = 0; i < t; i++) {
		int n;
		scanf("\n%d", &n);
		if (n == 0) {
			printf("Case #%d: INSOMNIA\n", i+1);
		} else { 
			bool digits[10] = {false};
			long current = 0;
			while (!allTrue(digits, 10)) {
				current += n;
				int current_copy = current;
				while (current_copy > 0) {
					digits[current_copy % 10] = true;
					current_copy /= 10;
				}
			}

			printf("Case #%d: %d\n", i+1, current);
		}
	}
	return 0;
}