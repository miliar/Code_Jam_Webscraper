#include <bits/stdc++.h>
using namespace std;
bool checkPrime(long long x)
{
    for (long long i = 2; i * i <= x; i++)
    {
        if (x % i == 0) return false;
    }
    return true;
}
long long getDivisor(long long x)
{
    for (long long i = 2; i * i <= x; i++)
    {
        if (x % i == 0) return i;
    }
    //assert(0);
}
bool check(string s)
{
    for (long long base = 2; base <= 10; base++)
    {
        long long cur = 0;
        for (long long i = 0; i < (long long)s.length(); i++)
        {
            cur = cur * base + s[i] - '0';
        }
        if (checkPrime(cur)) return false;
    }
    return true;
}
void print(string s)
{
    cout << s << ' ';
    for (long long base = 2; base <= 10; base++)
    {
        long long cur = 0;
        for (long long i = 0; i < (long long)s.length(); i++)
        {
            cur = cur * base + s[i] - '0';
        }
        cout << getDivisor(cur) << ' ';
    }
    cout << endl;
}
string cur;
long long len, need;
vector<string> res;
void gen(long long pos)
{
    if (res.size() == need) return;
    if (pos == len)
    {
        if (check(cur))
        {
            cerr << res.size() << endl;
            res.push_back(cur);
        }
        return;
    }
    if (rand() % 2)
    {
        cur += '1';
        gen(pos + 1);
        cur.resize((long long)cur.size() - 1);
        if (pos != 0 && pos != len - 1)
        {
            cur += '0';
            gen(pos + 1);
            cur.resize((long long)cur.size() - 1);
        }
    }
    else
    {
        if (pos != 0 && pos != len - 1)
        {
            cur += '0';
            gen(pos + 1);
            cur.resize((long long)cur.size() - 1);
        }
        cur += '1';
        gen(pos + 1);
        cur.resize((long long)cur.size() - 1);
    }
}
int main()
{
     //   print("110111");
    freopen("output.txt", "w", stdout);
    long long t;
    cin >> t;
    cin >> len >> need;
    cout << "Case #1:" << endl;
    gen(0);
    for (long long i = 0; i < need; i++)
    {
        for (long long j = 0; j < i; j++)
        {
            assert(res[j] != res[i]);
        }
        print(res[i]);
    }
}
