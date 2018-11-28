#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

bool is_prime(ll n)
{
    if (n <= 1) {
        return 0;
    }
    for (ll i = 2; i*i <= n; i++) {
        if (n % i == 0) {
            return 0;
        }
    }
    return 1;
}

ll change(string x, ll n)
{
    ll sum = 0;
    for (ll i = 0; i < (ll)x.size(); i++) {
        if (x[i] == '1') {
            sum += pow(n, i);
        }
    }
    return sum;
}

string i2s(ll n, ll N)
{
    string s;
    for (ll i = 0; i < N; i++) {        
        if (n & 1) {
            s += "1";
        } else {
            s += "0";
        }
        n /= 2;
    }
    return s;
}

vector<ll> divisor(ll n)
{
    vector<ll> res;
    for (ll i = 1; i*i <= n; i++) {
	if (n % i == 0) {
	    res.push_back(i);
	    if (i != n/i) res.push_back(n/i);
	}
    }
    sort(res.begin(), res.end());
    res.erase(unique(res.begin(), res.end()), res.end());
    return res;
}

int main()
{
    ll T, N, J;
    
    cin >> T;
    for (int tc = 0; tc < T; tc++) {
        cout << "Case #" << tc+1 << ":" << endl;
        cin >> N >> J;
        N -= 2;
        for (ll i = 0; i < (1<<N); i++) {
            string ii = "1" + i2s(i, N) + "1";
            bool ok = 1;

            vector<ll> v;
            for (ll j = 2; j <= 10; j++) {
                ll x = change(ii, j);
                vector<ll> div = divisor(x);
                if (is_prime(x) || div.size() <= 2) {
                    ok = 0;
                    break;
                }
                v.push_back(div[1]);
            }
            if (ok) {
                reverse(ii.begin(), ii.end());
                cout << ii;
                for (ll j = 0; j < (ll)v.size(); j++) {
                    cout << " " << v[j];
                }
                cout << endl;
                J--;
            }
            if (J == 0) {
                break;
            }
        }
    }
    return 0;
}
