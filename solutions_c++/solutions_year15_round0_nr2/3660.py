#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <algorithm>
#include <vector>
#include <set>

#define pb push_back
#define mp make_pair
#define ll long long
#define forn(i, n) for (int i = 0; i < (int) n; i++)

const int INF = 1e9;

using namespace std;


int main()
{
    freopen("a.in", "rt", stdin);
    freopen("a.out", "wt", stdout);

    int t, n;

    scanf("%d", &t);

    forn(t1, t) {
        vector <int> a;
    	cin >> n;

        int res = 0;

        forn(i, n) {
            int x;
            cin >> x;
            a.pb(x);
            res = max(res, a[i]);
        }

        for (int k = 1; k <= 1000; k++) {
            int res1 = 0;
            forn(i, n) {
                res1 += a[i] / k - 1;
                if (a[i] % k != 0)
                    res1++;
            }
            res = min(res, res1 + k);
        }

    	cout << "Case #" << t1 + 1 << ": " << res << endl;
    }


    return 0;
}

