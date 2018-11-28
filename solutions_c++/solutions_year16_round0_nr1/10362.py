#include <iostream>
#include <cstdio>

#define ll long long

using namespace std;


int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);

    int t, cs = 0;
    ll n;

    cin >> t;

    while(t--)
    {
        cs++;

        cin >> n;

        cout << "Case #" << cs << ": ";

        if(n == 0)
        {
            cout << "INSOMNIA\n";
            continue;
        }

        ll m = 2, a = n;
        int c = 0;
        bool map[10] = {0};

        while(true)
        {
            ll q = a;
            int r;
            while(q)
            {
                r = q%10;
                if(!map[r])
                {
                    c++;
                    map[r] = true;

                    if(c == 10)
                        break;
                }

                q = q/10;
            }
            if(c == 10)
                break;
            a = n*m;
            m++;
        }

        if(c == 10)
            cout << a << "\n";
    }

    return 0;
}
