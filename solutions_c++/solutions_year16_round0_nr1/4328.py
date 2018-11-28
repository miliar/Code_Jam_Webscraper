#include <iostream>
#include <cstdio>
using namespace std;

int n;

bool used[10];

bool doDigits(int q) {
    //printf("doDigits %d\n", q);
    while (q > 0) {
        used[q % 10] = true;
        q /= 10;
    }

    for (int i = 0; i<10; i++) if (!used[i]) return false;
    return true;
}

long calculate (int x) {
    for (int i = 0; i<10; i++) used[i] = false;

    long a = (long)x;
    while (!doDigits(a)) {
        a+=(long)x;
    }
    return a;
}

int main()
{
    //freopen("be.txt", "r", stdin);

    scanf("%d", &n);
    for (int i=0; i<n; i++) {
        int x; scanf("%d", &x);
        if (x == 0) printf("Case #%d: INSOMNIA\n", i+1);
        else printf("Case #%d: %li\n", i+1, calculate(x));
    }


    return 0;
}
