//#include <iostream>
#include <iomanip>
#include <fstream>
#include <algorithm>
using namespace std;

ifstream cin("B-large.in");
ofstream cout("B.txt");

int main(){
    int T;
    cin >> T;
    for(int t = 1; t <= T; t++){
        double C, F, X;
        cin >> C >> F >> X;
        double minTime = 3*X;

        double production = 2.0, farmTime = 0;
        while(farmTime < (2*X + 1)){
            double cookieTime = farmTime + (X / production);
            minTime = min(minTime, cookieTime);
            if(cookieTime > minTime) break;
            farmTime += C / production;
            production += F;
        }

        cout << fixed << setprecision(7) << "Case #" << t << ": " << minTime << endl;
    }
}