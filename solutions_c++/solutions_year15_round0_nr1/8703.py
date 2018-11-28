#include <cstdio>

using namespace std;

int main() {
    freopen("C:\\users\\martin\\downloads\\A-large.in", "r", stdin);
    freopen("C:\\users\\martin\\downloads\\A-large.out", "w", stdout);
    int t, T, smax, suma, re, i;
    char s[2000];
    scanf("%d", &T);
    for(t = 1;t <= T;t++) {
        scanf("%d%s", &smax, s);
        suma = 0;
        re = 0;
        for(i = 0;i <= smax;i++) {
            if(suma < i) {
                re += i - suma;
                suma = i;
            }
            suma += (s[i] - '0');
        }
        printf("Case #%d: %d\n", t, re);
    }
    return 0;
}
