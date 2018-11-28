#include <iostream>
#include <cstdio>
#include <string>
#include <assert.h>
#include <vector>

using namespace std;

int T;
double C, F, X;

int main(){

    freopen("fis.in", "r", stdin);
    freopen("fis.out", "w", stdout);

    cin >> T;


    cout.precision(7);
    cout.setf( ios::fixed, ios::floatfield);

    for(int t = 1; t <= T; ++t){

        cin >> C >> F >> X;

        double cookies = 0;
        double rate = 2;
        double sol = 0;

  
        // We buy farm if it is better
        double noBuyTime = (X - C) / rate;
        double buyTime   = X / (rate + F);

        while(buyTime < noBuyTime){
            sol += C / rate;
            rate += F;

            noBuyTime = (X - C) / rate;
            buyTime   = X / (rate + F);
        }

        sol += X / rate;

        cout << "Case #" << t << ": " << sol;
        cout << '\n';
    }
    return 0;
}