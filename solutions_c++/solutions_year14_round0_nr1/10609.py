#include<stdio.h>
#include<stdlib.h>
int main () {
    int t;
    scanf("%d", &t);
    for (int lo = 1; lo <= t; lo++) {
        int l;
        int a;
        scanf("%d", &l);
        int v[10];
        for (int c = 1; c <= 4; c++) {
            for (int g = 1; g <= 4; g++) {
                scanf("%d", &a);
                if (l == c) {
                    v[g] = a;
                }
            }
        }
        scanf("%d", &l);
        int res = 0;
        for (int c = 1; c <= 4; c++) {
            for (int g = 1; g <= 4; g++) {
                scanf("%d", &a);
                if (l == c) {
                    for (int i = 1; i <= 4; i++) {
                        if (v[i] == a) {
                            if (res == 0) res = a;
                            else res = -1;
                        }
                    }
                }
            }
        }
        printf("Case #%d: ", lo);
        if (res == 0) printf("Volunteer cheated!\n");
        else if (res == -1) printf("Bad magician!\n");
        else printf("%d\n", res);
    }
    return 0;
}
    
