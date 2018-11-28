#include<cstdio>

bool zero(bool tab[]) {
    for (int i = 0; i < 10; ++i) 
        tab[i] = false;
}

bool check(bool tab[]) {
    bool response = true;
    for (int i = 0; i < 10; i++) {
        if (!tab[i])
            response = false;
    }
    return response;
}

void update(bool tab[], int x) {
    int aux;
    while(x != 0) {
        aux = x % 10;
        x /= 10;
        tab[aux] = true;
    }
}

int main() {
    int n, x;
    bool numbs[15];
    scanf("%d", &n);
    for (int i = 1; i <= n; ++i) {
        zero(numbs);
        scanf("%d", &x);
        int firstx = x;
        if(x == 0) {
            printf("Case #%d: INSOMNIA\n", i);
            continue;
        }
        while(true) {
            update(numbs, x);
            if (check(numbs)) {
                printf("Case #%d: %d\n", i, x);
                break;
            }
            x += firstx;
        } 
    }
}
