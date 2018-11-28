#include <iostream>
#include <fstream>
#include <set>
#include <cstdlib>
#include <array>
#include <iomanip>

using namespace std;

int main()
{
    ifstream cin("input.in");
    ofstream cout("output.txt");
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int q;
    cin >> q;
    for (int num = 1; q; q--, num++)
    {
        cout << "Case #" << num << ": ";
        double c, f, x, now = 2, time = 0;
        cin >> c >> f >> x;
        while (x / now > c / now + x / (now + f))
            {
                time += c / now;
                now += f;
            }
        cout << setprecision(20) << time + x / now << '\n';
    }
    return 0;
}
