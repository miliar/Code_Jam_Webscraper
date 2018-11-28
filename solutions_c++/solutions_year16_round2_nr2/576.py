#include <iostream>
#include <cstdio>
#include <queue>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <utility>
#include <ctime>
#include <cassert>

#define F first
#define S second
#define pb push_back
#define mp make_pair

using namespace std;

typedef unsigned long long ll;
typedef pair <int, int> pii;
typedef pair <ll, ll> pll;

const int maxn = (int)1e6 + 10;
const int inf = (int)1e9;
const int mod = (int)1e9 + 7;
const ll INF = (ll)1e19;
const double eps = (int)1e-9;

char f[20], s[20], F[20], S[20];
int n;

void check(ll &diff, int pos, int ok)
{
    for (int i = 0; i < pos; ++i)
    {
        if (f[i] != '?' && s[i] == '?')
            s[i] = f[i];
        if (s[i] != '?' && f[i] == '?')
            f[i] = s[i];
        if (f[i] == '?' && s[i] == '?')
            s[i] = f[i] = '0';
        if (f[i] != s[i]) return;
    }
    
    if (pos == n)
    {
        for (int i = 0; i < n; ++i)
            F[i] = f[i];
        for (int i = 0; i < n; ++i)
            S[i] = s[i];
        return;
    }
    
    if (f[pos] != '?' && s[pos] == '?')
        s[pos] = f[pos] + ok;
    if (s[pos] != '?' && f[pos] == '?')
        f[pos] = s[pos] - ok;
    if (f[pos] == '?' && s[pos] == '?')
    {
        if (ok == -1)
            s[pos] = '0', f[pos] = '1';
        else
            s[pos] = '1', f[pos] = '0';
    }
    if (f[pos] == s[pos]) return;
    if (s[pos] < '0' || s[pos] > '9') return;
    if (f[pos] < '0' || f[pos] > '9') return;
    
    
    for (int i = pos + 1; i < n; ++i)
    {
        if (f[i] != '?' && s[i] == '?')
        {
            if (ok == -1)
                s[i] = '9';
            else
                s[i] = '0';
        }
        if (s[i] != '?' && f[i] == '?')
        {
            if (ok == 1)
                f[i] = '9';
            else
                f[i] = '0';
        }
        if (f[i] == '?' && s[i] == '?')
        {
            if (ok == -1)
                s[i] = '9', f[i] = '0';
            else
                s[i] = '0', f[i] = '9';
        }
    }
    
    ll ff = 0, ss = 0;
    
    for (int i = 0; i < n; ++i)
    {
        ff = ff * 10 + f[i] - '0';
        ss = ss * 10 + s[i] - '0';
    }
    
    if (ok == -1)
    {
        if (ff - ss < diff
            || (ff - ss == diff
                && (memcmp(f, F, n) < 0
                    || (memcmp(f, F, n) == 0
                        && memcmp(s, S, n) < 0))))
        {
            diff = ff - ss;
            for (int i = 0; i < n; ++i)
                F[i] = f[i], S[i] = s[i];
        }
    }
    else
    {
        if (ss - ff < diff
            || (ss - ff == diff
                && (memcmp(f, F, n) < 0
                    || (memcmp(f, F, n) == 0
                        && memcmp(s, S, n) < 0))))
        {
            diff = ss - ff;
            for (int i = 0; i < n; ++i)
                F[i] = f[i], S[i] = s[i];
        }
    }
    return;
}

void solve()
{
    char ff[20], ss[20];
    scanf("%s", ff);
    scanf("%s", ss);
    n = strlen(ff);
    
    ll diff = INF;
    for (int i = 0; i <= n; ++i)
        for (int ok = -1; ok < 2; ok += 2)
        {
            for (int j = 0; j < n; ++j)
                f[j] = ff[j], s[j] = ss[j];
            check(diff, i, ok);
        }
    
    F[n] = S[n] = 0;
    return;
}


int main()
{
    int test;
    scanf("%d", &test);
    for (int i = 0; i < test; ++i)
    {
        solve();
        printf("Case #%d: %s %s\n", i + 1, F, S);
    }
    return 0;
}