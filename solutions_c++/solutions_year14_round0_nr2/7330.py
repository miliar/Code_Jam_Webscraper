#include <iostream>
#include <cstdio>
using namespace std;
double C, F, X;
int main() {
    int T; cin >> T;
    for(int i = 1; i <= T; i++) {
        cin >> C >> F >> X;
        double now = 0, v = 2, time = 0;
        while(now < X) {
            if(C >= X) {
                time = X / v;
                break;
            }
            if(now < C) {
                time += (C - now) / v;
                now = C;
            }else {
                if((X - now) / v > (X - now + C) / (v + F)) {
                    now -= C;
                    v += F;
                }else {
                    time += (X - now) / v;
                    now = X;
                }
            }
        }
        cout << "Case #" << i << ": ";
        printf("%.7lf\n", time);
    }
    return 0;
}
