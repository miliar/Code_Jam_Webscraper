#include <iostream>
#include <vector>
#include <string>
using namespace std;

typedef vector<int> Row;
typedef vector<Row> Matrix;

int main()
{
    cout.precision(7);
    cout.setf(ios::fixed);
    int T;
    cin >> T;
    for (int xx = 1;xx <= T; ++xx) {
        double ttime = 0;
        double c,f,x;
        double cps = 2;
        bool finish = false;
        cin >> c >> f >> x;
        while (not finish) {
            if (x/cps < (x/(cps+f)+(c/cps))) {
                finish = true;
                ttime += x/cps;
            }
            else {
                ttime += c/cps;
                cps += f;
            }
        }
        cout << "Case #" << xx << ": " << ttime << endl;
    }
}
