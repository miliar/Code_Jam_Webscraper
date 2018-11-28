#include <iostream>
#include <cstdio>
using namespace std;

int main() {
    int t; cin >> t;
    for (int i = 1; i <= t; ++i) {
        double v=2,c,f,x; cin >> c >> f >> x;
        double t = x/v, t1, ts = 0;
        do {
            t1 = ts + c/v + x/(v+f);
            if (t1 < t){
                ts += c/v;
                v += f;
                t = t1;
            } else break;
        } while (true);
        printf("Case #%d: %.7f\n", i, t);       
    }
    return 0;
}