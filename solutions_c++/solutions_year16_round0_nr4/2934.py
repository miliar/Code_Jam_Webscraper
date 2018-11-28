#include <cstdio>

int main() {
    int t;
    scanf("%d", &t);
    for(int i = 0; i < t; i++) {
        int a, b, c;
        printf("Case #%d:", i + 1);
        scanf("%d %d %d", &a, &b, &c);
        for(int j = 0; j < a; j++) {
            printf(" %d", j + 1); 
        }
        puts("");
    }
}
