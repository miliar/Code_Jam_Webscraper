#include <iostream>
#include <cstdio>
#include <vector>
#include <cmath>
#include <algorithm>
#include <ctime>
#include <cstdlib>
#include <set>


using namespace std;


typedef long long LL;


LL gcd(LL a, LL b) {
    if (a == 0) {
        return b;
    }
    return gcd(b % a, a);
}


int main() {
    freopen("input", "r", stdin);
    freopen("output", "w", stdout);
    int t;
    cin >> t;
    for (int q = 0; q < t; ++q) {
        cout << "Case #" << q + 1 << ": ";
        LL x, y;
        scanf("%I64d/%I64d", &x, &y);
        //cout << x << y << endl;
        LL g = gcd(x, y);
        x /= g;
        y /= g;
        //cout << y << endl;
        LL c = 0;
        bool flag = true;
        for (; ; ) {
            if (y == 1) {
                break;
            }
            if (y % 2 == 1) {
                flag = false;
                break;
            }
            ++c;
            y /= 2;
            //cout << y << endl;
        } 
        //cout << "#" << endl;
        if (!flag) {
            cout << "impossible" << endl;
            continue;
        }
        y = (1 << c);
        c = 0;
        for (; y > x; y /= 2, ++c);
        cout << c << endl;
    }
    return 0;
}