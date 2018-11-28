#include <cstdio>
#include <algorithm>

using namespace std;

int main()
{
    int t, i;
    
    scanf("%d", &t);
    
    for (i = 0; i < t; i++) {
        int n, j;
        long long p, x, y, l, r, m;
        
        scanf("%d %lld", &n, &p);
        
        p--;
        
        l = 0, r = 1LL << n, m = (l + r) / 2;
        
        while (r - l > 1) {
            long long a = m, c = 0;
            
            for (j = 0; a > 0; j++) {
                c += 1LL << (n - j - 1);
                a = (a - 1) / 2;
            }
            
            if (c <= p) {
                l = m;
                m = (l + r) / 2;
            } else {
                r = m;
                m = (l + r) / 2;
            }
        }
        
        x = l;
        
        l = 0, r = 1LL << n, m = (l + r) / 2;
        
        while (r - l > 1) {
            long long a = (1LL << n) - m - 1, c = (1LL << n) - 1;
            
            for (j = 0; a > 0; j++) {
                c -= 1LL << (n - j - 1);
                a = (a - 1) / 2;
            }
            
            if (c <= p) {
                l = m;
                m = (l + r) / 2;
            } else {
                r = m;
                m = (l + r) / 2;
            }
        }
        
        y = l;
        
        printf("Case #%d: %lld %lld\n", i + 1, x, y);
    }
    
    return 0;
}
