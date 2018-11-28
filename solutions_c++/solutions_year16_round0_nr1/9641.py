#include <iostream>
#include <cstdio>
#include <queue>
#include <set>
#include <map>

using namespace std;

#define LL long long

int main() {
#ifdef _CONSOLE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w+", stdout);
#endif
    
    int digit[] = {1, 3, 7, 9};
    int t; scanf("%d", &t);
    for(int i = 1; i <= t; ++i) {
        
        LL n; scanf("%lld", &n);
        

        if(n == 0) {
            printf("Case #%d: INSOMNIA\n", i);
            continue;
        }
        
        LL ans = 0;
        vector<bool> cache(10, false);
        while(true) {
            bool ok = true;
            for(int j = 0; j < 10; ++j) {
                if(cache[j] == false)
                    ok = false;
            }
            if(ok) break;
            ans += n;
            LL temp = ans;
            while(temp) {
                cache[temp % 10] = true;
                temp /= 10;
            }
        }
        printf("Case #%d: %lld\n", i, ans);
    }
    return 0;
}
