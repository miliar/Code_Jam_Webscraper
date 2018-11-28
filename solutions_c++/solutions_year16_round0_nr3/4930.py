#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <cmath>
typedef unsigned long long ull;
using namespace std;
vector<char> is_prime(1000* 1000 * 101, 1);
vector<int> prime;
vector<vector<ull> > p;

bool check_prime(ull val)
{
    if (binary_search(prime.begin(), prime.end(), val))
        return true;
    for (int i = 0; i < prime.size(); ++i)
        if (val % prime[i] == 0)
            return false;
    return true;
}

ull get_val(int mask, int n, int os)
{
    ull val = 0;
    for (int i = 0; i < n; ++i)
        if (mask & (1 << i))
            val += p[os][i];
    return val;
}

bool check(int mask, int n, vector<int>& dels)
{
    dels.clear();
    for (int i = 2; i <= 10; ++i)
    {
        ull val = get_val(mask, n, i);
        if (check_prime(val))
            return false;
        int pos = 0;
        while(val % prime[pos]) ++pos;
        dels.push_back(prime[pos]);
    }
    return true;
}

void solve(int t, int n, int num)
{
    cout << "Case #" << t << ": " << endl;
    vector<int> d(n);
    vector<int> del;
    for (int i = 1 << (n - 1); i < (1 << n); ++i)
    {
            if(i % 2 == 1 && check(i, n, del))
            {
                for (int k = n - 1; k >= 0; --k)
                    cout << (((i & (1 << k)) != 0) ? 1 : 0);
                cout << " ";
                for (int i = 0; i < del.size(); ++i)
                    cout << del[i] << " ";
                cout << endl;
                --num;
                if (num == 0)
                    break;
            }
    }   
}

int main()
{
    p.assign(11, vector<ull>(17, 1));
    for (int i = 2; i < p.size(); ++i)
        for (int j = 1; j < p[0].size(); ++j)
            p[i][j] = i * p[i][j - 1];

    for (int i = 2; i < is_prime.size(); ++i)
    {
        if (is_prime[i])
            for(int j = i * i; j < is_prime.size(); j += i)
                is_prime[j] = 0;
    }
    for (int i = 2; i < is_prime.size(); ++i)
        if (is_prime[i])
            prime.push_back(i);

    int t, n, j;
    cin >> t;
    for (int i = 0; i < t; ++i)
    {
        cin >> n >> j;   
        solve(i + 1, n, j);
    }
}
