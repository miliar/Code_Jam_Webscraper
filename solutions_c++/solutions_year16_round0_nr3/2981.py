#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <set>
#include <stdlib.h>     /* srand, rand */
#include <time.h>       /* time */
#define MAX 1000000
using namespace std;
typedef unsigned long long int ll;

bool is_prime[MAX];
vector<ll> primes;

struct Coin {
    ll val;
    vector<ll> proofs;
};

bool operator== (Coin const& lhs, Coin const& rhs){
    return lhs.val == rhs.val;
}

bool operator< (Coin const& lhs, Coin const& rhs){
    return lhs.val < rhs.val;
}

ll pow(ll a, ll b) {
    if (b == 0) {
        return 1;
    } else {
        ll tmp = pow(a, b/2);
        if (b % 2 == 0) {
            return tmp*tmp;
        } else {
            return tmp*tmp*a;
        }
    }
}

ll toNum(string& a, ll base) {
    int n = a.size();
    ll num = 0;
    for (int i = 0; i < n; ++i) {
        if (a[i] == '1') {
            num += pow(base, n - i - 1);
        }
    }
    return num;
}

string genString(int n) {
    string ans(n, '1');
    for (int i = 1; i < n-1; ++i) {
        if (rand() % 2) {
            ans[i] = '0';
        }
    }
    return ans;
}

void sieve() {
    for (int i = 2; i < MAX; ++i) {
        is_prime[i] = true;
    }
    is_prime[0] = false;
    is_prime[1] = false;
    for (int i = 2; i*i <= MAX; ++i) {
        if (is_prime[i]) {
            for (int j = 2*i; j < MAX; j += i) {
                is_prime[j] = false;
            }
        }
    }
    for (int i = 2; i < MAX; ++i) {
        if (is_prime[i]) {
            primes.push_back(i);
        }
    }
}

ll checkPrime(Coin& a) {
    for (int i = 0; i < primes.size(); ++i) {
        if (a.val != primes[i] && a.val % primes[i] == 0) {
            return primes[i];
        }
    }
    return -1;
}

int main() {
    sieve();
    srand (time(NULL));
    int t;
    cin >> t;
    for (int kase = 1; kase <= t; ++kase) {
		int n,j;
        cin >> n >> j;
        set<Coin> coins;
        while (coins.size() < j) {
            string tmp = genString(n);
            Coin cn;
            for (int i = 2; i <= 10; ++i) {
                cn.val = toNum(tmp, i);
                ll pf = checkPrime(cn);
                if (pf != -1) {
                    cn.proofs.push_back(pf);
                } else {
                    break;
                }
            }
            if (cn.proofs.size() == 9) {
                coins.insert(cn);
            }
        }
		printf("Case #%d:\n", kase);
        for (auto it = coins.begin(); it != coins.end(); ++it) {
            cout << it->val;
            for (int i = 0; i < 9; ++i){
                cout << " " << it->proofs[i];
            }
            cout << endl;
        }
    }
    return 0;
}