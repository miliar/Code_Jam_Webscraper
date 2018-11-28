#include <cstdio>
#include <algorithm>

using namespace std;

int main()
{
    int t, i;
    
    scanf("%d", &t);
    
    for (i = 0; i < t; i++) {
        int n, k, m;
        long long b, l, r, m1, m2, sum1, sum2, j;
        double ans = 0, tmp1, tmp2, tmp3, tmp4;
        long long a[37] = {0};
        long long p[37];
        long long q[37];
        
        scanf("%lld %d", &b, &n);
        
        for (j = 0; j < n; j++) scanf("%lld", &a[j]);
        
        sort(a, a + 37);
        
        l = 0, r = 1e15;
        
        while (r - l > 1) {
            sum1 = sum2 = 0;
            tmp1 = tmp2 = 0;
            
            for (j = 0; j < 37; j++) p[j] = q[j] = 0;
            
            m1 = l + (r - l) / 3;
            m2 = l + (r - l) / 3 * 2;
            
            if (m1 < l || m2 >= r || m1 >= m2) break;
            
            for (j = 0; j < 37; j++) {
                if (a[j] < m1) {
                    p[j] = m1 - a[j];
                    sum1 += m1 - a[j];
                }
                
                if (a[j] < m2) {
                    q[j] = m2 - a[j];
                    sum2 += m2 - a[j];
                }
            }
            
            if (sum2 > b) {
                r = m2;
                
                continue;
            }
            
            for (j = 1; j <= 37; j++) {
                int c = 0;
                
                tmp3 = 0;
                
                for (k = j; k < 37; k++) {
                    if (a[k] <= m1) c++;
                }
                
                if (sum1 + c > b) continue;
                
                for (k = 0; k < j; k++) {
                    if (a[k] <= m1) tmp3 += p[k] * 36;
                }
                
                tmp3 /= j;
                
                tmp3 -= sum1 + c;
                
                tmp1 = max(tmp1, tmp3);
            }
            
            for (j = 1; j <= 37; j++) {
                int c = 0;
                
                tmp4 = 0;
                
                for (k = j; k < 37; k++) {
                    if (a[k] <= m2) c++;
                }
                
                if (sum2 + c > b) continue;
                
                for (k = 0; k < j; k++) {
                    if (a[k] <= m2) tmp4 += q[k] * 36;
                }
                
                tmp4 /= j;
                
                tmp4 -= sum2 + c;
                
                tmp2 = max(tmp2, tmp4);
            }
            
            if (tmp2 < 0 || tmp1 > tmp2) {
                r = m2;
            } else {
                l = m1;
            }
        }
        
        for (j = l; j < r; j++) {
            sum1 = 0;
            tmp1 = 0;
            
            for (k = 0; k < 37; k++) p[k] = 0;
            
            for (k = 0; k < 37; k++) {
                if (a[k] < j) {
                    p[k] = j - a[k];
                    sum1 += j - a[k];
                }
            }
            
            if (sum1 > b) break;
            
            for (k = 1; k <= 37; k++) {
                int c = 0;
                
                tmp3 = 0;
                
                for (m = k; m < 37; m++) {
                    if (a[m] <= j) c++;
                }
                
                if (sum1 + c > b) continue;
                
                for (m = 0; m < k; m++) {
                    if (a[m] <= j) tmp3 += p[m] * 36;
                }
                
                tmp3 /= k;
                
                tmp3 -= sum1 + c;
                
                tmp1 = max(tmp1, tmp3);
            }
            
            ans = max(ans, tmp1);
        }
        
        printf("Case #%d: %.12lf\n", i + 1, ans);
    }
    
    return 0;
}
