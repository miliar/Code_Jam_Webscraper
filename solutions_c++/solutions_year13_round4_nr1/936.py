#include <iostream>
#include <cstdio>
#include <string.h>
#include <map>
#include <vector>
#include <algorithm>
#define PII pair<int, int>
#define MP make_pair
using namespace std;

const int maxn = 1007, MOD = 1000002013;

int run;
int V, n;

long long calc(long long len)
{
    return len*(V+V-len+1)/2%MOD;
}

void solve()
{
    scanf("%d%d", &V, &n);
    int now = 0, res = 0;
    map<int, int> Map;
    vector< PII > zz;
    for (int i = 1; i <= n; i++)
    {
        int a, b, c;
        scanf("%d%d%d", &a, &b, &c);
        Map[a] += c;
        now += calc(b-a)*c%MOD;
        if (now >= MOD) now -= MOD;
        zz.push_back(MP(b, c));
    }
    sort(zz.begin(), zz.end());
    for (int i = 0; i < zz.size(); i++)
    {
        int x = zz[i].first, p = zz[i].second; 
        while (p > 0)
        {
            map<int, int>::iterator it = Map.upper_bound(x);
            it--;
            int num = min(p, it->second);
            res += calc(x-it->first)*num%MOD;
            if (res >= MOD) res -= MOD;
            p -= num;
            it->second -= num;
            if (it->second == 0) Map.erase(it);
        }
    }
    res = (now-res+MOD)%MOD;
    printf("Case #%d: %d\n", run, res);
}

int main()
{
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small-attempt0.out", "w", stdout);
    int test;
    scanf("%d", &test);
    for (run = 1; run <= test; run++) solve();
    return 0;
}
