#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

int n;
vector<int> a;

int breaksCnt(int maxSz)
{
    int ad = 0;
    for(int i = 0; i < n; ++i)
    {
        if(a[i] <= maxSz) break;

        int c = (a[i] + maxSz - 1) / maxSz;
        ad += max(0, c-1);
    }
    return ad;
}

bool isOK(int x)
{
    for(int i = 1; i <= x; ++i)
        if(breaksCnt(i) + i <= x)
            return true;
    return false;
}

int main()
{
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    ios_base::sync_with_stdio(false);

    int T;
    cin >> T;
    for(int t = 1; t <= T; ++t)
    {
        cin >> n;

        a.resize(n);
        for(int i = 0; i < n; ++i)
            cin >> a[i];

        sort(a.begin(), a.end());
        reverse(a.begin(), a.end());
//
//        cout << "DBG: ";
//        for(int i = 0; i < n; ++i)
//            cout << a[i] << ' ';
//        cout << endl;

        int l = 1;
        int r = a[0];

        while(l < r)
        {
            int m = (l+r) >> 1;
            if(isOK(m))
                r = m;
            else
                l = m+1;
        }

        cout << "Case #" << t << ": " << l << endl;
    }

    return 0;
}
