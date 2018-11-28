#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
using namespace std;
#define N 100000001
typedef long long ll;
int p[N];
bool v[N];
vector<int> a, ans;
int n, m, nn, s;

bool prime(ll n)
{
    if (n < N)
        return !v[n];
    for (int i = 0; i < s && p[i] * p[i] <= n; ++i)
        if (n % p[i] == 0)
            return 0;
    return 1;
}

ll get_factor(ll n)
{
    for (int i = 0; i < s && p[i] * p[i] <= n; ++i)
        if (n % p[i] == 0)
            return p[i];
    return 1;
}

ll get_base(int b)
{
    int k = a.size();
    ll bb = 1;
    ll s = 0;
    for (int i = 0; i < k; ++i)
    {
        s += a[i] * bb;
        bb *= b;
    }
    return s;
}

void get_base2(int i)
{
    a.clear();
    for (int j = i; j; j >>= 1)
        a.push_back(j & 1);
}

void solve()
{
    scanf("%d%d", &n, &m);
    nn = 1 << n;
    for (int i = 1 << (n - 1); i < nn; ++i)
    {
        if (i % 2 == 0)
            continue;
        if (prime(i))
            continue;
        get_base2(i);
        int j = 3;
        for (; j <= 10; ++j)
        {
            ll k = get_base(j);
            if (prime(k))
                break;
        }
        if (j > 10)
        {
            ans.push_back(i);
            if (ans.size() >= m)
                break;
        }
    }
    m = min(m, (int)ans.size());
    for (int i = 0; i < m; ++i)
    {
        get_base2(ans[i]);
        for (int j = a.size() - 1; j >= 0; --j)
            printf("%d", a[j]);
        printf(" %lld", get_factor(ans[i]));
        for (int j = 3; j <= 10; ++j)
        {
            ll k = get_base(j);
            printf(" %lld", get_factor(k));
        }
        puts("");
    }
}

int main()
{
    for (int i = 2; i < N; ++i)
    {
        if (!v[i]) p[s++] = i;
        for (int j = 0; j < s && i * p[j] < N; ++j)
        {
            v[i * p[j]] = 1;
            if (i % p[j] == 0) break;
        }
    }
    int t;
    freopen("1.txt", "r", stdin);
    freopen("2.txt", "w", stdout);
    scanf("%d", &t);
    for (int tt = 1; tt <= t; ++tt)
    {
        printf("Case #%d:\n", tt);
        solve();
    }
    return 0;
}