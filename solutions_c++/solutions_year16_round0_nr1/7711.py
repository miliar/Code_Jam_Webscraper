#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int TT;
    cin >> TT;

    for (int T = 1; T <= TT; ++T)
    {
       long long x, ans, t;
       bool flag[10];
       int cnt = 0;
       cin >> x;
       ans = x;
       memset(flag, 0, sizeof(flag));
       if (ans == 0)
       {
           cout << "Case #" << T << ": INSOMNIA" << endl;
           continue;
       }
       while (ans <= 1000000000000ll)
       {
           t = ans;
           while (t > 0)
           {
               int digit = t % 10;
               if (!flag[digit])
               {
                   ++cnt;
                   flag[digit] = 1;
               }
               t /= 10;
           }

           if (cnt == 10)
           {
               cout << "Case #" << T << ": " << ans << endl;
               break;
           }
           ans += x;
       }

       if (ans >= 1000000000000ll)
           cerr << "ERROR!!" << endl;
    }

    fclose(stdin);
    fclose(stdout);
}
