#include<bits/stdc++.h>
using namespace std;
int main()
{
    __int64 t, n;
    __int64 al[10];
    cin >> t;
    for (__int64 j = 1; j <= t; j++)
    {
        cin >> n;
        __int64 print = 1;
        for (__int64 i = 0; i < 10; i++)
            al[i] = 0;
        for (__int64 i = 1; i < 1000000; i++)
        {
            __int64 nn = n*i;
            while(nn)
            {
                al[nn%10]=1;
                nn/=10;
            }
            __int64 kr = 1;
            for (__int64 i = 0; i < 10; i++)
                if(!al[i])
                    kr = 0;
            if(kr)
            {
                print = 0;
                cout << "Case #" << j << ": " << n*i << '\n';
                break;
            }
        }
        if(print)
        {
            cout << "Case #" << j << ": INSOMNIA" << '\n';
        }
    }
}
