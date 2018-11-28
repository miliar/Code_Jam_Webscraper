#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

int a[1000];

int main()
{
    int t, i;
    
    scanf("%d", &t);
    
    for (i = 0; i < t; i++) {
        int n, k, ans, sum = 0, m = 1e9, c1 = 0, c2 = 0, j, l;
        vector <pair<int, int> > v;
        
        scanf("%d %d", &n, &k);
        
        for (j = 0; j < n - k + 1; j++) scanf("%d", &a[j]);
        
        for (j = 0; j < k; j++) {
            int x = 0, y = 0, z = 0;
            
            for (l = j; l + 1 < n - k + 1; l += k) {
                z += a[l + 1] - a[l];
                x = min(x, z);
                y = max(y, z);
            }
            
            m = min(m, x);
            c1 = max(c1, y - x);
            
            v.push_back(make_pair(x, y));
        }
        
        for (j = 0; j < v.size(); j++) sum += m - v[j].first;
        
        for (j = 0; j < v.size(); j++) c2 += c1 - v[j].second + v[j].first;
        
        while (sum >= a[0]) sum -= v.size();
        
        while (sum <= a[0]) sum += v.size();
        
        sum -= v.size();
        sum += c2;
        ans = c1;
        
        if (sum < a[0]) {
            ans += (a[0] - sum + v.size() - 2) / (v.size() - 1);
        }
        
        printf("Case #%d: %d\n", i + 1, ans);
    }
    
    return 0;
}
