#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

const int N = 10005;

typedef long long ll;
int t, l, sn;
ll x;
char str[N];
char s[N * 12];
char g[300][300];

char get(char a, char b) {
    int flag1 = 1, flag2 = 1;
    if (a == '2' || (a >= 'x' && a <= 'z')) {
        flag1 = -1;
        if (a == '2') a = '1';
        else a = a - 'x' + 'i';
    }
    if (b == '2' || (b >= 'x' && b <= 'z')) {
        flag2 = -1;
        if (b == '2') b = '1';
        else b = b - 'x' + 'i';
    }
    if (flag1 * flag2 == 1)
        return g[a][b];
    else {
        if (g[a][b] == '1') return '2';
        else if (g[a][b] == '2') return '1';
        else if (g[a][b] >= 'x' && g[a][b] <= 'z') return g[a][b] - 'x' + 'i';
        else return g[a][b] - 'i' + 'x';
    }
}

bool judge() {
    char u = s[0];
    int i = 1;
    for (; i < sn; i++) {
        if (u == 'i') break;
        u = get(u, s[i]);
    }
    if (i == sn) return false;
    u = s[i++];
    for (; i < sn; i++) {
        if (u == 'j') break;
        u = get(u, s[i]);
    }
    if (i == sn) return false;
    u = s[i++];
    for (; i < sn; i++) {
        u = get(u, s[i]);
    }
    return u == 'k';
}

int main() {
    g['1']['1'] = '1';
    g['1']['i'] = 'i';
    g['1']['j'] = 'j';
    g['1']['k'] = 'k';
    g['i']['1'] = 'i';
    g['i']['i'] = '2';
    g['i']['j'] = 'k';
    g['i']['k'] = 'y';
    g['j']['1'] = 'j';
    g['j']['i'] = 'z';
    g['j']['j'] = '2';
    g['j']['k'] = 'i';
    g['k']['1'] = 'k';
    g['k']['i'] = 'j';
    g['k']['j'] = 'x';
    g['k']['k'] = '2';
    int cas = 0;
    scanf("%d", &t);
    while (t--) {
        scanf("%d%lld", &l, &x);
        scanf("%s", str);
        int tot = min(x, x % 4 + 12);
        sn = 0;
        for (int i = 0; i < tot; i++) {
            for (int j = 0; j < l; j++)
                s[sn++] = str[j];
        }
        printf("Case #%d: ", ++cas);
        if (judge()) printf("YES\n");
        else printf("NO\n");
    }
    return 0;
}
