#include <bits/stdc++.h>
#define ll long long
#define ld long double
#define mp make_pair
#define pb push_back
#define ull unsigned ll
#define F first
#define S second
#define y1 sflgdfgfasdf
#define exp adfhsalkjdfglkjsdfhglkjsdhfgjkhsdkfjghslkdfhglksdfhgkljsdfhgksjdhfgjkhsdflkghsdlkfghlksdfjhglksdfjglksdjfh

using namespace std;

const ll MIN = 1e3 + 2;
const ll MXN = 1e6 + 3;
const ll INF = 1e9 + 7;
const ll LINF = 1e18 + 15;
const ld EPS = 1e-9;

ll n;
string st;

int main(){
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    cin >> n;
    for (ll i = 1; i <= n; i++){
        ll ans1 = 0;
        cin >> st;
        cout << "Case #" << i << ": ";
        for (ll j = 0; j < st.size(); j++){
            if (j != 0 && st[j] != st[j - 1]){
                ans1++;
            }
        }
        if (st[st.size() - 1] == '-')
            ans1++;
        cout << ans1 << "\n";
    }
    return 0;
}
