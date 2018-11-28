#include <iostream>
#include <fstream>
#include <set>

using namespace std;

bool f(int x, int r, int c)
{
    if (r > c)
        swap(c, r);
    if (x == 4)
    {
        if (r == 4 && c == 4 || r == 3 && c == 4) return 0;
        return 1;
    }
    if (x == 3)
    {
        if (r == 1 && c == 3) return 1;
        if (r * c % 3 == 0) return 0;
        return 1;
    }
    if (x == 2)
    {
        if (r * c % 2 == 0) return 0;
        return 1;
    }
    return 0;
}

int main()
{
    freopen("D-small-attempt1.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t;
    cin >> t;
    //cerr << " t = " << t << endl;
    for (int j = 0; j < t; ++j)
    {
        int x, r, c;
        cin >> x >> r >> c;
        if (f(x, r, c))
            cout << "Case #" << j + 1 << ": RICHARD" << endl;
        else
            cout << "Case #" << j + 1 << ": GABRIEL" << endl;
    }
    return 0;
}
