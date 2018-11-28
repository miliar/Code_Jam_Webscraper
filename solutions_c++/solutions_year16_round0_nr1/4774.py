#include <iostream>
#include <cstdio>
#include <vector>
#include <fstream>

using namespace std;

int main() {
    int T, x;
    freopen("A-large.in","r",stdin);
    freopen("Alarge.out","w",stdout);
    scanf("%d", &T);
    for (int t = 1; t <= T; t++) {
        int  ct = 0;
        long long cur = 0, x;
        scanf("%lld", &x);
        vector<int> hashdig(10, 0);
        cur = x;
        while (ct != 10 && cur) {

            long long tmp = cur;
            while (cur) {
                if (!hashdig[ cur % 10 ])
                    hashdig[ cur % 10 ] = 1, ct++;
                cur /= 10;
            }

            cur = tmp + x;
        }

        if (ct != 10)
            printf("Case #%d: INSOMNIA\n", t);
        else
            printf("Case #%d: %lld\n", t, cur - x);


    }



    return 0;
}
