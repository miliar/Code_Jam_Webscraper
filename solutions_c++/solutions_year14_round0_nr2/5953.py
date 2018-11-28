#include <iostream>
#include <iomanip>
#include <algorithm>
using namespace std;

int main(int argc, char** argv) {

    int T;
    cin >> T;
    
    double farmCost, farmRate, goal;
    double farms;
    
    double time;
    double oldTime;
    double farmTime;
    for (int i = 0; i < T; ++i) {
        farms = 1;
        time = 0;
        cin >> farmCost >> farmRate >> goal;
        
        oldTime = goal / 2.0f;
        //cout << oldTime << endl;
        farmTime = 0;
        while(farms) {
            farmTime += farmCost / (2.0f + farmRate * (farms - 1));
            //cout << "Farm time: " << farmTime << endl;
            time = (goal / (farms * farmRate + 2.0f)) + farmTime;
            
            //cout << time << endl;
            if (time > oldTime) {
                break;
            } else {
                oldTime = time;
                farms++;
            }
        }
        cout.setf(ios::fixed);
        cout << "Case #" << i+1 << ": " << setprecision(7) << oldTime << endl;
        //cout << farms << endl;
    }
    
    return 0;
}

