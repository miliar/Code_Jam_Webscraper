#include <bits/stdc++.h>

using namespace std;

typedef pair<int, int> pii;
typedef pair<long long, long long> pll;
#define MP make_pair
#define F first
#define S second

const int N = 1001;

template<class Tsum, class Tval>
class BIT
{
    vector<Tval> f;

public:
    void initialize(int n)
    {
        f.assign(n, 0);
    }

    void initialize(vector<Tval> values)
    {
        f.assign(values.size(), 0);
        for (int i = 0; i < f.size(); ++i)
            update(i, values[i]);
    }

    void update(int pos, Tval add)
    {
        for (; pos < f.size(); pos = (pos | (pos + 1)))
            f[pos] += add;
    }

    Tsum getSum(int pos)
    {
        Tsum res = 0;
        for (; pos >= 0; pos = (pos & (pos + 1)) - 1)
            res += (Tsum)f[pos];
        return res;
    }

    Tsum getSum(int L, int R)
    {
        return getSum(R) - getSum(L - 1);
    }
};

BIT<int, int> tree;

int inv(const vector<int> &v)
{
    int res = 0;
    tree.initialize(N + 1);
    for (int i = 0; i < v.size(); i++)
    {
        res += tree.getSum(N - v[i]);
        tree.update(N - v[i], 1);
    }
    return res;
}

/*int inv2(const vector<int> &v)
{
    int res = 0;
    for (int i = 0; i < v.size(); i++)
        for (int j = 0; j < i; j++)
            if (v[j] > v[i])
                res++;
    return res;
}*/

void solve(int test)
{
    int n;
    cin >> n;
    vector<int> v(n);
    for (int i = 0; i < n; i++)
        cin >> v[i];
    vector<int> x = v;
    sort(x.begin(), x.end());
    for (int i = 0; i < v.size(); i++)
        v[i] = lower_bound(x.begin(), x.end(), v[i]) - x.begin();
    int res = 0;
    int l = 0;
    int r = n - 1;
    for (int i = 0; i < n; i++)
    {
        int j = 0;
        while (v[j] != i)
            j++;
        int fl = j - l;
        int fr = r - j;
        if (fl <= fr)
        {
            for (int p = j; p > l; p--)
            {
                res++;
                swap(v[p], v[p - 1]);
            }
            l++;
        }
        else
        {
            for (int p = j; p < r; p++)
            {
                res++;
                swap(v[p], v[p + 1]);
            }
            r--;
        }
    }
    cout << "Case #" << test << ": ";
    cout << res << "\n";
}

int main()
{
    ios_base::sync_with_stdio(0);
    #ifdef TEST
        freopen("input.txt", "r", stdin);
        freopen("output.txt", "w", stdout);
    #endif

    cout.setf(ios::fixed);
    cout.precision(10);
    cerr.setf(ios::fixed);
    cerr.precision(10);

    int t;
    cin >> t;
    for (int q = 1; q <= t; q++)
        solve(q);

    return 0;
}
