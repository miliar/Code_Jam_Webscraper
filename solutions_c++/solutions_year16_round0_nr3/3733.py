#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <cstring>

using namespace std;

typedef long long ll;

ll n, k;

string toBin(ll a, ll d) {
    string res="";
    while(d>0) {
        res += a % 2 + '0';
        a /= 2;
        --d;
    }
    reverse(res.begin(), res.end());
    return res;
}

ll fromBin(const string &s, ll base) {
    ll res=0;
    for(ll i=0; i<s.size(); ++i) {
        res = res * base + s[i]-'0';
    }

    return res;
}

#define MAXP 34000000LL
vector<ll> p;
bool e[MAXP];

void erat() {
    memset(e, true, sizeof(e));
    p.clear();
    e[0] = e[1] = false;
    for(ll i=2; i<MAXP; ++i) {
        if (e[i]) {
            p.push_back(i);
            for(ll j = 2*i; j<MAXP; j += i) {
                e[j] = false;
            }
        }
    }
}

ll nums[16];

bool check(ll a) {
    string s = "1" + toBin(a, n-2) + "1";
    for(ll i=2; i<=10; ++i) {
        ll b = fromBin(s, i);
        ll j;
        bool found = false;
        for(j=0; j<p.size() && p[j] * p[j] <= b; ++j) {
            if (b % p[j] == 0) {
                nums[i] = p[j];
                found = true;
                break;
            }
        }
        if (!found) return false;
    }
    return true;
}

int main() {
    freopen("C-small-attempt1.in", "r", stdin);
    freopen("C-small-attempt1.out", "w", stdout);
    ll T;
    cin>>T>>n>>k;
    ll left = k;
    erat();
    printf("Case #1:\n");
    ll cur=0;
    while(left) {
        if (check(cur)) {
            --left;
            cout<<1<<toBin(cur, n-2)<<1;
            for(ll i=2; i<=10; ++i) {
                cout<<" "<<nums[i];
            }
            cout<<endl;
        }
        ++cur;
    }
    return 0;
}
