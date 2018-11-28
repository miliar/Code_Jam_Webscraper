#include <cstdio>
#include <string>
#include <iostream>
#include <cstdlib>
using namespace std;

int t;

void work()
{
    cin >> t;
    for (int i = 0; i < t; ++i)
    {
        int k, c, s;
        cin >> k >> c >> s;
        cout << "Case #" << i + 1 << ":";
        for (int j = 1; j <= k; ++j) cout << " " << j;
        cout << endl;
    }
}

int main()
{
    freopen("D-small-attempt0.in", "r", stdin);
    freopen("D-small-attempt0.out", "w", stdout);
    work();
    return 0;
}
