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

int N, a;

int main() {
#ifdef __APPLE__
    ifstream cin("/Users/byunghoon/Desktop/Programs/Programs/in.txt");
    ofstream cout("/Users/byunghoon/Desktop/Programs/Programs/out.txt");
#endif
    
    cin >> N;
    for (int i = 0; i < N; i++) {
        cin >> a;
        if (a == 0) cout << "Case #" << i+1 << ": INSOMNIA" << endl;
        else {
            vb seen(10, false);
            int seenC = 0;
            ll j;
            for (j = 1; ; j++) {
                ll temp = a * j;
                while (temp > 0) {
                    if (!seen[temp % 10]) {
                        seenC++;
                        seen[temp % 10] = true;
                    }
                    temp /= 10;
                }
                if (seenC == 10) break;
            }
            cout << "Case #" << i+1 << ": " << a*j << endl;
        }
    }
    
    return 0;
}