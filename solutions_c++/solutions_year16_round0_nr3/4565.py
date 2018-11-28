#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <cstdio>
#include <cmath>
#include <vector>
#include <map>
#include <string>
#include <cstdlib>
#include <limits>
#include <algorithm>

using namespace std;

using llg = long long;


vector<pair<string, vector<llg> > > ans;

llg to_base(llg x, llg base, int n)
{
    llg ans = 0, tbase = 1;
    for (int i = 0; i < n; i++)
    {
        if (x & (1LL << i))
            ans += tbase;
        tbase *= base;
    }
    return ans;
}

llg primes[] = { 2, 3, 5, 7, 11, 13, 17, 19, 23 };

llg is_prime(llg x)
{
    if (x == 2)
        return 1;
    if (!(x & 1))
        return 2;

    for (llg i = 3; i * i <= x; i += 2)
    {
        if (x % i == 0)
            return i;
    }
    return 1;
}

string binary(llg x)
{
    string str;
    while (x > 0)
    {
        str += '0' + (x & 1);
        x >>= 1;
    }
    reverse(str.begin(), str.end());
    return str;
}

bool check(llg x, int n)
{
    vector<llg> dividors;
    llg res, divd;
    for (int i = 2; i <= 10; i++)
    {
        res = to_base(x, i, n);
        divd = is_prime(res);
        if (divd == 1)
            return false;
        dividors.push_back(divd);
    }
    ans.push_back(make_pair(binary(x), dividors));
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int n, j, cases;
    cin >> cases >> n >> j;

    cout << "Case #1:" << endl;

    llg maxn = 1LL << (n - 2), tmp;



    for (llg i = 0; i < maxn; i++)
    {
        tmp = (1LL << (n - 1)) | (i << 1) | 1;
        if (check(tmp, n))
            j--;
        if (j == 0)
            break;
    }

    for (auto& vt : ans)
    {
        cout << vt.first << ' ';
        for (int i = 0; i < 9; i++)
            cout << vt.second[i] << ' ';
        cout << endl;
    }

    fclose(stdin);
    fclose(stdout);
    return 0;
}