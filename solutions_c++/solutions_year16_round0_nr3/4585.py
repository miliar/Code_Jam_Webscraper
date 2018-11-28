#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef unsigned int uint;

// Calcula (a * b) % mod sem overflow se a <= LLONG_MAX / 2. Complexidade: O(log b).
ll produc_mod(ll a, ll b, ll mod) {
    ll sum = 0;
    while(b) { if(b & 1) sum = (sum + a) % mod; a = (a + a) % mod; b /= 2; }
    return sum;
}

// Calcula (a ^ b) % mod sem overflow se a <= LLONG_MAX / 2. Complexidade: O(log b).
ll exp_mod(ll a, ll b, ll mod) {
    ll prod = 1;
    while(b) { if(b & 1) prod = produc_mod(prod, a, mod); a = produc_mod(a, a, mod); b /= 2; }
    return prod;
}

//Testa se n é primo com o Teste de Miller na base b. Retorna true se n for [pseudo]primo para b.
bool miller(ll n, ll b){
    ll q = n-1, k = 0, r, i = 0;
    while ((q & 1) == 0){
        q >>= 1;
        ++k;
    }
    r = exp_mod(b,q,n);
    if (r == 1) return true;
    while (i < k) {
        if (r == n-1) return true;
        r = produc_mod(r, r, n);
        ++i;
    }
    return false;
}

//Determina se um número é primo usando o teste de Miller para 4 bases (determinístico para n < 10^12).
bool isprime(long long n){
    const int n_bases = 4;
    int j, bases[] = {2, 13, 23, 1662803};
    if (n < 0) n = -n;
    if (n <= 1) return false;
    for (j = 0; j < n_bases; ++j) {
        if (n == bases[j]) return true;
        if (n % bases[j] == 0) return false;
        if (!miller(n, bases[j])) return false;
    }
    return true;
}

ll gcd(ll a, ll b) {
    return b == 0 ? a : gcd(b, a % b);
}

ll pollard_rho(ll n) {
    while (true) {
        int i = 1;
        ll x = rand() % (n-1) + 1, y = x, k = 2, d;
        do {
            i++; d = gcd(n + y - x, n);
            if(d > 1 && d < n) {
                return d;
            }
            if(i == k) y = x, k *= 2;
            x = (produc_mod(x, x, n) + 2) % n;
        } while(y != x);
    }
}

ll prime[100], top = 0;
// Fatora n usando o Pollard-Rho. Complexidade esperada: O(n^(1/4)).
void factorize(ll n) {
    if (isprime(n)) prime[top++] = n;
    else {
        ll div = pollard_rho(n);
        if (isprime(div)) prime[top++] = div;
        else factorize(div);
        if (isprime(n / div)) prime[top++] = n / div;
        else factorize(n / div);
    }
}

string conv(ull n){
    string s = "";
    while (n){
        if (n&1) s += '1';
        else s += '0';
        n >>= 1;
    }
    return string(s.rbegin(), s.rend());
}

vector< pair< uint, vector<ull> > > big_table;

int main(){
    int t, cases = 1;

    uint max = (1ULL<<16)-1;
    uint begin = (1ULL<<15)+1;
    for (uint i = begin; i <= max; i+=2){
        bool ok = true;
        vector<ull> div;
        for (int j = 2; j <= 10; j++){
            uint mask = i;
            ull exp = 1, n = 0;
            while (mask){
                n += (mask&1) * exp;
                exp *= j;
                mask >>= 1;
            }
            if (isprime(n)){
                ok = false;
                break;
            }
            div.push_back(pollard_rho(n));
        }

        if (ok){
            big_table.push_back( make_pair(i, div) );
            if (big_table.size() == 50) break;
        }

    }

    /*cout << "pre computation DONE" << endl;

    cout << " total size: " << big_table.size() << endl;
    for (int i = 0; i < big_table.size(); i++){
        cout << "mask: " << big_table[i].first << " size of entry: " << big_table[i].second.size() << endl;
        cout << "divisors: " << endl;
        for (int j = 0; j < big_table[i].second.size(); j++)
            cout << big_table[i].second[j] << " ";
        cout << endl;
    }*/

    t = 1;
    while (t--){
    
        cout << "Case #" << cases++ << ": " << endl;

        for (int i = 0; i < big_table.size(); i++){
            cout << conv(big_table[i].first);
            for (int j = 0; j < big_table[i].second.size(); j++)
                cout << " " << big_table[i].second[j];
            cout << endl;
        }
    }
    return 0;
}
