// Written by Luis Garcia, 2016.
// OJ-ID: CJ1603A

#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

int main() {
    char *words[10] = {
        "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"
    };

    char S[2001], out[2001];

    int T;
    scanf("%d", &T);
    for (int _T = 1; _T <= T; ++_T) {
        scanf("%s", S);

        struct { int n; char c; } pts[] = {
            {0, 'Z'},
            {8, 'G'},
            {3, 'H'},
            {4, 'R'},
            {2, 'W'},
            {6, 'X'},
            {5, 'F'},
            {7, 'V'},
            {1, 'O'},
            {9, 'E'},
        };

        int cnt[26] = {}, k = 0;
        for (char * psz = S; * psz; ++psz) {
            ++cnt[* psz - 'A'];
        }

        for (int i = 0; i < 10; ++i) {
            int t = cnt[pts[i].c - 'A'];
            int n = pts[i].n;
            
            for (char * psz = words[n]; * psz; ++psz) {
                cnt[* psz - 'A'] -= t;
            }

            for (int j = 0; j < t; ++j)
                out[k++] = n + '0';
        }

        sort(out, out + k);
        out[k] = 0;
        printf("Case #%d: %s\n", _T, out);
    }
    return 0;
}
