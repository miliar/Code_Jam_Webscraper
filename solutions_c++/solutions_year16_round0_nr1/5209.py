#include <iostream>
#include <vector>
#include <fstream>

using namespace std;

int main ()
{
    freopen ("output.txt", "w", stdout);
    freopen ("A-large.in", "r", stdin);
    int t;
    cin >> t;
    for (int i = 1; i <= t; ++i)
    {
        int n, x = 0;
        cin >> n;
        if (n != 0)
        {
            vector <int> a(10);
            for (int j = 0; j < 10; ++j)
                a[j] = j;
            while (a[0] != -1 || a[1] != -1 || a[2] != -1 || a[3] != -1 || a[4] != -1 || a[5] != -1 || a[6] != -1 || a[7] != -1 || a[8] != -1 || a[9] != -1)
            {
                ++x;
                int k = n * x;
                while (k != 0)
                {
                    a[k % 10] = -1;
                    k = k / 10;
                }
            }
            cout << "Case #" << i << ": " << n * x << endl;
        }
        else
            cout << "Case #" << i << ": INSOMNIA" << endl;
    }
}
