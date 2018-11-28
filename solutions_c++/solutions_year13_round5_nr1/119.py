#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>

using namespace std;

#define LL long long

LL B;
int _n;
LL a[100];
int n = 37;
const LL inf = 40000000000000;



int main()
{
    freopen("al.in", "r", stdin);
    freopen("alout.txt", "w", stdout);
    int T, ca = 0;
  //  scanf("%d", &T);
    cin >> T;
    while (T--)
    {
        for (int k = 1; k <= n; k++)
            a[k] = 0;
        a[n + 1] = inf;
        //scanf("%I64d", &B);
        cin >> B;
       // scanf("%d", &_n);
       cin >> _n;
        for (int i = 1; i <= _n; i++)
        {
            LL tmp;
          //  scanf("%I64d", &tmp);
            cin >> tmp;
            a[i] = tmp;
        }
        sort(a + 1, a + 1 + n);
        LL L = 0, R = inf;
        while (L < R)
        {
            LL mid = (L + R) >> 1;
            LL temp = 0;
            for (int k = 1; k <= n; k++)
                if (a[k] < mid)
                    temp += mid - a[k];
            if (temp > B) R = mid;
            else L = mid + 1;
        }
   long double ans = 0;
        for (LL num = max(0LL, L - 100); num <= L + 100; num++)
        {
          long  double ans0 = 0;
            LL b;
            for (int cnt = 1; cnt <= n; cnt++)
            {
                b = B;
                int flag = 0;
                for (int i = 1; i <= cnt; i++)
                    if (a[i] > num) flag = 1;
                if (flag == 1) continue;
                for (int i = 1; i <= cnt; i++)
                    b -= max(0LL, num - a[i]);
                for (int i = cnt + 1; i <= n; i++)
                    b -= max(0LL, num + 1LL - a[i]);
                if (b < 0) continue;
                ans0 = 0;
                for (int i = 1; i <= cnt; i++)
                {
                    ans0 += (long double)36.0 * (long double)(num - a[i]) * ((long double)1.0 / (long double)cnt);
                }
                ans0 -= (long double)(B - b);
                ans = max(ans, ans0);
                //if (ans > 69) cout << num << " " << cnt << endl;
            }
        }
        printf("Case #%d: %lf\n", ++ca, (double)ans);

    }
    return 0;
}
