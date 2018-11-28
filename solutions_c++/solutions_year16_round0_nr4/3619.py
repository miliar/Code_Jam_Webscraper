#include <iostream>
#include <cmath>
#include <vector>
#include <fstream>

using namespace std;

int main ()
{
    freopen ("outputDsmall.txt", "w", stdout);
    freopen ("D-small-attempt0.in", "r", stdin);
    int t;
    cin >> t;
    for (int i = 1; i <= t; ++i)
    {
        int k, c, s;
        cin >> k >> c >> s;
        cout << "Case #" << i << ": ";
        for (int j = 1; j <= k; ++j)
            cout << j << " "; //it works only if k == s
        cout << endl;
    }
}

