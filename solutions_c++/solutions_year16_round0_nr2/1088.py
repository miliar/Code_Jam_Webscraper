// Written by Luis Garcia, 2016.
// OJ-ID: CJ1601B

#include <cstdio>
#include <cstring>

using namespace std;

int f(char * sz, int i, char v) {
    while (i >= 0 && sz[i] == v) --i;
    if (i < 0) return 0;
    return f(sz, i, v == '+' ? '-' : '+') + 1;
}

int main() {
    int T;
    char S[200];
    scanf("%d", &T);
    for (int _T = 1; _T <= T; ++_T) {
        scanf("%s", &S);

        int n = strlen(S);
        printf("Case #%d: %d\n", _T, f(S, n - 1, '+'));
    }
    return 0;
}
