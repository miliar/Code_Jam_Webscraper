#include <iostream>
#include <cmath>
#include <algorithm>
#include <iomanip>
using namespace std;
int main (){
    int T;
    double C, F, X,ans,now,past;
    cout << setprecision(8);
    cin >> T;
    for(int ca=1;ca<=T;ca++){
        cin >> C >> F >> X;
        now = 2.0;
        ans = X / now;
        past = 0;
        while(1){
            if(past + C / now + X/(F+now) < ans){
                ans = past + C / now + X/(F+now);
                past += C/now;
                now += F;

            }else break;
            //cout << ans << "\n";
        }
        cout << fixed ;
        cout <<"Case #" << ca << ": "<< setprecision(7)<< ans <<"\n";
    }
    return 0;
}
/*
4
30.0 1.0 2.0
30.0 2.0 100.0
30.50000 3.14159 1999.19990
500.0 4.0 2000.0
*/
