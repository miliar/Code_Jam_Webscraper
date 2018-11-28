#include <cstdio>
#include <algorithm>
#include <set>
#include <functional>

using namespace std;

int n, x;

void solve ()
{
    multiset<int,greater<int>> S;

    scanf ("%d%d", &n, &x);

    for (int i = 0; i < n; ++i) {
        int t; scanf ("%d", &t);
        S.insert(t);
    }

    int ans = 0;
    while (S.size()) {
        int t = *S.begin(); 
        S.erase(S.begin());

        auto jt = S.lower_bound(x - t);
        if (jt != S.end())
            S.erase(jt);

        ++ans;
    }

    printf ("%d\n", ans);
}

int main (int argc, char *argv[])
{
    int No; scanf ("%d", &No);
    for (int i = 0; i < No; ++i) {
        if (argc == 1) printf ("Case #%d: ", i + 1);
        solve();
    }

    return 0;
}


