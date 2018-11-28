//Pranet Verma
#include <bits/stdc++.h>
using namespace std;
bool state[10];
int _left;
bool process(long long x) {
    do {
        int dig = x % 10;
        if (state[dig] == true) {
            state[dig] = false;
            --_left;
        }
        x /= 10;
    }
    while(x);
    return _left == 0;
}
int main()
{
    int t;
    scanf("%d", &t);
    for (int i = 1; i <= t; ++i) {
        printf("Case #%d: ", i);
        int n;
        scanf("%d", &n);
        memset(state, true, sizeof state);
        _left = 10;
        int limit = 1000000;
        long long curr = n;
        bool found = false;
        while(limit--) {
            if (process(curr)) {
                printf("%lld\n", curr);
                found = true;
                break;
            }
            curr += n;
        }    
        if (!found) {
            printf("INSOMNIA\n");
        }
    } 
}