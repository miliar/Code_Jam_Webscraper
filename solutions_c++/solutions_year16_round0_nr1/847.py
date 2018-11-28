#include<bits/stdc++.h>
typedef long double ld;
typedef long long ll;
typedef unsigned long long ull;
typedef unsigned int uint;
using namespace std;

int digitMask[1000000];
int ans[1000001];

int getDigitMask(ll x) {
    if (x < 1000000) {
        return digitMask[x];
    }

    int mask = 0;
    do {
        mask |= digitMask[x % 1000000];
        x /= 1000000;
    } while(x);
    return mask;
}


int main() {
    #ifdef LOCAL
    freopen(".in", "r", stdin);
    freopen(".out", "w", stdout);
    #endif    	   	

    for (int i = 0; i < 10; ++i) digitMask[i] = 1 << i;
    for (int i = 10; i < 1000000; ++i) digitMask[i] = digitMask[i / 10] | (1 << (i % 10));

    for (int i = 1; i <= 1000000; ++i) {
        int mask = 0, it = 1;
        while (1) {
            mask |= getDigitMask(i * it);
            if (mask == 1023) {
                break;
            }
            ++it;
        }
        ans[i] = i * it;
        assert(ans[i] <= 100000000);
    }


    int n;
    cin >> n;
    for (int ti = 1; ti <= n; ++ti) {
        int x;
        cin >> x;        
        cout << "Case #" << ti << ": ";
        if (x == 0) {
            cout << "INSOMNIA\n";
        } else {
            cout << ans[x] << "\n";
        }
    }

    return 0;
}
