#include <bits/stdc++.h>

#define uint unsigned int
#define INF 999999999
#define LINF 999999999999999999
#define ll long long
#define ld long double
#define M 1000000007
#define E 0.0000001
#define N (1<<17)
#define pii pair<int, int>
#define pll pair<long long, long long>
#define pdd pair<double, double>
#define ull unsigned long long
#define C 'a'

using namespace std;

ll prime(ll k) {
    for (ll i = 2; i * i <= k; i++) {
        if (k % i == 0) return i;
    }
    return 0;
}

ll tobase (vector<ll> n, ll k) {
    ll sum = 0;
    ll mult = 1;
    for (int i = 0; i < n.size(); i++) {
        sum += mult * (n[n.size() - i - 1]);
        mult *= k;
    }
    return sum;
}

int main() {
    //ifstream in("google.in");
    ofstream out("small.out");
    int t = 1;
    //in>>t;
    out<<"Case #1:"<<endl;
    for (int c = 1; c <= t; c++) {
        int n = 16;
        int j = 50;
        int foo = 0;
        ll i = 0;
        while (foo != j) {
            ll ti = (1<<(n - 1)) | (i<<1) | 1;
            vector<ll> v(n);
            vector<ll> q;
            for (int i = 0; i < n; i++) {
                v[n - i - 1] = ti % 2;
                ti /= 2;
            }
            for (int i = 2; i <= 10; i++) {
                ll lol = prime(tobase(v, i));
                if (lol) {
                    q.push_back(lol);
                } else break;
            }
            if (q.size() == 9) {
                foo++;
                for (int x : v) out<<x;
                out<<" ";
                for (ll x : q) out<<x<<" ";
                out<<endl;
                cout<<foo<<"/"<<j<<endl;
            }
            i++;
        }
    }
    out.close();
}
