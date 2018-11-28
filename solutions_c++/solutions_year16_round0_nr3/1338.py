#include <bits/stdc++.h>

using namespace std;

bool check1(long long mask){
    return mask & 1;
}

bool try_to_get_divisor(long long mask, long long k, long long c){
    long long bp = 0;
    long long cur = 1LL;
    for (int j = 0; j < 32; ++j){
        if (mask & (1LL << (long long)j)) bp = (bp + cur) % c;
        cur = (cur * k) % c;
    }
    return !bp;
}

long long calc_mask(long long mask, long long k){
    long long c = 1LL;
    bool can = true;
    long long res = 0LL;
    for (long long i = 0LL; i < 32LL; ++i){
        if (mask & (1LL << i)){
            if (!can) return (long long)1e18;
            res += c;
        }
        c *= k;
        if (c > 1e9) can = false;
    }
    return res;
}

int find_divisor(long long mask, long long k){
    long long n = min(calc_mask(mask, k), 101LL);
    for (int i = 2; i < n; ++i){
        if (try_to_get_divisor(mask, k, i)) return i;
    }
    return -1;
}

void print_mask(long long mask){
    bool was = false;
    for (int i = 32; i >= 0; --i){
        if (was) cout << (mask & (1LL << (long long)i) ? 1 : 0);
        else {
            if (mask & (1LL << (long long)i)){
                was = true;
                cout << (mask & (1LL << (long long)i) ? 1 : 0);
            }
        }
    }
    cout << " ";
}

int main()
{
    freopen("C-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    cin >> t;
    for (int tt = 0; tt < t; ++tt){
        int LEN, J, cnt = 0; cin >> LEN >> J;
        cout << "Case #" << t << ": " << endl;
        for (long long mask = (1LL << (long long)(LEN - 1)); mask < (1LL << (long long)LEN); ++mask){
            if (!check1(mask)) continue;
            bool ok = true;
            for (int i = 2; i <= 10; ++i){
                long long res = find_divisor(mask, i);
                if (res == -1LL) {ok = false; break;}
            }
            if (ok) {
                cnt++;
                print_mask(mask);
                for (int i = 2; i <= 10; ++i){
                    long long res = find_divisor(mask, i);
                    cout << res << " ";
                }
                cout << endl;
            }
            if (cnt >= J) break;
        }
    }
    return 0;
}
