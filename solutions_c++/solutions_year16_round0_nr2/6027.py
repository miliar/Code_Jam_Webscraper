#include <bits/stdc++.h>
using namespace std;

const int N = 1e2+1;
int t, T, n;
char s[N], o[] = {'+', '-'};

int slv(int n, int i) {
    if (n == -1) return -1;
    while(n>=0 and o[i] == s[n]) --n;
    return 1 + slv(n, i^1);
}

int main() {
    scanf("%d", &T);
    while(t++ < T) {
        scanf("%s", s);
        n = strlen(s);
        printf("Case #%d: %d\n", t, slv(n-1, 0));
    }
    return 0;
}
