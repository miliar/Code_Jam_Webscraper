
#include <iostream>
#include <vector>
#include <cstdio>
using namespace std;
double f(double c,double f, double x) {
    double timeNow = 0.0;
    double speedNow = 2.0;
    while (true) {
        double dt1 = x/speedNow; //finish time
        double timenxtFarm = c/speedNow;
        double dt2 = timenxtFarm+x/(speedNow+f);
        if (dt1<dt2 +1e-7) return timeNow+dt1;
        timeNow += timenxtFarm;
        speedNow+=f;
    }
}
int main() {
    int t;
    cin >> t;
    for (int c = 1; c<= t; c++)  {
        cout << "Case #" << c <<": ";
        double x,y,z;
        cin >> x >> y >> z;
        printf("%.8lf\n",f(x,y,z));

    }

}
