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

int n, p, s, r;
vector<string> v[6];

void sol() {
    int i, j;

    cin >> n >> r >> p >> s;
    for(i = 0; i < 6; ++i)
        v[i].clear();

    for(i = 1; i <= r; ++i)
        v[0].push_back("R");

    for(i = 1; i <= p; ++i)
        v[1].push_back("P");

    for(i = 1; i <= s; ++i)
        v[2].push_back("S");

    for(i = 1; i <= n; ++i) {

        while(1) {
            int elmax = 0, pmax;

            for(j = 0; j < 3; ++j) {

                if(v[j].size() > elmax) {
                    elmax = v[j].size();
                    pmax = j;
                }
            }

            if(!elmax)
                break;

            string nou = v[pmax].back(), n2, r;
            v[pmax].pop_back();

            pmax = (pmax + 1) % 3;

            if(v[pmax].size()) {
                n2 = v[pmax].back();
                v[pmax].pop_back();

                if(nou > n2)
                    r = n2 + nou;
                else
                    r = nou + n2;

                v[pmax + 3].push_back(r);
            }
            else {
                pmax = (pmax + 1) % 3;

                if(!v[pmax].size()) {
                    out << "IMPOSSIBLE";
                    return;
                }

                n2 += v[pmax].back();
                v[pmax].pop_back();


                if(nou > n2)
                    r = n2 + nou;
                else
                    r = nou + n2;

                v[(pmax + 1) % 3 + 3].push_back(r);
            }
        }

        for(j = 0; j < 3; ++j) {
            v[j] = v[j + 3];
            v[j + 3].clear();
        }
    }

    for(i= 0; i < 3; ++i) if(v[i].size())
        out << v[i][0];
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
