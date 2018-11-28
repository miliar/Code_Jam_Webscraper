#include <stdio.h>
#include <stdlib.h>

#ifndef COUNT_ARRAY_SIZE
#define COUNT_ARRAY_SIZE 10
#endif

void foreach_print(int *arr, int size) {
    for(int i = 0; i < size; i++)
        printf("%d\n", arr[i]);
}

bool Ok(bool arr[][COUNT_ARRAY_SIZE], int n) {
    for(int i = 0; i < COUNT_ARRAY_SIZE; i++) {
        if(arr[n][i] == false)
            return false;
    }


    return true;
}

void print_infinite(int order, FILE *file) {
    fprintf(file, "Case #%d: INSOMNIA\n", order + 1);
}

void print_result(int order, int res, FILE *file) {
    fprintf(file, "Case #%d: %d\n", order + 1, res);
}

int main() {
    int n = 0;
    FILE *file = fopen("A-large.in", "r");
    if (file != NULL) {
    	fscanf(file, "%d", &n); // numbers
	}
    
    int arr[n];
    for(int i = 0; i < n; i++)
        fscanf(file, "%d", &arr[i]);
    fclose(file);
    bool done[n][COUNT_ARRAY_SIZE] = {false};
    
    FILE *out = fopen("A-large.out", "w+");

    for(int i = 0; i < n; i++) {
        switch (arr[i]) {
            case 0:
                print_infinite(i, out);
                break;
            default:
                    int initial = arr[i];
                do {
                    int tmp1 = arr[i];

                    while(tmp1) {
                        done[i][tmp1 % 10] = true;
                        tmp1 /= 10;
                    }
                    arr[i] += initial;
                } while(!Ok(done, i));
                
                print_result(i, (arr[i] - initial), out);
        }
    }
    fclose(out);

    return 0;
}
