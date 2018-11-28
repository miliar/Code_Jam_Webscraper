#include <iostream>
#include <vector>
#include <cstdio>
using namespace std;

void solve(int t){
    double C, F, X;
    cin >> C >> F >> X;

    double cookies = 2;
    double min_time = 1E100;
    
    double acc_time = 0;
    
    while(true){
        double Xtime = X/cookies;
        double Ctime = C/cookies;

        cookies += F;
        
        double cmin_time = acc_time + Xtime;
        
        if(cmin_time > min_time)
            break;
        min_time = cmin_time; 
        acc_time += Ctime;
    }
    
    printf("Case #%d: %.7f\n",t + 1, min_time);
}

int main(){
    int T;
    cin >> T;
    for(int i = 0; i < T; ++ i)
        solve(i);
    return 0;
}
