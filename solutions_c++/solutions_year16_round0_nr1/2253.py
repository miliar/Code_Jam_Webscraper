#include <cstdio>

void process(bool found[], int& num, int x) {
    while(x) {
        if(!found[x % 10]) {
            num++;
            found[x % 10] = true;
        }
        x /= 10;
    }
}

int calculate_last_number(int x) {
    bool found[10] = {0};
    int num = 0;
    int current = 0;
    do {
        current += x;
        process(found, num, current);
    }
    while(num < 10);
    return current;
}

int main() {
    int T,x;
    scanf("%d", &T);
    for(int i = 1; i <= T; i++) {
        scanf("%d", &x);
        printf("Case #%d: ", i);
        x == 0 ? printf("INSOMNIA\n") : 
                 printf("%d\n", calculate_last_number(x));
    }
    return 0;
}