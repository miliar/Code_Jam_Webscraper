#include <iostream>
#include <cstdio>
#include <vector>
#include <ctime>
#include <cstdlib>
#include <set>
#include <map>
#include <algorithm>
#include <cmath>
#include <unordered_map>
#include <unordered_set>
#include <cstring>


#define puba push_back
#define mapa make_pair
#define ff first
#define ss second
#define pii pair < int, int >


using namespace std;


vector < int > used;
vector < vector < int > > g;
int n;

bool dfs(vector < int > &perm, int pos) {
    if (pos == (int) perm.size()) return true;

    bool flag = true;
    for (int i = 0; i < n; ++i) {
        if (g[perm[pos]][i] == 1 && used[i] == 0) {
            used[i] = 1;
            flag = false;
            if (!dfs(perm, pos + 1)) return false;
            used[i] = 0;
        }
    }
    if (flag) return false;
    return true;
} 


typedef long long LL;
int main() {
    int t;
    cin >> t;
    for (int q = 0; q < t; ++q) {
        cerr << q << endl;
        cout << "Case #" << q + 1 << ": ";
        //int n;
        cin >> n;
        string s;

        //vector < vector < int > > g;
        g.clear();
        g.resize(n);


        vector < pii > bads;
        for (int i = 0; i < n; ++i) {
            cin >> s;
            for (int j = 0; j < n; ++j) {
                g[i].puba(s[j] - '0');
                if (s[j] == '0') {
                    bads.puba(mapa(i, j));
                }
            }
        }

        int sz = bads.size();
        int ans = (int) 10000;
        for (int masc = 0; masc < (1 << sz); ++masc) {
            vector < int > num;
            for (int i = 0; i < sz; ++i) {
                if (masc & (1 << i)) {
                    num.puba(i);
                }
            }

            for (int i = 0; i < (int) num.size(); ++i) {
                g[bads[num[i]].ff][bads[num[i]].ss] = 1;
            }

            vector < int > perm (n);
            for (int i = 0; i < n; ++i) {
                perm[i] = i;

            }
            bool flag = true;

            do {
                used.clear();
                used.resize(n, 0);

                if (!dfs(perm, 0)) {
                    flag = false;
                    break;
                }
            } while (next_permutation(perm.begin(), perm.end()));
            
            if (flag && (int) num.size() < ans) {
                ans = num.size();
            }

            for (int i = 0; i < (int) num.size(); ++i) {
                g[bads[num[i]].ff][bads[num[i]].ss] = 0;
            }

        }
        cout << ans << endl;
    }
    return 0;
}