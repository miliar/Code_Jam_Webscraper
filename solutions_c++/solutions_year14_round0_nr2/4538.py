#include <iostream>
#include <cmath>
#include <iomanip>
#include <fstream>
using namespace std;

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int t;
    cin >> t;
    for (int s=1; s<=t; ++s) {
        double c = 0, f = 0, x = 0, time = 0;
        cin >> c >> f >> x;
        int m = ceil(x/c-2/f-1);
        if (m<0) m = 0;
        for (int i=0; i<m; ++i) {
            time += c/(2+i*f);
        }
        time += x/(2+m*f);
        cout << setprecision(7) << std::fixed << "Case #" << s << ": " << time << endl;
    }
    return 0;
}

