#include<bits/stdc++.h>
using namespace std;
__int64 s[17], otv[11];
int main()
{
    __int64 jc, n, a[11][17], t;

    for (__int64 i = 2; i < 11; i++)
        for (__int64 j = 0; j < 17; j++)
            if (j)
                a[i][j] = a[i][j-1]*i;
            else
                a[i][j] = 1;

    cin >> t;
    for (__int64 test = 1; test <= t; test++)
    {
        cin >> n >> jc;
         s[0] = 1; s[n-1] = 1;
        cout << "Case #" << test << ":" << '\n';
        for (__int64 i = 0; i < 1<<(n-2) && jc; i++)
        {
            __int64 ii = i;
            for (__int64 j = 0; j < 11; j++)
                otv[j] = 0;
            __int64 kost = 0;
            for (__int64 j = n-3; j >= 0; j--)
            {
                if(i >= a[2][j])
                   {
                       s[j+1] = 1;
                       i -= a[2][j];
                   }
                else
                    s[j+1] = 0;
            }
                i = ii;
                __int64 ans = 0;
            for (__int64 in = 2; in < 11; in++)
            {
                ans = 0; kost = 0;
                for (__int64 j = 0; j < n; j++)
                    ans += a[in][j]*s[j];
                for (__int64 j = 2; j*j <= ans; j++)
                    if(ans%j == 0)
                    {
                        kost = j;
                        break;
                    }
                if (kost)
                    otv[in] = kost;
                else
                    break;

            }
            if (kost)
            {
                for (__int64 j = 0; j < n; j++)
                    cout << s[n-j-1];
                cout << ' ';
                for (__int64 j = 2; j < 11; j++)
                    cout << otv[j] << ' ';
                cout << '\n';
                jc--;
            }
            i = ii;
        }
    }
}
