#include <fstream>
#include <iostream>
#include <iomanip>
using namespace std;

int t;
double c, f, x, r, sum;

ifstream f1("B-large.in");
ofstream g("output.txt");

int main()
{
    f1 >> t;
    for (int i = 0; i < t; i ++)
    {
        r = 2;
        f1 >> c >> f >> x;
        sum = 0;

        while ((x / r) > (c / r + x / (r + f)))
        {
            sum += c / r;
            r += f;
        }
        sum += x / r;
        g.precision(7);
        g << "Case #" << i + 1 << fixed << ": " << sum;
        g << endl;
    }
    return 0;
}
