#include <iostream>
#include <iomanip> 

using namespace std;

int main(){
    int T;
    double C,F,X;
    
    cin >> T;
    double baseSpeed = 2.0f;
    for (int t1 = 1 ; t1 <= T ; t1++){
        cin >> C >> F >> X;
        
        double totalTime = 0.0f;
        double speed = baseSpeed;

        while ((X  / (speed + F) + C / speed) < X / speed){
            totalTime += C / speed;
            speed += F;
        }
        totalTime += X / speed;
        
        cout << "Case #" << t1 << ": " << fixed << setprecision(7) << totalTime << endl;
    }
    return 0;
}