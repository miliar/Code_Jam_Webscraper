#include <iostream>

using namespace std;

int main() {
    int T,t;
    scanf("%d",&T);
    t = T;
    while (T--) {
        int count = 0,c=0, i=1;
        unsigned long long N,temp;
        bool a[10] = {false,};
        scanf("%lld", &N);
        if (!N) { printf("Case #%d: INSOMNIA\n", t-T); continue; }
        for (i = 1; count < 10; ++i) {
            temp = i*N;
            c = count;
            while (temp > 0) {
                if (!a[temp%10]) {
                    count++;
                    a[temp%10] = true;
                }
                temp /= 10;
            }
        }
        printf("Case #%d: %lld\n", t-T, (i-1)*N);
    }
}