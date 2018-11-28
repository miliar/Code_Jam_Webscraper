#include <stdio.h>
#include <math.h>
#include <iostream>
#include <fstream>

int get_digits(int n) {
    return floor(log10(abs(n))) + 1;
}

void sheep(int n, int max) {
    
    int digits;
    int current;
    bool check[10];
    bool check_all;
    
    for (int i = 0; i < 10; i++) {
        check[i] = false;
    }
    if (n != 0) {
    for (int i = 1; n * i < max; i++) {
        current = n * i;
        digits = get_digits(current);
        //printf("%d\n", current);
        for (int j = 0; j < digits; j++) {
            check[(current / (int)pow(10, j)) % 10] = true;
        }
        check_all = true;
        for (int i = 0; i < 10; i++) {
            if (check[i] == false) {
                check_all = false;
                break;
            }
        }
        if (check_all) {
            printf("%d\n", current);
            return;
        }
    }
    }
    printf("INSOMNIA\n");
}

int main(int argc, const char * argv[]) {
    int n, max;
    std::cin >> max;
    for(int i = 0; i < max; ++i)
    {
        std::cin >> n;
        printf("Case #%d: ", i + 1);
        sheep(n, 2147483647 - n);
    }
    return 0;
}



