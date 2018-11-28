#include <iostream>
#include <cmath>
#include <cstring>
 
using namespace std;

#define printVar(a) cout<<#a<<" = "<<a<<"\n"

int t, n;
int Ps[1000];
int opCount, minSteps;

int main(){
    cin >> t;
    for(int ti = 1; ti <= t; ti++){
        cin >> n;
        int maxPs = 0;
        for(int ni = 0; ni < n; ni++){
            cin >> Ps[ni];
            maxPs = max(maxPs, Ps[ni]);
        }
        minSteps = maxPs;
        for(int maxPi = 1; maxPi < maxPs; maxPi++){
           // printVar(maxPi);
            opCount = 0;
            for(int ni = 0; ni < n; ni++){
                if(Ps[ni] > maxPi){
             //       cout << "|>|\n";
                    opCount += (Ps[ni]+maxPi-1)/maxPi - 1;
                }
               // printVar(opCount); 
            }
            minSteps = min(minSteps, maxPi+opCount);
        }
        cout << "Case #" << ti << ": " << minSteps << "\n";
    }
    return 0;
}

