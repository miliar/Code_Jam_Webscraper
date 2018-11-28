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

int n, d[20100][2], nd[20100][2];
char a[20100];

void sol() {
    int i, j;

    cin >> a;
    n = strlen(a);

    for(i = 0; i <= n; ++i)
        d[i][0] = d[i][1] = -1;
    d[0][0] = 0; d[0][1] = 0;

    for(i = 0; i < n; ++i) {
        if(a[i] == 'C')
            a[i] = 1;
        else
            a[i] = 0;

        for(j = 0; j <= i + 1; ++j)
            nd[j][0] = nd[j][1] = -1;

        for(j = 0; j <= i + 1; ++j) {

            if(d[j + 1][1 - a[i]] != -1)
                nd[j][a[i]] = d[j + 1][1 - a[i]] + 5;
            if(d[j + 1][a[i]] != -1)
                nd[j][1 - a[i]] = d[j + 1][a[i]] + 10;

            if(j) {
                nd[j][a[i]] = d[j - 1][1 - a[i]];
            }
        }

        for(j = 0; j <= i + 1; ++j) {
            d[j][0] = nd[j][0];
            d[j][1] = nd[j][1];

            if(j == 0) {
                d[0][0] = max(d[0][0], d[0][1]);
                d[0][1] = max(d[0][0], d[0][1]);
            }

            //cout << d[j][0] << " " << d[j][1] << "\n";
        }
    }

    int r = 0;

    for(i = 0; i <= n; ++i)
        r = max(r, max(d[i][0], d[i][1]));

    out << r;
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
