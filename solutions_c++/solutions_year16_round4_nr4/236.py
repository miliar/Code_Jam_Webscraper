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

ofstream out("tttt");

const int N = 5;

int n, rez, ver, el[N], used[N];
char a[N][N], na[N][N];


void bback(int p, int el) {
    if(p == n + 1) {
        ver = 1;
        for(int i = 1; i <= n; ++i) if(na[el][i] && !used[i])
            ver = 0;

        return;
    }

    if(p != el) for(int i = 1; i <= n; ++i) if(na[p][i] && !used[i] && na[el][i]) {
        used[i] = 1;

        bback(p + 1, el);

        if(ver)
            return;

        used[i] = 0;
    }
    bback(p + 1, el);
}

int calc(int m) {
    int i, j, k;
    int nc = 0, rc = 0;

    for(i = 1; i <= n; ++i)
        for(j = 1; j <= n; ++j)
            na[i][j] = a[i][j];

    for(i = 1; i <= n; ++i) {

        for(j = 1; j <= n; ++j) if(na[i][j] == 0) {

            if(m & (1<<nc)) {
                na[i][j] = 1;
                ++rc;
            }


            ++nc;
        }
    }

    for(i = 1; i <= n; ++i) {
        ver = 0;

        memset(used, 0, sizeof(used));

        bback(1, i);

        if(ver)
            return 666;
    }

    return rc;
}

void sol() {

    int nr0 = 0, i, j;

    cin >> n;

    for(i = 1; i <= n; ++i) {
        cin >> (a[i] + 1);

        for(j = 1; j <= n; ++j) {
            a[i][j] -= '0';
            if(!a[i][j])
                ++nr0;
        }
    }

    rez = 666666;

    for(i = 0; i < (1<<nr0); ++i) {

        rez = min(rez, calc(i));
    }

    out << rez;
}

int main() {
    freopen("ttt", "r", stdin);
    //freopen("tttt", "w", stdout);

    int t, a = 0;
    cin >> t;

    while(t--) {
        ++a;
        out << "Case #" << a << ": ";
        sol();
		out << "\n";

        printf("Test %d\n", a);
    }

    return 0;
}
