#include <iostream>
#include <vector>
#include <deque>
#include <cstdio>
#include <climits>
#include <cstring>
using namespace std;

#define ll long long

int main() {
    int T;
    cin>>T;

    for (int t=1;t<=T;++t) {
        int N;
        long double V, X;
        cin>>N>>V>>X;
        long double R[100], C[100];

        for (int i=0;i<N;++i) {
            cin>>R[i]>>C[i];
        }

        long double ans = 0;
        bool impossible = false;
        if (N == 1) {
            if (C[0] == X) {
                ans = V / R[0];
            } else {
                impossible = true;
            }
        } else {
            if (C[0] == C[1]) {
                if (C[0] == X) {
                    ans = V / (R[0]+ R[1]);
                } else {
                    impossible = true;
                }
            } else if (C[0] == X) {
                ans = V / R[0];
            } else if (C[1] == X) {
                ans = V / R[1];
            } else {
                long double a = (V * X - V * C[1]) / (C[0] - C[1]);
                long double b = V - a;
                if (a < 0 || b < 0) impossible = true;
                else ans = max(a / R[0], b / R[1]);
            }
        }


        // a+b = V;
        // (a*Ca + b*Cb) / (a+b) = X
        // a*Ca + b*Cb = a*X + b*X
        // a*Ca + (V-a)*Cb = a*X + (V-a)*X
        // a*Ca - a*Cb = -V*Cb + V*X
        // a = (V*X - V*Cb) / (Ca - Cb)


        if (impossible) {
            printf("Case #%d: IMPOSSIBLE\n", t);
        } else {
            printf("Case #%d: %.16Lf\n", t, ans);
        }
    }
}
