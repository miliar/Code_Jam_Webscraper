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

long long isPrim(long long a) {

    for(long long i = 2; i * i <= a; ++i)
        if(a % i == 0)
            return i;

    return 0;
}

int n, j, els;
long long el[11], p[11], va[11];

bool ver(long long nr) {
    long long aa = nr;

    int i;

    for(i = 2; i <= 10; ++i) {
        p[i] = 1;
        el[i] = 0;
    }

    while(nr) {

        for(i = 2; i <= 10; ++i) {

            el[i] += p[i] * (nr & 1);
            p[i] *= i;
        }

        nr /= 2;
    }

    for(i = 2; i <= 10; ++i) {

        va[i] = isPrim(el[i]);
        if(!va[i])
            return 0;
    }

    ++els;

    out << el[10] << " ";

    for(i = 2; i <= 10; ++i)
        out << va[i] << " ";
out << "\n";
    if(els == j)
        return 1;

    return 0;
}

int sol() {
    long long nr;


    cin >> n >> j;

    nr = 1 + (1LL<<(n - 1));

    while(1) {

        if(ver(nr))
            return 0;

        nr += 2;
    }
}

int main() {
    freopen("ttt", "r", stdin);
    //freopen("tttt", "w", stdout);

    int t, a = 0;
    cin >> t;

    while(t--) {
        ++a;
        out << "Case #" << a << ":\n";
        sol();

        printf("Test %d\n", a);
    }

    return 0;
}
