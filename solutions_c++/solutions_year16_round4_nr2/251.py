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

const int N = 210;

int n, k;
double p[N], rez, d[N][N];

double calc(int cs, int cd) {
    int i, j, nrb = 0;

    for(i = 0; i < n; ++i)
        d[0][i] = 0;

    d[0][0] = 1;

    for(i = 1; i <= n; ++i) {

        for(j = 0; j <= i + 1; ++j) {

            if(i > cs && i < cd) {
                d[i][j] = d[i - 1][j];
                continue;
            }

            d[i][j] = d[i - 1][j] * (1.0 - p[i]);
            if(j)
                d[i][j] += d[i - 1][j - 1] * p[i];
        }
    }

    return d[n][k / 2];
}

double brut() {
    int i, j;
    rez = 0;

    for(i = 0; i < (1<<n); ++i) {
       // rez = max(rez, calc(i));
    }

    return rez;
}

double soll() {
    int i, j; rez = 0;

    for(i = 0; i <= k; ++i) {

        int ma = 0;

    //    for(j = 0; j < i; ++j)
    //        ma += (1<<j);
    //    for(j = n - 1; j > n - (k - i) - 1; --j)
    //        ma += (1<<j);

        rez = max(rez, calc(i, n - (k - i) + 1));
    }

    return rez;
}

void sol() {
    int i, j;

    cin >> n >> k;

    for(i = 1; i <= n; ++i)
        cin >> p[i];
    sort(p + 1, p + n + 1);

    //brut();

    //if(brut() != soll())
    //    while(1) cout << "asdsdsads";

    out << soll();
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
