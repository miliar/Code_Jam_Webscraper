#include <bits/stdc++.h>

using namespace std;

int cases;

typedef long long ll;

ll n, tmp;
int mask;

const int DEST = 0x000003FF;

bool check() {
    return (DEST&mask) == DEST;
}

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    ios_base::sync_with_stdio(0);
    cin >> cases;
    for(int CASE = 1 ; cases-- ; ++CASE) {
        cin >> n;
        cout << "Case #" << CASE << ": ";
        if(n == 0) cout << "INSOMNIA";
        else {
            mask = 0;
            for(int j = 1 ;; ++j) {
                tmp = n*j*1LL;
                while(tmp) {
                    mask |= (1 << (tmp%10));
                    tmp /= 10;
                }
                if(check()) {
                    cout << n*j*1LL;
                    break;
                }
            }
        }
        cout << endl;
    }
}
