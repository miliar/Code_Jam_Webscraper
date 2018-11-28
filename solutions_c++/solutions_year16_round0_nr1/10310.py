/***** PES College of Engineering, mandya ****/
#include <bits/stdc++.h>
#define ll long long
using namespace std;

int main()
{
    int t, c, i, r;
    ll n, a;
    cin >> t;
    ll x =1;
    while(t--)
    {
        int f[10] = {0};
        c = 0;
        cin >> n;
        for(i=1 ; i<=100 ; i++)
        {
            a = n;
            a *= i;
            while(a>0)
            {
                r = a%10;
                //cout << r << endl;
                if(f[r] == 0)
                {
                    f[r] = 1;
                    c++;
                }
                a /= 10;
            }
            if(c == 10)
            {
                cout << "Case #" << x << ": " << n*i << endl;
                x++;
                break;
            }
        }
        if(c != 10)
        {
            cout << "Case #" << x << ": INSOMNIA" << endl;
            x++;
        }
    }
    return 0;
}
