#include <iostream>
#include <fstream>
#include <iomanip>
using namespace std;

int main()
{
    ifstream infile("B-large.in");
    ofstream outfile("output");

    int t;
    infile >> t;
    for (int ca = 1; ca <= t; ++ca)
    {
        double c, f, x, ans = 0, s = 2;
        infile >> c >> f >> x;
        while (true)
        {
            double v1 = x / s;
            double v2 = c / s + x / (s + f);
            if (v1 < v2)
            {
                ans += v1;
                break;
            }
            ans += c / s;
            s += f;
        }
        outfile << "Case #" << ca << ": " << setiosflags(ios::fixed)
            << setprecision(7) << ans << endl;
    }
    return 0;
}
