#include <iostream>
#include <map>
#include <set>
#include <vector>
#include <cstring>
#include <string>

using namespace std;

typedef vector<int> vi;

int a[10][10];
int max_in_row[10];
int max_in_col[10];

int main()
{
    freopen("b.in", "r", stdin);
    freopen("b.out", "w", stdout);
    
    int t;
    cin >> t;
    for (int cnt = 1; cnt <= t; ++cnt)
    {
       // printf("Case #%d:\n", cnt);
       int n, m;
       cin >> n >> m;
       // cout << n << " " << m << endl;
       for (int i = 0; i < n; ++i)
       {
           for (int j = 0; j < m; ++j)
           {
               scanf("%d", &a[i][j]);
               // printf("%d ", a[i][j]);
           }
           // printf("\n");
       }
       // printf("\n");
       
       memset(max_in_row, 0, sizeof(max_in_row));
       memset(max_in_col, 0, sizeof(max_in_col));
       for (int i = 0; i < n; ++i)
           for (int j = 0; j < m; ++j)
           {
               if (a[i][j] > max_in_row[i])
               {
                   max_in_row[i] = a[i][j];
               }

               if (a[i][j] > max_in_col[j])
               {
                   max_in_col[j] = a[i][j];
               }
           }

       bool flag = true;
       for (int i = 0; i < n; ++i)
           for (int j = 0; j < m; ++j)
           {
               if (a[i][j] < max_in_row[i] && a[i][j] < max_in_col[j])
               {
                   flag = false;
               }
           }
       printf("Case #%d: ", cnt);
       if (flag)
           printf("YES\n");
       else
           printf("NO\n");
           
    }
    return 0;
}