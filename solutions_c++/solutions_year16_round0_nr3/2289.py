#include <bits/stdc++.h>

using namespace std;

vector<unsigned long long> primes;

unsigned long long fpow(unsigned long long a,unsigned long long n)
{
    unsigned long long result = 1;
    unsigned long long power = n;
    unsigned long long value = a;
    while(power>0)
    {
        if(power&1)
            result = result*value;
        value = value*value;
        power /= 2;
    }
    return result;
}

void sieve(int n)
{
    bool prime[n+1];
    memset(prime, true, sizeof(prime));

    for (int p=2; p*p<=n; p++)
    {
        if (prime[p] == true)
        {
            for (int i=p*2; i<=n; i += p)
                prime[i] = false;
        }
    }

    for (int p=2; p<=n; p++)
        if (prime[p])
            primes.push_back(p);
}

int found = 0;
int n, j;

void solve (string s)
{
    if (s.size() >= n || found == j) return;

    if (s.size() == n - 1)
    {
        s += '1';
        unsigned long long intr[11];
        unsigned long long ex[11];
        memset(ex, -1, sizeof(ex));
        for (int i = 2; i <= 10; i++)
        {
            intr[i] = 0;
            int p = 0;
            for (int j = s.size() - 1; j >= 0; j--)
                intr[i] += (unsigned long long)(s[j] - '0') * fpow(i, p++);
        }

        //for (int i = 2; i < 11; i++) cout << intr[i] << " ";
        //cout << endl;

        bool diva = true;
        for (int i = 2; i <= 10; i++)
        {
            bool div = true;
            for (int j = 0; j < primes.size(); j++)
                if (!(intr[i]%primes[j]) && intr[i] != primes[j])
                {
                    ex[i] = primes[j];
                    break;
                }
            if (ex[i] == -1) div = false;
            diva = min(div, diva);
        }
        if (diva)
        {
            cout << s << " ";
            for (int i = 2; i <= 10; i++) cout << ex[i] << " ";
            cout << endl;
            found++;
        }
    }
    else
    {
        solve(s + '1');
        solve(s + '0');
    }
}


int main()
{
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("output.out", "w", stdout);
    sieve(100000);
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++)
    {
        cin >> n >> j;
        cout << "Case #" << i << ":" << endl;
        solve("1");
    }
    return 0;
}
