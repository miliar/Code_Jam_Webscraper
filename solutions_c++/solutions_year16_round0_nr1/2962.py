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

const int N = 15;

int n, ver[N];

ofstream out("tttt");

int sol() {
    int i, j;

    memset(ver, 0, sizeof(ver));
    cin >> n;

    if(n == 0) {
        out <<"INSOMNIA";
        return 0;
    }

    int nrdif = 0;
    int aa = n, zz = 0;

    while(1) {
        ++zz;

        int nx = n;

        while(nx) {

            if(!ver[nx % 10]) {
                ver[nx % 10] = 1;
                nrdif++;
            }

            nx /= 10;
        }

        if(nrdif == 10) {
            out << n;

    printf("%d\n", zz);

            return 0;
        }

        n += aa;
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
