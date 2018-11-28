#include <iostream>
#include <cstdio>
#include <string>
#include <string.h>
#include <queue>
#include <math.h>
#include <cmath>
#include <map>
#include <set>
#include <vector>
#include <algorithm>
#include <bitset>
#include <ctype.h>
#include <cassert>
#include <stack>
#include <fstream>
#include <unordered_map>
#include <unordered_set>
#include <ctime>
#include <functional>

using namespace std;

#define snd second
#define fst first
#define mp make_pair
#define ll long long
#define ull unsigned long long
#define ld long double
#define pb push_back
#define left _left
#define right _right

const ld pi = 3.14159265359;

template<typename T>
T abs(T x) {
    return x > 0 ? x : -x;
}

template<typename T>
T sqr(T x) {
    return x * x;
}


int pw(int x) {
    int i = 0;
    while ((1 << i) < x) {
        i++;
    }
    assert((1 << i) == x);
    return i;
}

int main() {
    srand(time(NULL));
    //gen();
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    int t;
    cin >> t;

    for (int tt = 1; tt <= t; tt++) {
        cerr << tt << endl;
        int p;
        cin >> p;

        vector<int> v;
        for (int i = 0; i < p; i++) {
            int x;
            cin >> x;
            v.pb(x);
        }

        vector<int> a;

        int sum = 0;
        for (int i = 0; i < p; i++) {
            int cnt;
            cin >> cnt;
            sum += cnt;
            while (cnt--) {
                a.pb(v[i]);
            }
        }

        sort(a.begin(), a.end());

        multiset<ll> need;
        vector<ll> ans;

        for (int i = 1; i < a.size(); i++) {
            if (need.count(a[i])) {
                need.erase(need.find(a[i]));
            } else {
                for (int j = 1; j < (1 << ans.size()); j++) {
                    ll s = 0;
                    for (int h = 0; h < ans.size(); h++) {
                        if (j & (1 << h)) {
                            s += ans[h];
                        }
                    }
                    need.insert(s + a[i]);
                }

                ans.pb(a[i]);
            }
        }

        assert(need.empty());

        sort(ans.begin(), ans.end());


        printf("Case #%d:", tt);
        for (int y : ans) {
            printf(" %d", y);
        }

        printf("\n");
    }

    return 0;
}