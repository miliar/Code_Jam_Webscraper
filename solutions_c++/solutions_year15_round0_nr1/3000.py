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

void sol() {
    char a[1100];
int n;
    cin >> n >> a;
    int nr = 0, nrc = a[0] - '0';

    for(int i = 1; a[i] != 0; ++i) {
        if(nrc < i) {
            ++nr;
            ++nrc;
        }

        nrc += a[i] - '0';
    }

    cout << nr << "\n";
}

int main() {
    freopen("ttt", "r", stdin);
    freopen("tttt", "w", stdout);

    int t, i= 0 ;
    cin >> t;
    while(t--) {
        ++i;
        cout << "Case #" << i << ": ";
        sol();
    }

    return 0;
}
