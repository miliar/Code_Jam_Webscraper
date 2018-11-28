//D.cpp
//Fractiles
//By phoenixinter@gmail.com
//Apr 9, 2016

#include<iostream>
#include<string>
#include<set>
using namespace std;

int main()
{
    int t, kaseno = 0;
    cin >> t;
    while (t--)
    {
        long long k, c, s;
        cin >> k >> c >> s;
        cout << "Case #" << ++kaseno << ": ";
        long long tot = 1;
        for (int i = 0; i < c; i++)
            tot *= k;
        if (c == 1)
        {
            if (s == k)
            {
                for (int i = 1; i <= s; i++)
                    cout << i  << " ";
                cout << endl;
            }
            else
            {
                cout << "IMPOSSIBLE" << endl;
            }
        }
        else  if (k == 1)
        {
            cout << 1 << endl;
        }
        else
        {
            long long minS = (k % 2 == 1 ? k / 2 + 1 : k / 2);
            if (s < minS)
            {
                cout << "IMPOSSIBLE" << endl;
            }
            else
            {
                int gridNum = 0, gridIdx = 1;
                long long base = tot / k;
                while (gridNum < k)
                {
                    long long idx = base * gridNum + gridIdx + 1;
                    cout << idx << " ";
                    gridNum += 2;
                    gridIdx += 2;
                    if (gridIdx == k)
                        gridIdx--;
                }
                cout << endl;
            }
        }
    }
    return 0;
}