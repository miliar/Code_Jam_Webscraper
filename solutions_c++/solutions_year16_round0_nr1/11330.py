#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("out2.o", "w", stdout);
    map<int, int> mp;
    int n, t, i, j, temp, m, b, a;
    scanf("%d", &t);

    for(i = 1; i <= t; i++)
    {
        scanf("%d", &n);

        if(n == 0)
        {
            cout << "Case #" << i << ": " << "INSOMNIA" << endl;
            continue;
        }

        b = 0;
        for(j = 1; ; j++)
        {
            a = n*j;
            temp = a;
            while(temp > 0)
            {
                m = temp%10;

                if(mp.count(m) == 0)
                {
                    mp[m] = 1;
                    b++;
                }

                temp = temp / 10;
            }

            if(b == 10)
            {
                cout << "Case #" << i << ": " << a << endl;
                break;
            }
        }

        mp.clear();
    }

    return 0;
}
