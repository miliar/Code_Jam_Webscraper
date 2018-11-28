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

const int N = 205;

int n, nr, ver[2][1000000], rmin;
map<string, int> s;
vector<int> v[N];
char a[20000];

void sol() {
    int i, j;

    s.clear();

    memset(ver, 0, sizeof(ver));
    nr = 0;

    cin >> n;

    for(i = 1; i <= n; ++i)
        v[i].clear();

    cin.get();

    for(i = 1; i <= n; ++i) {
        cin.getline(a, 20000);

        string t = "";

        for(j = 0; a[j] != 0; ++j) {
            if(a[j] == ' ') {

                if(!s[t]) {
                    s[t] = ++nr;
                }

                v[i].push_back(s[t]);

                t = "";
            }
            else
                t += a[j];
        }

        if(!s[t]) {
            s[t] = ++nr;
        }

        v[i].push_back(s[t]);

        t = "";
    }

    for(i = 0; i < v[1].size(); ++i)
        ver[0][v[1][i]] = 1;
    for(i = 0; i < v[2].size(); ++i)
        ver[1][v[2][i]] = 1;

    int nrc = 0, rez = 1000000000;
    for(i = 0; i <= nr; ++i)
        if(ver[0][i] && ver[1][i])
            ++nrc;

    if(n == 2) {
        cout << nrc;
        return;
    }

    for(i = 0; i < (1<<(n - 2)); ++i) {

        for(j = 3; j <= n; ++j) {

            int aa = (((1<<(j - 3)) & i) != 0);

            for(vector<int>::iterator it = v[j].begin(); it != v[j].end(); ++it) {
                ver[aa][*it]++;

                if(ver[aa][*it] == 1 && ver[1 - aa][*it])
                    ++nrc;
            }
        }

        rez = min(rez, nrc);

        for(j = 3; j <= n; ++j) {

            int aa = (((1<<(j - 3)) & i) != 0);

            for(vector<int>::iterator it = v[j].begin(); it != v[j].end(); ++it) {
                ver[aa][*it]--;

                if(ver[aa][*it] == 0 && ver[1 - aa][*it])
                    --nrc;
            }
        }
    }

    cout << rez;
}

int main() {
    freopen("ttt", "r", stdin);
    freopen("tttt", "w", stdout);

    int t, a = 0;
    cin >> t;

    while(t--) {
        ++a;
        cout << "Case #" << a << ": ";
        sol();
        cout << "\n";
    }

    return 0;
}
