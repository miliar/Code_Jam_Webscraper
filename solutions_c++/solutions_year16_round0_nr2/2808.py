#include <bits/stdc++.h>

using namespace std;

typedef pair<int, int> ii;
typedef pair<ii, int> iii;
typedef pair<ii, ii> iiii;
typedef pair<int, bool> ib;
typedef vector<bool> vb;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef vector<vb> vvb;
typedef vector<vi> vvi;
typedef vector<vii> vvii;
typedef long long ll;
typedef pair<ll, ll> pll;
typedef vector<ll> vll;
typedef vector<pll> vpll;

int N;
string cake;

ll solve(int to, bool flip) {
    //printf("solve(%s)\n", cake.substr(0, to+1).c_str());
    ll ans = 0;
    for (int j = to; j >= 0; j--) {
        if (cake[j] == (flip ? '+' : '-')) {
            ans = solve(j-1, !flip) + 1;
            break;
        }
    }
    return ans;
}

int main() {
#ifdef __APPLE__
    ifstream cin("/Users/byunghoon/Desktop/Programs/Programs/in.txt");
    ofstream cout("/Users/byunghoon/Desktop/Programs/Programs/out.txt");
#endif
    
    cin >> N;
    for (int i = 0; i < N; i++) {
        cin >> cake;
        ll a = solve((int) cake.length() - 1, false);
        cout << "Case #" << i+1 << ": " << a << endl;
    }
    
    return 0;
}