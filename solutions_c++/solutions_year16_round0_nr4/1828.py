#pragma comment(linker, ”/STACK:36777216“)
#include<bits/stdc++.h>

#define x first
#define y second
#define y0 hi1
#define y1 hi2
#define ll long long
#define mp make_pair
#define pb push_back
#define sqr(a) (a)*(a)
#define ld long double
#define all(a) (a).begin(), (a).end()

using namespace std;

const int inf = 2000000000;

ll power(ll a, ll b){
    if(b == 0)return 1;
    if(b % 2)return a * power(a, b - 1);
    ll f = power(a, b / 2);
    return f * f;
}

ll a[100][100];

int main(){
    cin.tie(0);
    ios_base::sync_with_stdio(0);
    freopen("D-small-attempt2.in", "r", stdin);
    freopen("D-small-attempt2.out", "w", stdout);
    int T;
    cin >> T;
    for(int num = 1; num <= T; num++){
        cout << "Case #" << num << ": ";
        ll k, c, s;
        cin >> k >> c >> s;
        if(k == 1){
            cout << "1\n";
            continue;
        }
        if(k == s){
            for(int j = 2; j <= k; j++){
                a[1][j] = 1;
            }

            for(int i = 2; i <= c; i++){
                for(int j = 2; j <= k; j++){
                    a[i][j] = (a[i - 1][j] - 1) * k + k + 1;
                }
            }
            ll f = 1;
            cout << f << " ";
            for(int i = 2; i <= s; i++){
                f = f + a[c][i];
                cout << f << " ";
            }
        }
        cout << "\n";
    }
}
