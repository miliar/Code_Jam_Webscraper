// vim:set ts=8 sw=4 et smarttab:
// Qualification Round 2013

#include <cstdio>
#include <cstring>
#include <cassert>
#include <vector>
#include <map>

typedef std::vector<char> vc;

struct my_less
{
    bool operator() (const vc &lhs, const vc &rhs) const
    {
        if (lhs.size() != rhs.size())
            return lhs.size() < rhs.size();
        return lhs < rhs;
    }
};

typedef std::map<vc, int, my_less> table_type;
table_type table;

inline int sq(int a)
{
    return a * a;
}

void print_vc(const vc &v)
{
    for (int i = 0; i < (int)v.size(); ++i)
        printf("%c", v[i]);
    printf("\n");
}

vc make_square(const vc &a)
{
    int n = a.size();
    int m = (n - 1) * 2 + 1;
    vc ret(m);
    for (int k = 0; k < m; ++k)
    {
        int t = 0;
        for (int i = (k >= n - 1 ? k - (n - 1) : 0), j = k - i; i < n && j >= 0; ++i, --j)
            t += (a[i] - '0') * (a[j] - '0');
        assert(t < 10);
        ret[k] = '0' + t;
    }
    for (int i = 0, j = m - 1; i < j; ++i, --j)
        assert(ret[i] == ret[j]);
    return ret;
}

void recur(vc &a, int n, int st, int remain)
{
    if (n % 2 == 1 && st == n / 2)
    {
        int i = st;
        for (int j = 0; sq(j) <= remain; ++j)
        {
            a[i] = '0' + j;
            recur(a, n, st + 1, remain - sq(j));
        }
    }
    else if (st >= n / 2)
    {
        vc key = make_square(a);
        int value = table.size() + 1;
        table[key] = value;
    }
    else
    {
        int i = st;
        for (int j = 0; 2 * sq(j) <= remain; ++j)
        {
            if (st == 0 && j == 0)
                continue;
            a[i] = a[n - 1 - i] = '0' + j;
            recur(a, n, st + 1, remain - 2 * sq(j));
        }
    }
}

void input_vc(vc &v)
{
    char s[102];
    scanf("%s", s);
    int n = strlen(s);
    v.resize(n);
    for (int i = 0; i < n; ++i)
        v[i] = s[i];
}

int solve(const vc &v1, const vc &v2)
{
    table_type::const_iterator it1 = table.lower_bound(v1);
    table_type::const_iterator it2 = table.upper_bound(v2);
    int a, b;
    if (it1 != table.end())
        a = it1->second;
    else
        a = table.size() + 1;
    if (it2 != table.end())
        b = it2->second;
    else
        b = table.size() + 1;
    int ans = b - a;
    return ans;
}

int main()
{
    vc a(1);
    a[0] = '1';
    table[a] = 1;
    a[0] = '4';
    table[a] = 2;
    a[0] = '9';
    table[a] = 3;
    for (int n = 2; n <= 50; ++n)
    {
        vc a(n, '0');
        recur(a, n, 0, 9);
    }

    /*
    for (table_type::const_iterator it = table.begin(); it != table.end(); ++it)
        print_vc(it->first);
    */
    int ntc;
    scanf("%d", &ntc);
    for (int tc = 1; tc <= ntc; ++tc)
    {
        vc v1, v2;
        input_vc(v1);
        input_vc(v2);
        int ans = solve(v1, v2);
        printf("Case #%d: %d\n", tc, ans);
    }
}
