
#include <iostream>
#include <cstdio>
using namespace std;

int T;
int main(){
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    cin >> T;
    //cout.precision(7);
    for (int test = 1; test<=T; test++){
        double c, f, x;
        cin >> c >> f >> x;
        double cps = 2;
        double time = 0;
        while ((x/cps) > (c/cps + x/(cps+f))){
            time = time + (c/cps);
            cps = cps + f;
            //cout << "Farm purchased, new cps = " << cps << ", time = " << time << endl;
        }
        time = time + x/cps;

        printf("Case #%d: %.7f\n", test, time);
    }
}
