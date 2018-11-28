#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

double dp[2][401];

double calc(vector <double>& v) {
    int i, j, k;
    
    for (i = 0; i < 2; i++) {
        for (j = 0; j <= 400; j++) {
            dp[i][j] = 0;
        }
    }
    
    dp[0][200] = 1;
    
    for (i = 0; i < v.size(); i++) {
        for (j = 0; j <= 400; j++) {
            if (dp[0][j] == 0) continue;
            
            dp[1][j - 1] += dp[0][j] * (1 - v[i]);
            dp[1][j + 1] += dp[0][j] * v[i];
        }
        
        for (j = 0; j <= 400; j++) {
            dp[0][j] = dp[1][j];
            dp[1][j] = 0;
        }
    }
    
    return dp[0][200];
}

int main() {
    int t, i;
    
    scanf("%d", &t);
    
    for (i = 0; i < t; i++) {
        int n, k, j, l;
        double ans = 0;
        vector <double> v;
        
        scanf("%d %d", &n, &k);
        
        for (j = 0; j < n; j++) {
            double x;
            
            scanf("%lf", &x);
            
            v.push_back(x);
        }
        
        sort(v.begin(), v.end());
        
        for (j = 0; j <= k; j++) {
            vector <double> w;
            
            for (l = 0; l < j; l++) w.push_back(v[l]);
            for (l = n - k + j; l < n; l++) w.push_back(v[l]);
            
            ans = max(ans, calc(w));
        }
        
        printf("Case #%d: %.12lf\n", i + 1, ans);
    }
    
    return 0;
}
