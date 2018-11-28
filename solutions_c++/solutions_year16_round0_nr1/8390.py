#include <cstdio>

int v[10];

void update(int n) {
    while (n > 0) {
        v[n % 10] = 1;
        n = n / 10;
    }
}

int main() {
    int a, n;
    scanf("%d", &a);
    int cas = 1;
    for (int i = 0; i < a; i++) {
        scanf("%d", &n);
        for (int j = 0; j < 10; j++)
            v[j] = 0;
        bool found;
        int e;
        for (int j = 1; j < 500; j++) {
            e = n * j;
            update(e);
            found = true;
            for (int k = 0; k < 10; k++)
                if (!v[k])
                    found = false;
            if (found)
                break;
        }
        if (found)
            printf("Case #%d: %d\n", cas, e);
        else
            printf("Case #%d: INSOMNIA\n", cas);
        cas++;
    }
    
    return 0;
}
