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

int k, c, s;

int sol() {
    int i;

    cin >> k >> c >> s;

    long long po = 1, l = 1;
    for(i = 1; i < c; ++i)
        l = l * k;

    for(i = 1; i <= k; ++i) {

        out << po << " ";
        po += l;
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
        sol(); out << "\n";

        printf("Test %d\n", a);
    }

    return 0;
}
