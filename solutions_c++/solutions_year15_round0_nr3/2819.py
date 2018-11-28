#include <iostream>
#include <cstdio>
#include <map>

#define ll long long

using namespace std;

int main()
{
    freopen("in", "r", stdin);
    freopen("out", "w", stdout);
    int mat[4][4] =
    {
        {0,1,2,3},
        {1,0,3,2},
        {2,3,0,1},
        {3,2,1,0}
    };

    bool isNeg[4][4]=
    {
        {0,0,0,0},
        {0,1,0,1},
        {0,1,1,0},
        {0,0,1,1}
    };

    int T; cin >> T;

    for (int qq = 1; qq <= T; qq++)
    {
        ll L, X; cin >> L >> X;
        ll minI = L*X;
        ll maxK = -1;
        int neg = 0;
        int cur = 0;
        
        string s; cin >> s;
        for (ll i = 0; i < L*X; i++)
        {
            ll curpos = i%L;
            char curchar = s[curpos];
            int curChar = curchar - 'i' + 1;
            neg = neg^isNeg[cur][curChar];
            cur = mat[cur][curChar];
            if (cur == 1 && neg == 0)
            {
                minI = min(minI, i);
            }else if (cur == 3 && neg == 0)
            {
                maxK = i;
            }
            //cout << cur << " " << neg << endl;
            
        }
        bool ret = false;
        if (cur == 0 && neg == 1)
        {
            if (minI < maxK)
            {
                ret = true;
            }
        }
        cout << "Case #" << qq << ": " << (ret? "YES" : "NO") << endl;
    }

    
    return 0;
}
