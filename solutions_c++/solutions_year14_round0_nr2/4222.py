#include <iostream>
#include <stdio.h>
#include <vector>
#include <math.h>

using namespace std;

int T;
double C, F, X;
int main() {
    freopen("cookie.in","r",stdin);
    freopen("cookie.out","w",stdout);
    cin >> T;
    int caseNumber = 1;
    while(T-- > 0) {
        cin >> C >> F >> X;
        double speed = 2, pre = 0, ret = 1e30;
        for(int itr = 0; itr < 100100; itr++) {
            ret = min(ret, pre + X / speed);
            pre += C / speed;
            speed += F;
        }
        printf("Case #%d: %.10f\n", caseNumber++, ret);
    }
    return 0;
}
