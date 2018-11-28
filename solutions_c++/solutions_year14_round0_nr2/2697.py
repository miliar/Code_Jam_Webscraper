#include <vector>
#include <algorithm>
#include <iterator>
#include <iomanip>
#include <fstream>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    
    ifstream in("D:\\input.txt");
    ofstream out("D:\\output.txt");

    int t;
    in >> t;

    out << fixed << setprecision(7);

    for(int q = 1; q <= t; ++q) {
        double C, F, X;
        in >> C >> F >> X;

        int k = max(0.0, ceil(X / C - 2 / F - 1.0));

        double ans = X / (2 + k*F);
        for(int i = 0; i < k; ++i) {
            ans += C / (2 + i*F);
        }

        out << "Case #" << q << ": " << ans << endl;
    }

    system("pause");

    return 0;
} 