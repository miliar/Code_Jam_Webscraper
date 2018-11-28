#include <iostream>
#include <fstream>

using namespace std;

typedef long long ll;

ll n, t;

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    cin >> t;
    for (int k = 1; k <= t; ++k)
    {
        ll up;
        char up_c;
        ll add = 0;
        cin >> n;
        cin >> up_c; up = up_c - '0';
        for (ll i = 1; i < n+1; ++i)
        {
            char c;
            cin >> c;
            ll d = c - '0';
            if (up < i && d != 0)
            {
                add += i - up;
                up = i;
            }
            up += d;
        }
        cout << "Case #" << k << ": " << add << endl;
    }

    return 0;
}
