#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <string>
using namespace std;

const int MAXN = 100;

string work()
{
     int n, m, map[MAXN][MAXN];
     int max_n[MAXN], max_m[MAXN];
     
     cin >>n >>m;
     
     for (int i = 0; i < n; ++ i)
         max_n[i] = 0;
     for (int i = 0; i < m; ++ i)
         max_m[i] = 0;
     
     for (int i = 0; i < n; ++ i)
         for (int j = 0; j < m; ++ j)
         {
             cin >>map[i][j];
             if (map[i][j] > max_n[i]) max_n[i] = map[i][j];
             if (map[i][j] > max_m[j]) max_m[j] = map[i][j];
         }
     
     for (int i = 0; i < n; ++ i)
         for (int j = 0; j < m; ++ j)
             if (map[i][j] < max_n[i] and map[i][j] < max_m[j])
                return "NO";
     
     return "YES";
}

int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    
    int T; cin >>T;
    for (int t = 1; t <= T; ++ t)
        printf("Case #%d: %s\n", t, work().c_str());
}
