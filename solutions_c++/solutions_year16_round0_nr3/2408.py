#include <bits/stdc++.h>
#include <stdio.h>
#include "a.h"

using namespace std;
typedef long long ll;

const int N = 16;
const int J = 50;

ll divisor[9];

string to_string(ll n, ll b)
{
    string res;
    do {    
        res += '0'+n%b;
        n /= b;
    }while(n);
    reverse(res.begin(), res.end());
    return res;
}

ll to_ll(const string& str, ll b) 
{
    ll res = 0ll;
    for (auto ch : str)
        res = res*b + ch-'0';
    return res;
}

bool test_format(const string &str) {
    if (str.length() != N) return false;
    if (str.front() != '1' || str.back() != '1') return false;
    for (auto ch : str) 
        if (ch != '0' && ch != '1') return false;
    return true;
}

bool test_format(ll n, ll b) {
    string str = to_string(n, b);
    if (!test_format(str)) return false;
    return true;
}

ll is_prime(ll n) 
{
    for (auto p : primes) {
        if (n % p == 0) return p;
        if (p*p > n) break;
    }
    return -1;
}

bool test(const string& str)
{
    for (ll b=2; b<=10; ++b) {
        ll m = to_ll(str, b);
        if ((divisor[b-1]=is_prime(m)) < 0) 
            return false;
    }
    return true;
}

void gen()
{
    int cnt = 0;
    string can(N, '1');
    for (ll i=0; i<(1<<(N-2)); ++i) {
        for (int j=0; j<N-2; ++j)
            can[j+1] = (i&(1<<j))?'1':'0';
        if (test(can)) {
            cout << can << " ";
            for (int k=1; k<10; ++k)
                printf("%lld%c", divisor[k], k==9?'\n': ' ');
            if (++cnt == J) return;
        }
    }
}

int main()
{
    printf("Case #1:\n");
    gen();
    return 0;
}