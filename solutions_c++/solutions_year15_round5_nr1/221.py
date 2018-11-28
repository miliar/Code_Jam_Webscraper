#include<iostream>
#include<fstream>
#include<cstdio>
#include<vector>
#include<string>
#include<cstring>
#include<queue>
#include<map>
#include<set>
#include<algorithm>
#include<iomanip>
#include<bitset>
using namespace std;

const int N = 1000100;

int n, d, rez, s[N], p[N], m[N];
bool ver[N];
vector<int> v[N];

void init() {
    int i;

    memset(ver, 0, sizeof(ver));

    for(i = 0; i < n; ++i) {
        v[i].clear();
    }
}

int ab(int a) {
    return a > 0 ? a : -a;
}

bool cmp(int a, int b) {
    return s[a] < s[b];
}

int aint[4 * N], nr[4 * N], cs[N], cd[N], ren;

void update(int nod, int pozx, int pozy, int poz1, int poz2, int val) {
    if(pozx >= poz1 && poz2 >= pozy) {
        aint[nod] += val;

        if(aint[nod])
            nr[nod] = pozy - pozx + 1;
        else
            nr[nod] = nr[2 * nod] + nr[2 * nod + 1];

        return;
    }

    int mid = (pozx + pozy) / 2;

    if(mid >= poz1)
        update(2 * nod, pozx, mid, poz1, poz2, val);
    if(mid < poz2)
        update(2 * nod + 1, mid + 1, pozy, poz1, poz2, val);

    if(aint[nod])
        nr[nod] = (pozy - pozx + 1);
    else
        nr[nod] = nr[2 * nod] + nr[2 * nod + 1];
}

void calccs(int nod, int pa) {
    cs[nod] = ++ren;

    for(vector<int>::iterator it = v[nod].begin(); it != v[nod].end(); ++it) if(*it != pa)
        calccs(*it, nod);

    cd[nod] = ren;
}

void sol() {
    int i, j;

    cin >> n >> d;

    rez = 0;

    init();
    memset(aint, 0, sizeof(aint));
    memset(nr, 0, sizeof(nr));

    int s0, as, css, rs, m0, am, cm, rm;

    cin >> s0 >> as >> css >> rs >> m0 >> am >> cm >> rm;


    s[0] = s0;
    m[0] = m0;

    ren = 0;

    for(i = 1; i < n; ++i) {

        s[i] = (s[i - 1] * as + css) % rs;

        m[i] = (m[i - 1] * am + cm) % rm;

        v[m[i] % i].push_back(i);
    }

    for(i = 0; i < n; ++i)
        p[i] = i;

    calccs(0, -1);

    sort(p, p + n, cmp);

    j = 0;

    int ver = 0;

    for(i = 0; i < n; ++i)
        update(1, 1, ren, cs[i], cd[i], 1);

    for(i = 0; i < n; ++i) {
        while(j < n && s[p[j]] - s[p[i]] <= d) {
            update(1, 1, ren, cs[p[j]], cd[p[j]], -1);

            if(p[j] == 0)
                ver = 1;

            ++j;
        }

        if(ver)
            rez = max(rez, n - nr[1]);

        update(1, 1, ren, cs[p[i]], cd[p[i]], 1);
        if(p[i] == 0)
            break;
    }

    cout << rez;
}

int main() {
    freopen("ttt", "r", stdin);
    freopen("tttt", "w", stdout);

    int t, a = 0;
    cin >> t;

    while(t--) {
        ++a;
        cout << "Case #" << a << ": ";
        sol();
        cout << "\n";
    }

    return 0;
}
