#include <cstdio>
#include <string>
#include <iostream>
#include <cstdlib>
using namespace std;

int t;

bool f[10];

void work()
{
    cin >> t;
    for (int i = 0; i < t; ++i)
    {
        int n;
        cin >> n;
        cout << "Case #" << i + 1 << ": ";
        for (int j = 0; j < 10; ++j) f[j] = false;
        int tot = 10;
        for (int k = 1; k <= 10000000; ++k)
        {
                long long d = (long long)n * (long long)k;
                long long od = d;
                while (d != 0)
                {
                                int x = d % 10;
                                //cout << x << endl;
                                if (!f[x]) {f[x] = true; tot --;}
                                d /= 10;
                                if (tot == 0) break;
                }
                if (tot == 0) {cout << od << endl; break;}
        }
        if (tot != 0) cout << "INSOMNIA" << endl;
    }
}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    work();
    return 0;
}
