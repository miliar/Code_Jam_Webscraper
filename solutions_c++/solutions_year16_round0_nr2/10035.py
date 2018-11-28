#include <cstdio>
#include <cstdlib>
#include <cstring>

#ifndef DATA_LENGTH
#define DATA_LENGTH 100
#endif

void swap(char *cake) {
	if(*cake == '+')
		*cake = '-';
	else
		*cake = '+';
}

int main() {
	
	int n = 0;
    FILE *file = fopen("B-small-attempt0.in", "r");
    if (file != NULL) {
    	fscanf(file, "%d", &n); // numbers
    	//printf("size:%d\n", n);
	}
	
	char arr[n][DATA_LENGTH];
    for(int i = 0; i < n; i++)
        fscanf(file, "%s", arr[i]);
        
    fclose(file);
	
	int pc[n] = {0};
	
	for(int i = 0; i < n; i++) {
		int s = strlen(arr[i]);
		for(int j = s - 1; j >= 0; j--) {
			if (arr[i][j] == '-') {
				for(int k = j; k >= 0; k--) {
					swap(&arr[i][k]);
				}
				pc[i]++;
			}
		}
	}
	
	FILE *out = fopen("2.out", "w+");
	
	for(int i = 0; i < n; i++) {
		fprintf(out, "Case #%d: %d\n", i + 1, pc[i]);
	}
	fclose(out);
	
	return 0;
}
