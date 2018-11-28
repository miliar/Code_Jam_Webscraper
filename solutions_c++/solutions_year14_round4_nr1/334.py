//
// data_packing.cpp
//
// Siwakorn Srisakaokul - ping128
// Written on Saturday, 31 May 2014.
//

#include <cstdio>
#include <iostream>
#include <sstream>
#include <cstdlib>
#include <string>
#include <vector>
#include <set>
#include <queue>
#include <stack>
#include <list>
#include <cmath>
#include <algorithm>
#include <map>
#include <ctype.h>
#include <string.h>

#include <assert.h>

using namespace std;

typedef long long LL;
typedef pair<int, int> PII;
typedef pair<PII, int> PII2;

#define MAXN 10005

int N;
int SZ;

void solve() {
    multiset<int> files;
    cin >> N >> SZ;
    for (int i = 0; i < N; i++) {
        int a;
        cin >> a;
        files.insert(a);
    }

    int ans = 0;
    while (files.size() > 0) {
        ans++;
        if (files.size() <= 1) {
            break;
        }
        
        auto it = files.begin();
        int used = *it;
        files.erase(it);
        if ((int)files.size() > 0) {
            auto it2 = files.lower_bound(SZ - used);
            if (it2 != files.end() && *it2 == SZ - used) {
            } else if (it2 != files.begin()) it2--;
            if (*it2 <= SZ - used) {
                files.erase(it2);
            }
        }
    }
    cout << ans << endl;
}

int main() {
    int test;
    scanf("%d", &test);
    for (int tt = 0; tt < test; tt++) {
        printf("Case #%d: ", tt + 1);
        solve();
    }
    return 0;
}

