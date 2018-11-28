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

char a[110];
int l;

int sol() {

    int i, j;

    cin >> (a + 1);
    l = strlen(a + 1);

    while(a[l] == '+')
        --l;

    if(!l)
        return 0;

    int r = 1;

    for(i = 2; i <= l; ++i) {
        if(a[i] != a[i - 1])
            ++r;
    }

    return r;
}

int main() {
    freopen("ttt", "r", stdin);
    //freopen("tttt", "w", stdout);

    int t, a = 0;
    cin >> t;

    while(t--) {
        ++a;
        out << "Case #" << a << ": ";
        out << sol() << "\n";

        printf("Test %d\n", a);
    }

    return 0;
}
