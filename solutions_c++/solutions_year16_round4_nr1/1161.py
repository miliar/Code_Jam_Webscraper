#include <iostream>
#include <fstream>
#include <vector>
#define pb push_back

using namespace std;

int main()
{
    ifstream cin("A-large.in");
    ofstream cout("output_large");
    int t;
    cin >> t;
    for (int i = 0; i < t; ++i)
    {
        int n, r, p, s;
        cin >> n >> r >> p >> s; //r -> s -> p
        cout << "CASE #" << i + 1 << ": ";
        vector<string> poolr, pools, poolp, npr, nps, npp;
        for (int i = 0; i < r; ++i)
            poolr.pb("R");
        for (int i = 0; i < s; ++i)
            pools.pb("S");
        for (int i = 0; i < p; ++i)
            poolp.pb("P");
        for (int i = 0; i < n; ++i)
        {
            int nr = (r + s - p) / 2, ns = (p + s - r) / 2, np = (p + r - s) / 2;
            if (nr < 0 || ns < 0 || np < 0)
                {n = 0; break;}
            npr.clear(), nps.clear(), npp.clear();
            for (int i = 0; i < nr; ++i)
                npr.pb(min(poolr.back(), pools.back()) + max(poolr.back(), pools.back())), poolr.pop_back(), pools.pop_back();
            for (int i = 0; i < ns; ++i)
                nps.pb(min(pools.back(), poolp.back()) + max(pools.back(), poolp.back())), pools.pop_back(), poolp.pop_back();
            for (int i = 0; i < np; ++i)
                npp.pb(min(poolp.back(), poolr.back()) + max(poolp.back(), poolr.back())), poolp.pop_back(), poolr.pop_back();
            swap(npr, poolr);
            swap(nps, pools);
            swap(npp, poolp);
            swap(nr, r);
            swap(ns, s);
            swap(np, p);
        }
        if (!n)
            cout << "IMPOSSIBLE\n";
        else if (poolr.size())
            cout << poolr.back() << '\n';
        else if (pools.size())
            cout << pools.back() << '\n';
        else if (poolp.size())
            cout << poolp.back() << '\n';
    }
    return 0;
}
