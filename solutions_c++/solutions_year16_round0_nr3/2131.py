#include <bits/stdc++.h>

using namespace std;

void solution();

int main()
{
    ios_base::sync_with_stdio(false);
#ifdef HOME
    freopen("C.in", "rt", stdin);
    clock_t start = clock();
#endif
    solution();
#ifdef HOME
    cerr.precision(3);
    cerr << endl << "Total time: " << fixed << double(clock() - start) / double(CLOCKS_PER_SEC) << endl;
#endif
    return 0;
}

//typedef long long ll;
typedef __int128 ll;
#define int __int128

istream& operator>> (istream& in, __int128& value)
{
    value = 0;
    char ch = 0;
    while (!isdigit(ch))
        ch = in.get();
    while (isdigit(ch))
    {
        if (ch >= '0' && ch <= '9')
            value = value * 10 + (ch - '0');
        ch = in.get();
    }
    return in;
}

ostream& operator<< (ostream& out, __int128 value)
{
    if (value == 0)
    {
        string s = "0";
        out << s;
        return out;
    }
    string s;
    if (value < 0)
    {
        value = -value;
        s += '-';
    }
    while (value > 0)
    {
        s += char('0' + value % 10);
        value /= 10;
    }
    reverse(s.begin(), s.end());
    assert(!s.empty());
    out << s;
    return out;
}

int n, j;

inline void print(int mask)
{
    string s;
    while (mask > 0)
    {
        s += char('0' + (mask & 1));
        mask >>= int(1);
    }
    reverse(s.begin(), s.end());
    cout << s;
}

inline int to_base(int mask, const int& base)
{
    int p = 1;
    int val = 0;
    while (mask > 0)
    {
        if (mask & 1)
            val += p;
        p *= base;
        mask >>= int(1);
    }
    return val;
}

#define N 10000000
bool pr[N + 1];
int p[N + 1], pc = 0;

void precalc()
{
    cerr << "Size of int128: " << sizeof(__int128) << endl;
    if (sizeof(__int128) <= 4)
        exit(0);
    for (int i = 2; i <= N; ++i)
        pr[i] = true;
    for (int i = 2; i + i <= N; ++i)
        if (pr[i])
            for (int j = i + i; j <= N; j += i)
                pr[j] = false;
    for (int i = 2; i <= N; ++i)
        if (pr[i])
            p[pc++] = i;
    for (int i = 0; i < 10; ++i)
        cerr << p[i] << " ";
    cerr << endl;
}

inline int first_divider(const int& x)
{
    //for (int i = 2; i * i <= x; ++i)
    for (int i = 0; i < pc && p[i] * p[i] <= x; ++i)
        if (x % p[i] == 0)
            return p[i];
    return -1;
}

void solve()
{
    int cnt = 0;
    for (int _mask = 0; _mask < (1 << (n - 2)); ++_mask)
    {
        int mask = (int(1) << int(n - 1)) | (_mask << int(1)) | int(1);
        vector<int> d;
        for (int base = 2; base <= 10; ++base)
        {
            int x = to_base(mask, base);
            int y = first_divider(x);
            if (y > 1 && y < x)
            {
                assert(x % y == 0);
                d.push_back(y);
            }
        }
        /*if (mask % 1024 == 0)
        {
            cerr << "mask: " << mask << " " << cnt << "/" << j << endl;
        }*/
        if (d.size() < 9)
            continue;
        print(mask);
        for (int i = 0; i < 9; ++i)
            cout << " " << d[i];
        cout << endl;
        if (cnt % 1 == 0)
            cerr << cnt << "/" << j << endl;
        ++cnt;
        if (cnt == j)
            break;
    }
}

void solution()
{
    precalc();
    int T;
    cin >> T;
    cerr << "T: " << T << endl;
    for (int t = 0; t < T; ++t)
    {
        cin >> n >> j;
        cerr << "n: " << n << " j: " << j << endl;
        cout << "Case #" << t + 1 << ":" << endl;
        solve();
    }
}
