#include <bits/stdc++.h>

#define pb push_back
#define mp make_pair
#define F first
#define S second

using namespace std;

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    cin >> t;
    for (int h=0; h<t; h++)
    {
        long long n;
        cin >> n;
        if (n == 0)
        {
            cout << "Case #" << h+1 << ": INSOMNIA" << endl;
            continue;
        }
        vector <int> p(10);
        long long d, i = 1;
        while (true)
        {
            bool f = true;
            for (int i=0; i<10; i++)
                if (p[i] == 0)
                    f = false;
            if (f)
                break;
            d = n*i;
            while (d > 0)
            {
                p[d%10] = 1;
                d /= 10;
            }
            i++;
        }
        d = n*(i-1);
        cout << "Case #" << h+1 << ": "  << d << endl;
    }
    return 0;
}
