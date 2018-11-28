#include <iostream>
#include <fstream>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <set>
#include <algorithm>
#include <map>
#include <queue>
#include <stack>
using namespace std;

typedef long long ll;
#define I 2
#define J 3
#define K 4

// i - 2, j - 3, k - 4
int O[5][5] = {
    {0,  0,  0,  0,  0, },
    {0,  1,  2,  3,  4, },
    {0,  2, -1,  4, -3, },
    {0,  3, -4, -1,  2, },
    {0,  4,  3, -2, -1, },
};

ll n, k;
string s;

int mul(int x, int y)
{
    bool neg = ((x < 0) ^ (y < 0));
    int val = O[abs(x)][abs(y)];
    return val * (neg ? -1 : 1);
}

int gety(int x, int z)
{
    for(int y = 1; y <= 4; y++) if(abs(O[abs(x)][y]) == abs(z))
    {
        int val = O[abs(x)][y] * (x < 0 ? -1 : 1);
        bool neg = (z == val * -1);
        return y * (neg ? -1 : 1);
    }
}

#define MAXN 11111

int a[MAXN];
int pref[MAXN], suf[MAXN];
int full[5];
map< pair< pair<int, int>, pair<int, int> >, bool > can;

bool solve()
{
    for(int i = 0; i < n; i++) a[i] = (s[i] == 'i' ? 2 : (s[i] == 'j' ? 3 : 4));
    pref[0] = a[0];
    for(int i = 1; i < n; i++) pref[i] = mul(pref[i - 1], a[i]);
    suf[0] = pref[n - 1];
    for(int i = 1; i < n; i++) suf[i] = gety(pref[i - 1], pref[n - 1]);

    full[1] = pref[n - 1];
    for(int i = 2; i <= 4; i++) full[i] = mul(full[i - 1], full[1]);
    full[0] = full[4];

    can.clear();
    for(int i = -1; i < n; i++)
    {
        for(int c1 = 0; c1 <= 3; c1++) for(int c2 = 0; c2 <= 3; c2++)
        {
            int left = mul(full[c1], (i >= 0 ? pref[i] : 1));
            int right = mul((i + 1 < n ? suf[i + 1] : 1), full[c2]);
            can[{{c1, c2}, {left, right}}] = true;
        }
    }

    for(int i = 0; i < n; i++) for(int c0 = 0; c0 <= 3; c0++)
    {
        int first = mul(full[c0], pref[i]);
        if(first == I)
        {
            for(int c1 = 0; c1 <= 3; c1++)
            {
                if(k < c0 + c1 + 2) continue;
                int c2 = (k - 2 - c0 - c1) % 4;
                int need1 = gety((i + 1 < n ? suf[i + 1] : 1), J);
                if(can[{{c1, c2}, {need1, K}}]) return true;
            }
        }
    }

    for(int i = 0; i + 1 < n; i++) for(int c0 = 0; c0 <= 3; c0++)
    {
        int first = mul(full[c0], pref[i]);
        if(first == I)
        {
            if(k < c0 + 1) continue;
            int c2 = (k - c0 - 1) % 4;
            for(int j = i + 2; j < n; j++)
            {
                if(mul(suf[j], full[c2]) == K and mul(suf[i + 1], full[c2]) == mul(J, K)) return true;
            }
            if(suf[i + 1] == J and full[c2] == K) return true;
        }
    }


    //for(int i = 0; i < n; i++) cout << a[i] << " "; cout << endl;
    //for(int i = 0; i < n; i++) cout << pref[i] << " "; cout << endl;
    //for(int i = 0; i < n; i++) cout << suf[i] << " "; cout << endl;


    return false;
}

int main()
{
    freopen("c2.in", "r", stdin);
    freopen("c2.out", "w", stdout);
    int testcnt;
    cin >> testcnt;
    for(int i = 1; i <= testcnt; i++)
    {
        cin >> n >> k >> s;
        bool ans = solve();
        printf("Case #%d: ", i);
        cout << (ans ? "YES" : "NO") << endl;
    }
}
