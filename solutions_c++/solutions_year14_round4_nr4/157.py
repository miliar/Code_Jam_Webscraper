#include <iostream>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <algorithm>
#include <set>

using namespace std;

int T;

int abs(int a) { return a > 0 ? a : -a; }
int min(int a, int b) { return a < b ? a : b; }



int n, m;
string a[100];
int p[100];
set<string> cnt[100];
int maxcnt;
int maxans;

void place(int d)
{
    if (d == m) {
        for (int i=0; i<n; ++i) cnt[i].clear();
        // count
        for (int i=0; i<m; ++i) {
            //
            cnt[p[i]].insert("");
            for (int j=0; j<a[i].length(); ++j) {
                cnt[p[i]].insert(a[i].substr(0,j+1));
                //cout << a[i].substr(0, j+1) << endl;
            }
            //cout << a[i] << '-' << endl;
        }
        int tot = 0;
        for (int i=0; i<n; ++i) {
            //cout << cnt[i].size() << ' ';
            tot += cnt[i].size();
        }
        //cout << endl;
        if (tot > maxans) {
            maxans = tot;
            maxcnt = 1;
        } else if (tot == maxans) {
            maxcnt++;
        }
        return;
    }
    for (int i=0; i<n; ++i) {
        p[d] = i;
        place(d+1);
    }
}

int solve()
{
    maxans = 0;
    maxcnt = 0;
    place(0);
}

int main()
{
    cin >> T;
    for (int t=1; t<=T; ++t) {
        cin >> m >> n;
        for (int i=0; i<m; ++i) {
            cin >> a[i];
        }

        solve();
        printf("Case #%d: %d %d\n", t, maxans, maxcnt);
    }
    return 0;
}
