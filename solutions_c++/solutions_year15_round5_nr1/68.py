#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

int a[1000000];
int b[1000000];
int c[1000000];
vector <int> v[1000000];
vector <int> w[1000000];

int dfs(int x)
{
    int ans = 1, i;
    
    c[x] = 1;
    
    for (i = 0; i < v[x].size(); i++) {
        if (b[v[x][i]] == 1) ans += dfs(v[x][i]);
    }
    
    return ans;
}

int dfs2(int x)
{
    int ans = 1, i;
    
    b[x] = c[x] = 0;
    
    for (i = 0; i < v[x].size(); i++) {
        if (b[v[x][i]] == 1) ans += dfs2(v[x][i]);
    }
    
    return ans;
}

int main()
{
    int t, i;
    
    scanf("%d", &t);
    
    for (i = 0; i < t; i++) {
        int n, d, s0, as, cs, rs, m0, am, cm, rm, ans = 0, sum = 0, j, k;
        vector <pair<int, int> > z;
        
        scanf("%d %d", &n, &d);
        scanf("%d %d %d %d", &s0, &as, &cs, &rs);
        scanf("%d %d %d %d", &m0, &am, &cm, &rm);
        
        for (j = 0; j < n; j++) {
            b[j] = c[j] = 0;
            v[j].clear();
            w[j].clear();
        }
        
        a[0] = s0;
        
        for (j = 1; j < n; j++) a[j] = ((long long)a[j - 1] * as + cs) % rs;
        
        for (j = 1; j < n; j++) {
            m0 = ((long long)m0 * am + cm) % rm;
            
            v[m0 % j].push_back(j);
            w[j].push_back(m0 % j);
        }
        
        for (j = 0; j < n; j++) z.push_back(make_pair(a[j], j));
        
        sort(z.begin(), z.end());
        
        for (k = 0; k < n; k++) {
            int x = z[k].second;
            
            if (z[k].first > z[0].first + d) break;
            
            b[x] = 1;
            
            if (x == 0 || c[w[x][0]] == 1) sum += dfs(x);
            
            ans = max(ans, sum);
        }
        
        for (j = 0; j < n; j++) {
            int x = z[j].second;
            
            b[x] = 0;
            
            if (c[x] == 1) sum -= dfs2(x);
            
            for (; k < n; k++) {
                int x = z[k].second;
                
                if (z[k].first > z[j + 1].first + d) break;
                
                b[x] = 1;
                
                if (x == 0 || c[w[x][0]] == 1) sum += dfs(x);
                
                ans = max(ans, sum);
            }
        }
        
        printf("Case #%d: %d\n", i + 1, ans);
    }
    
    return 0;
}
