#include <bits/stdc++.h>

using namespace std;
typedef long long ll;
const int N = 1000000;
int hash[3000];
int rec[51][51];
int ans[55];
int main()
{
#ifndef ONLINE_JUDGE  
    freopen("in.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif 
   // ios::sync_with_stdio(0);
    int T, cas = 1;
    scanf("%d", &T);
    while (T--)
    {
        int n, m;
        scanf("%d", &n);
        printf("Case #%d: ", cas++);
        memset(hash, 0, sizeof(hash));
        m = 2 * n - 1;
        for (int i = 0;i < m; i++)
            for (int j = 0;j < n; j++)
               {
                    int x;
                    scanf("%d", &x);
                    hash[x]++;
               }

        int id = 0;
        for (int i = 0;i <= 2500; i++)
            if (hash[i] & 1)
                ans[id++] = i;
        sort(ans, ans + id);
        for (int i = 0;i < id; i++)
            printf("%d%c", ans[i], i == id - 1?'\n':' ');
    }
   
    
    
    return 0;
}