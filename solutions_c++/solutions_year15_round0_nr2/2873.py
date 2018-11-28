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

int n, x[1100];

bool ssol(int nr) {
    int i, j;

    for(i = 1; i <= nr; ++i) {
        int nx[1100], k, nu = 0;

        for(j = 1; j <= n; ++j) if(x[j] > i) {
            int left = x[j] - i;
            nu += left / i;
            if(left % i)
                ++nu;
        }

        if(nu <= nr - i)
            return 1;
    }
    return 0;
}

void sol() {
    cin >> n;

    int i, j, pas;

    for(i = 1; i <= n; ++i)
        cin >> x[i];

    pas = (1<<10);

    for(i = 0; pas; pas /= 2)
        if(!ssol(i + pas))
            i += pas;

    cout << i + 1 << "\n";
}

int main() {
    freopen("ttt", "r", stdin);
    freopen("tttt", "w", stdout);

    int t, i = 0;

    cin >> t;
    while(t--) {
        ++i;
    cout << "Case #" << i << ": ";
    sol();
    }

    return 0;
}
