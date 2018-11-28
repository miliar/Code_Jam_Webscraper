#include <iostream>
#include <fstream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <set>

#define f first
#define s second

using namespace std;




int main()
{
    freopen("b.txt", "r", stdin);
    freopen("bout.txt", "w", stdout);
    int T;
    cin >> T;
    for (int i = 0; i < T; ++i)
    {
        long double c, f, x;
        cin >> c >> f >> x;
        long double Ans = 100000;
        long double time = 0;
        long double sp = 2;
        for (int k = 0; k <= x; ++k)
        {
            long double now = time + x / sp;
            Ans = min(now, Ans);
            time += c / sp;
            sp += f;
        }
        cout.precision(400);
        cout << "Case #" << i + 1 <<": " << Ans << endl;
    }
    return 0;
}
