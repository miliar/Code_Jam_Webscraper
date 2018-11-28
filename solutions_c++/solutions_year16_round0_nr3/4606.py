#include<bits/stdc++.h>
using namespace std;
bool prime[10000001];
vector < string > v;
int n;
void sieve()
{

    for(int i = 0; i<=1000000; i++)prime[i] =1;

    prime[0] = prime[1] = 0;

    for(int i = 2 ; i <= sqrt(10000001); i++)
        if(prime[i])
        {

            for(int j = 2; i*j<=(10000000); j++)prime[i * j] = 0;
        }

}
bool isprime(long long x)
{
    for (int i = 2 ; i <= 10000000 ; i++ )
    {
        if (x % i == 0)
            return 0;
    }
    return 1;
}
long long power( int base, int p)
{
    long long res = 1;
    for (int i = 1 ; i <= p ; i++ )
        res *= base;
    return res;
}
string fromDecimal(long long N, long long base)
{
    string res;
    while(N)
    {
        res += char('0' + (N % base));
        N /= base;
    }
    reverse(res.begin(),res.end());
    return res;
}
long long toDecimal(long long N, string s, int base)
{
    stringstream ss;
    if (s == "*")
    {
        ss << N ;
        ss >> s;
        ss.clear();
    }
    int sz = int(s.size()) ;
    long long res = 0, j = 0;
    for (int i = sz - 1 ; i >= 0 ; i--)
    {
        res += ((s[i] == '1') * power(base, j));
        j ++ ;
    }
    return res;
}
void BitMask(int i, string s = "")
{
    if (i == (n - 2))
    {
        s = '1' + s + '1';
        int x = toDecimal(1,s, 2);
        if (!prime[x])
            v.push_back(s);
        return;
    }
    BitMask(i + 1, s + '0');
    BitMask(i + 1, s + '1');
}
long long getD(long long x)
{
    for (int i = 2 ; i < x ; i++ ) /// not to submit large as this
    {
        if (x % i == 0)
            return i;
    }
}
int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    freopen("in.txt", "rt", stdin);
    freopen("out.txt", "wt", stdout);

    sieve();

    int t;
    cin >> t;
    for (int i = 1 ; i <= t ; i++ )
    {
        cout << "Case #" << i << ":\n";
        int jj;
        cin >> n >> jj;
        BitMask(0,"");
        for (int j = 0 ; j < v.size() ; j++ )
        {
            if (!jj) break;
            vector < long long > res;

            long long base10 = toDecimal(1,v[j], 2);
            int m = getD(base10);
            res.push_back(m);
            for (int b = 3 ; b <= 10 ; b++)
            {
                res.push_back(toDecimal(1,v[j],b));
            }
            int check = 1;
            for (int idx = 1 ; idx < res.size() ; idx ++ )
            {
                if (res[idx] < 10000001)
                {
                    if (prime[res[idx]])
                        check = 0;
                    break;
                }
                else
                {
                    if (isprime(res[idx]))
                    {
                        check = 0;
                        break;
                    }
                }
            }
            if (check)
            {
                --jj;
                cout << v[j] << " ";
                for (int idx = 0 ; idx < res.size() ; idx ++)
                {
                    cout << getD(res[idx]);
                    if (idx != 9)
                        cout << " ";
                }
                cout << "\n";
            }
        }
        v.clear();
       // cout << "\n";
    }
}
