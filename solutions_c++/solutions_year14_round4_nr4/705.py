#include <iostream>
#include <cmath>
#include <vector>
#include <memory.h>
#include <map>
#include <set>
#include <cstdio>
#include <algorithm>
#include <cstdlib>
#include <ctime>
#include <string>

using namespace std;

const int DEBUG = 1;

int p[55];
string s[55];

int n,m,t,ans,res;

void rec(int x) {
    if (x == m) {
        int ret = 0;
        for (int i = 0; i < n; ++i) {
            map<pair<int,int>, bool> a;
            //map<string, bool> a;
            int rett = 0;
            for (int j = 0; j < m; ++j)
                if (p[j] == i) {
                    long long h1 = 0, h2 = 0;
                    for (int q = 0; q < (int)s[j].size(); ++q) {
                        h1 = (h1 * 31 + (s[j][q] - 'A' + 1)) % 1000000007;
                        h2 = (h2 * 29 + (s[j][q] - 'A' + 1)) % 1000000009;
                        pair <int, int> v = make_pair(h1, h2);
                        if (!a.count(v)) {
                            a[v] = true;
                            ++rett;
                        }
                    }
                }
            if (rett > 0) rett++;
            ret += rett;
        }
        if (ret > ans) {
            ans = ret;
            res = 1;
        }
        else if (ret == ans) res++;
        return ;
    }

    for (int i = 0; i < n; ++i) {
        p[x] = i;
        rec(x + 1);
    }
}

int main()
{
    if (DEBUG) {
        freopen("input.txt","r",stdin);
        freopen("output.txt","w",stdout);
    }
    int number = 0;
    cin >> t;
    while (t--) {
        ++number;
        cin >> m >> n;
        for (int i = 0; i < m; ++i) cin >> s[i];
        //for (int i = 0; i < m; ++i) reverse(s[i].begin(),s[i].end());
        cout << "Case #" << number << ": ";
        ans = 0, res = 1;
        rec(0);
        cout << ans << " " << res << endl;
    }
    return 0;
};

