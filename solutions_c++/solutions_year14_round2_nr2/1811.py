#include <iostream>

using namespace std;

int main()
{
    int t, a, b, k, ok;
    cin >> t;
    for (int i = 0; i < t; ++i)
    {
        cin >> a >> b >> k;
        ok = 0;
        for (int ai = 0; ai < a; ++ai)
        {
            for (int bi = 0; bi < b; ++bi)
            {
                if ((ai&bi) < k) ++ok;
            }
        }
        cout << "Case #" << (i+1) << ": " << ok << endl;
    }
}