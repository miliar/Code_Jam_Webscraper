#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#define MAXUS 1001
using namespace std;
int main() {
    int z,n;
    char input[MAXUS];
    scanf("%d",&z);
    for (int j = 0; j < z; j++) {
        scanf("%d", &n);
        scanf("%s",input);
        int sum = input[0] - '0' , result = 0;
        for (int i = 1; i < n+1; i++) {
            if (sum < i) {
                sum++;
                result++;
            } 
            sum += input[i] - '0';
        }
        printf("Case #%d: %d\n", j+1, result);
    }

	return 0;
}
