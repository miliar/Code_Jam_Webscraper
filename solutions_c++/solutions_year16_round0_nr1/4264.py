#include <iostream>
#include <stdio.h>
#include <string.h>
#include <limits.h>

using namespace std;

long safe_add(long a, long b) {
    if (b > 0 && a > LONG_MAX - b)
    	return -1;
    
    return a + b;
}
					 
bool flag_digit(long x, int* arr) {
	if (x < 10) {
		arr[x] = 1;
		return true;
	}
    else {
		int d = x % 10;
		arr[d] = 1;
		flag_digit(x / 10, arr);
    }
}

int main(int argc, char *args[]) {
	if (argc == 2 && strcmp(args[1], "small") == 0) {
		freopen("small.in", "r", stdin);
		freopen("small.out", "w", stdout);
	}
	else if (argc == 2 && strcmp(args[1], "large") == 0) {
		freopen("large.in", "r", stdin);
		freopen("large.out", "w", stdout);
	}
	else {
		cout << "\nPlease enter \"small\" or \"large\" test file.";
		return 0;
	}

	int T;
	cin >> T;
	for (int i=0; i<T; i++) {
        long N;
        cin >> N;
        if (N == 0)
			printf("Case #%d: %s\n", i+1, "INSOMNIA");
        else {
			long temp = 0;
			int m = 1;
			int flags[10] = {0};        
			while (N * m < LONG_MAX) {
				temp = N * m;
				flag_digit(temp, flags);
                int sum = 0;
				for (int p=0; p<10; p++) {
					sum += flags[p]; 
				}
				if (sum == 10) {
					printf("Case #%d: %ld\n", i+1, temp);
					break;
				}	
				m++;
			}
    	}
	}

	fclose(stdin);
	fclose(stdout);
	return 0;	
}	
