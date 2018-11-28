#include <iostream>
#include <cmath>
#include <iomanip>

using namespace std;

double recurse(double c,double f, double x, double rate) {
    // Base condition.
    double withoutBuying = x/rate;
    double withBuying = (c/rate) + (x/(rate + f));
 //   cout << "base: " << withBuying << " " << withoutBuying << endl;
    if (withoutBuying <= withBuying) {
 //       cout << "Nuff with buying farms " << rate << endl;
        return withoutBuying;
    }
    double furtherTime = recurse(c, f, x, rate + f);

    return (c/rate) + furtherTime;


}
int main () {
    int numOfCases;
    cin >> numOfCases;
    int caseNum = 0;
    double c, f, x, rate;
    while(numOfCases--) {
        caseNum++;
        cin >> c >> f >> x;
        rate = 2;
        cout << "Case #" << caseNum << ": ";
        cout << std::fixed << setprecision(7) << recurse(c, f, x, rate);
        cout << endl;
    }
}
                                                                                                         
