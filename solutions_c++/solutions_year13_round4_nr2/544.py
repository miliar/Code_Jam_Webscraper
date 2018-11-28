#include <iostream>
#include <vector>
#include <string>
#include <cstring>
using namespace std;

const int MAXN = 1100;
const int INF = 1000000000;

long long pow2(long long a) {
    long long ans = 1;
    for (int i = 1; i <= a; ++i) ans += ans;
    return ans;
};


int main() {
    int tt;
    cin >> tt;
    for (int ttt = 1; ttt <= tt; ++ttt) {
        long long a, b, ans1, ans2;
        cin >> a >> b;
        long long tmpb = b, c = pow2(a - 1);
        if (b == c * 2 || b == c * 2 - 1) {
            ans1 = b - 1;
        } else
        if (b > c) {
            ans1 = 2;
            while (c > 0 && b > c) {
                b -= c;
                c /= 2;
                ans1 += ans1;
            }
            ans1 -= 2;
        } else {
            ans1 = 0;
        } 
        
        b = tmpb;
        
        long long p = 0, tmp = 1;
        while (b >= tmp) {
            ++p;
            tmp += tmp;
        }
        --p;
        
        ans2 = pow2(a) - pow2(a - p);
        
        cout << "Case #" << ttt << ": " << ans1 << " " << ans2 << endl;
    }

    return 0;
}
