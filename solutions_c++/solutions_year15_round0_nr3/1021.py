#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>

using namespace std;

const int MAXL = (int)1e4;
const int MAXLEN = 10000;

typedef long long ll;

int line[MAXL];

constexpr int gn(char c) 
{
    return c == 'i' ? 2 :
        c == 'j' ? 3 :
        c == 'k' ? 4 : 100;
}

int mul_table[4][4] = {
   { 1, gn('i'), gn('j'), gn('k') },
   { gn('i'), -1, gn('k'), -gn('j') },
   { gn('j'), -gn('k'), -1, gn('i') },
   { gn('k'), gn('j'), -gn('i'), -1 },
};


int mul(int a, int b)
{
    if (a * b == 0)
        return 0;
    int mul = 1;
    if (a < 0) mul *= -1;
    if (b < 0) mul *= -1;
    a = abs(a);
    b = abs(b);
    return mul * mul_table[a - 1][b - 1];
}

int pow(int base, ll deg)
{
    int ret = 1;
    for ( ; deg; deg >>= 1)
    {
        if (deg & 1)
            ret = mul(ret, base);
        base = mul(base, base);
    }

    return ret;
}

int nums[] = {
   gn('i'), gn('j'), gn('k'), 1,
   -gn('i'), -gn('j'), -gn('k'), -1,
};

int getA(int b, int c)
{
    if (count_if(begin(nums), end(nums), [=](int a) { return mul(a, b) == c; }) != 1)
        cerr << "bad" << endl;
    for (auto a : nums)
        if (mul(a, b) == c)
            return a;
    return 0;
}

int getB(int a, int c)
{
    if (count_if(begin(nums), end(nums), [=](int b) { return mul(a, b) == c; }) != 1)
        cerr << "bad" << endl;
    for (auto b : nums)
        if (mul(a, b) == c)
            return b;
    return 0;
}


bool check(int len, ll times)
{   
    int r = std::accumulate(line, line + len, 1, mul);
    if (r == 1 || pow(r, times) != -1) 
        return false;
    
    map<int, int> pows;

    int pw = 0;
    pows[1] = pw++;
    int x = 1;
    while (pw <= times && pows.count(x = mul(x, r)) == 0)
        pows[x] = pw++;
    
    ll tot_len = len * times;

    ll mini = numeric_limits<ll>::max();

    int cur = 1;
    for (int i = 0; i < len; i++)
    {
        cur = mul(cur, line[i]);
        if (cur == gn('i'))
        {
            mini = i;
            break;
        }   
        int a = getA(cur, gn('i'));
        if (pows.count(a))
            mini = min(mini, 1LL * len * pows[a] + i);
    }

    cur = 1;
    ll maxk = numeric_limits<ll>::min();

    for (int i = 0; i < len; i++)
    {
        cur = mul(line[len - i - 1], cur);
        if (cur == gn('k'))
        {
            maxk = tot_len - i - 1;
            break;
        }
        int b = getB(cur, gn('k'));
        if (pows.count(b))
            maxk = max(maxk, tot_len - len * pows[b] - i - 1);
    }

    return maxk > mini + 1;
}

int main()
{
    int t;
    cin >> t;
    for (int test = 0; test < t; test++)
    {
        cout << "Case #" << test + 1 << ": ";
        int l;
        ll x;
        string s;
        cin >> l >> x >> s;
        transform(begin(s), end(s), line, gn);
        
        cout << (check(l, x) ? "YES" : "NO") << endl;

    }

    return 0;
}
