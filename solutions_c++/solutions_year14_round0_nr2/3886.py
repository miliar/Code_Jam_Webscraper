#include<iostream>
#include<vector>
#include<math.h>
using namespace std;

vector<double> timeToBuild;

double timeWithFarms(double c, double f, double x, int n) {
    if (n != 0 && timeToBuild[n] == 0) {
        timeToBuild[n] = timeToBuild[n - 1] + (c / (2.0 + f * (n - 1)));
        //printf("c=%f, f=%f, x=%f, timeToBuild[%d]=%f, timeToBuild[%d]=%f\n", c, f, x, n-1, timeToBuild[n-1], n, timeToBuild[n]);
    }
    //printf("timeTobuild[%d]=%f\t timeToGoal[%d]=%f\n", n, timeToBuild[n], n, timeToBuild[n] + (x / (2.0 + f * n)));
    return timeToBuild[n] + (x / (2.0 + f * n));
}

int main() {
    int cases;
    cin >> cases;
    for (int nc = 1; nc <= cases; nc++) {
        timeToBuild = vector<double>(100000, 0.0);
        
        // c : farm cost, f : rate / farm, x : goal
        double c, f, x;
        cin >> c >> f >> x;
        
        int n = 0;
        double memorizedTime = timeWithFarms(c, f, x, 0);
        double temp = 0;
        while (memorizedTime > (temp = timeWithFarms(c, f, x, n + 1))) {
            memorizedTime = temp;
            n++;
        }
        printf("Case #%d: %.7f\n", nc, memorizedTime);
    }
}
