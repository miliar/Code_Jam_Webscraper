#include <cstdio>
#include <cstring>
using namespace std;

FILE *fout = fopen ("OPF.out", "w");
FILE *fin  = fopen ("OPF.in", "r");
char s[1001];
int k, l;

bool ok() {
    for (int i = l-k+1; i < l; ++i)
        if (s[i] == '-')
        return false;
    return true;
}

void solve(int x) {
    int y = 0;
    fscanf(fin, "%s %d\n", s, &k);
    fprintf(fout, "Case #%d: ", x);
    l = strlen(s);
    for (int i = 0; i+k <= l; ++i)
    if (s[i] == '-') {
        for (int j = i; j < i+k; ++j)
            s[j] = '-' + '+' - s[j];
        ++y;
    }
    if (ok())
        fprintf(fout, "%d\n", y);
    else
        fprintf(fout, "IMPOSSIBLE\n");
}

int main() {
    int T;
    fscanf(fin, "%d\n", &T);
    for (int i = 1; i <= T; ++i)
        solve(i);
    return 0;
}
