#include <iostream>
#include <cstdio>

using namespace std;

int match(int v) {
    int matched = 0;
    while (v) {
        matched |= 1 << (v%10);
        v /= 10;
    }
    return matched;
}

int main() {
    int T;
    cin>>T;
    for (int t=1;t<=T;++t) {
        int N;
        cin>>N;

        if (N == 0) {
            printf("Case #%d: INSOMNIA\n", t);
        } else {

            int matched = 0;
            int cur = N;
            while (matched != (1<<10)-1) {
                matched |= match(cur);
                cur += N;
            }

            printf("Case #%d: %d\n", t, cur - N);
        }
    }
}
