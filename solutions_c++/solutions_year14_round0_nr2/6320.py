#include <iostream>
#include <cstring>
#include <string>
#include <cmath>
#include <iomanip>

using namespace std;

int main(){
    int t;
    double C, F, X;
    cin >> t;
    for(int test = 1; test <= t; test++){
        cin >> C >> F >> X;
        double totime = X / 2.0, temp, farm = 0, now = 2.0;
        while(1){
            farm += C / now;
            now += F;
            temp = X / now;
            if((temp + farm) > totime) break;
            totime = temp + farm;
            //cout << totime << endl;
        }
        cout << "Case #" << test << ": ";
        cout << fixed << setprecision(7) << totime << endl;
    }
    return 0;
}
