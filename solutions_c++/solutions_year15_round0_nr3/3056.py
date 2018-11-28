#include <cstdio>
#include <cstdlib>

const int MAXN = 11111, MAXC = 222;

char a[MAXN], p[MAXC][MAXC];
int s[MAXN][MAXN];

inline char calc(char x, char y) {
    return x / abs(x) * y / abs(y) * p[abs(x)][abs(y)];
}

int main() {
    int t;
    scanf("%d", &t);
    p['1']['1'] = '1', p['1']['i'] = 'i', p['1']['j'] = 'j', p['1']['k'] = 'k';
    p['i']['1'] = 'i', p['i']['i'] = -'1', p['i']['j'] = 'k', p['i']['k'] = -'j';
    p['j']['1'] = 'j', p['j']['i'] = -'k', p['j']['j'] = -'1', p['j']['k'] = 'i';
    p['k']['1'] = 'k', p['k']['i'] = 'j', p['k']['j'] = -'i', p['k']['k'] = -'1';
    for (int cs = 1; cs <= t; ++cs) {
        int l, x;
        scanf("%d%d%s", &l, &x, a);
        for (int i = 0; i < l; ++i)
            for (int j = 1; j < x; ++j)
                a[i + l * j] = a[i];
        l *= x;
        for (int i = 0; i < l; ++i) {
            s[i][i] = a[i];
            for (int j = i + 1; j < l; ++j)
                s[i][j] = calc(s[i][j - 1], a[j]);
        }
        bool got = false;
        for (int i = 0; !got && i < l - 2; ++i)
            if (s[0][i] == 'i')
                for (int j = i + 1; !got && j < l - 1; ++j)
                    if (s[i + 1][j] == 'j' && s[j + 1][l - 1] == 'k')
                        got = true;
        printf("Case #%d: %s\n", cs, got ? "YES" : "NO");
    }
    return 0;
}
