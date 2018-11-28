#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <string>
#include <cstring>
#include <map>
#include <set>
#include <vector>

const int N = 1e5+3;
const int inf = 1e9;

typedef long long ll;

using namespace std;

double p[N];
vector<vector<int>> f;
bool solve()
{
    int n,k;
    scanf("%d%d",&n,&k);
    for (int i = 0; i < n; ++i)
        scanf("%lf", &p[i]);
    
    int M = 1<<k;
    vector<int> v(k);
    f.clear();
    for (int ms = 0; ms < M; ++ms) {
        int t=  0;
        for (int i = 0; i < k; ++i)
            if (ms >> i & 1) t++;
        if (t*2 == k) {
            for (int i = 0; i < k; ++i)
                if (ms >> i & 1)
                    v[i] = 1;
                else
                    v[i] = -1;
            f.push_back(v);
        }
    }
//    for (int i = 0; i < f.size(); ++i) {
//        for (int x : f[i])
//            printf("%d ",x);
//        puts("");
//    }
    
    M = 1<<n;
    double ans=0;
    for (int ms = 1; ms < M; ++ms) {
        int t=  0;
        for (int i = 0; i < n; ++i)
            if (ms >> i & 1) t++;
        if (t != k)
            continue;
        t = 0;
        for (int i = 0; i < n; ++i)
            if (ms >> i & 1)
                v[t++] = i;
        double d = 0;
        for (int i = 0; i < f.size(); ++i) {
            double x = 1.;
            for (int j = 0; j < f[i].size(); ++j)
                if (f[i][j] < 0)
                    x *= (1. - p[v[j]]);
                else
                    x *= p[v[j]];
            d += x;
        }
        //printf("%d %.3f\n", ms, d);
        ans = max(ans, d);
    }
    printf("%.9f\n", ans);
    return false;
}

int main()
{
        freopen("input.txt","r", stdin);
        freopen("output.txt", "w", stdout);
    int countTests;
    scanf("%d", &countTests);
    for (int curTest = 1; curTest <= countTests; ++curTest) {
        printf("Case #%d: ", curTest);
        solve();
    }
    
    return 0;
}
