#include <stdio.h>
#include <stdlib.h>
#include <math.h>

bool fair(int x)
{
     int w[100];
     int t = 0;
     while (x!=0){
           w[t++] = x%10;
           x/=10;      
     }
     for (int i = 0, j = t-1; i<j; ++i, --j)
         if (w[i]!=w[j]) return false;
     return true;
 }
 
bool check(int x)
{
     if (x != (int)(floor(sqrt(x)) * floor(sqrt(x)))) return false;
     if (fair(x) && fair((int)(floor(sqrt(x)) + (1e-7)))) return true; else return false;     
}
     
int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int cases, i = 0;
    scanf("%d", &cases);
    while (cases--){
          ++i;
          int a, b;
          printf("Case #%d: ", i);
          scanf("%d%d", &a, &b);
          int t = 0;
          for (int i = a; i <= b; ++i)
              if (check(i)) ++t;
          printf("%d\n", t);          
    }
    return 0;
}
