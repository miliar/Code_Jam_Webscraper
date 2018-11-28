#include <iostream>
#include <vector>
#include <set>
#include <algorithm>
#include <iomanip>

using namespace std;

int main() {
    cout << setprecision(15);
    int t;
    cin >> t;
    for(int testcase(0); testcase != t; ++testcase) {
        cout << "Case #" << testcase + 1 << ": ";
        double c, f, x;
        cin >> c >> f >> x;
        double production = 2;
        double time = 0;
        while(true) {
            double time_no_factory =  x / production;
            double time_to_factory = c / production;
            double time_with_factory = time_to_factory + x / (production + f);
            if(time_no_factory <= time_with_factory) {
                time += time_no_factory;
                break;
            }
            time += time_to_factory;
            production += f;
        }
        cout << time << endl;
    }
}
