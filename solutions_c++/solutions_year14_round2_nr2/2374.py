#include <iostream>
#include <cstdio>
#include <string>
#include <algorithm>
#include <vector>
#include <memory.h>

using namespace std;
int main() {
    int _tc;
    cin >> _tc;

    for (int tc=1; tc<=_tc; tc++) {
        int A,B,K;
        cin >> A >> B >> K;

        int tr = 0;
        for (int a=0; a<A; a++) {
            for (int b=0; b<B; b++) {
                if ((a & b) < K)
                    tr++;
            }
        }

        printf("Case #%d: %d\n", tc, tr);
    }
}