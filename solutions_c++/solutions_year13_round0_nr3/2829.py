#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <string>
using namespace std;

const int MAXN = 100;

bool check(int num)
{
     int digit[4];
     int len = 0;
     while (num > 0)
     {
           digit[len ++] = num % 10;
           num /= 10;
     }
     for (int i = 0; i < len / 2; ++ i)
         if (digit[i] != digit[len - i - 1])
            return false;
     return true;
}

int work()
{
    int a, b; cin >>a >>b;
    int ans = 0, i = 0;
    while (i * i <= b)
    {
          if (i * i >= a and check(i) and check(i * i)) ++ ans;
          ++ i;
    }
    return ans;
}

int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    
    int T; cin >>T;
    for (int t = 1; t <= T; ++ t)
        printf("Case #%d: %d\n", t, work());
}
