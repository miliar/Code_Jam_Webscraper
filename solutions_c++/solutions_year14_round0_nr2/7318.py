#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <iomanip>

using namespace std;

int numTest, testCase;
double F, C, X;

bool needMoreFarm(double cost, double increase, double target, double numFarm){
    if ( (target - cost) / (2 + numFarm * increase) > target / (2 + (numFarm + 1) * increase) )
        return true;
    return false;
}

int main(){
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);

    double time;
    int numFarm;
    testCase = 0;

    cin >> numTest;
    while(testCase < numTest){
        testCase++;
        cin >> C >> F >> X;
        time = 0;
        numFarm = 0;
        while (needMoreFarm(C, F, X, numFarm)){
            time += C / (2.0 + (F * numFarm));
            numFarm++;
        }
        time += X / (2.0 + (F * numFarm));
        printf("Case #%d: %.7lf\n", testCase, time);
    }
    return 0;
}
