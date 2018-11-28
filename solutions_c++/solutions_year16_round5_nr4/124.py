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

int n, l;
char a[55], b[101][55];

void sol() {
    int i, j;

    cin >> n >> l;


    for(i = 1; i <= n; ++i) {

        cin >> b[i];

    }


    cin >> a;

    for(i = 1; i <= n; ++i) {
        int vv = 0;

        for(j = 0; j < l; ++j) {
            if(b[i][j] != a[j])
                vv = 1;
        }

        if(!vv) {
            out << "IMPOSSIBLE";
            return;
        }
    }

    if(l == 1) {
        out << "? 0";
        return;
    }

    for(i = 1; i < l; ++i)
        out << "1";
    out << " ";
    for(i = 1; i <= l; ++i) {
        out << "0?";
    }
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
