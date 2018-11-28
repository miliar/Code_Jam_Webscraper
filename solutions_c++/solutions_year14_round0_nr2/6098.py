#include<iostream>
#include <cstdio>
using namespace std;
double speedUp = 0;
double solve(double speed, double cost, double goal){
    if(goal < cost)
        return goal/speed;
    if(goal/speed > ((cost/speed)+ goal/(speedUp+speed))){
        return cost/speed + solve(speed+speedUp, cost, goal);
    }
    else
        return goal/speed;
}

int main(){
    int T;
    double cost,goal;
    cin >> T;
    for(int ca=1;ca<=T;++ca){
        cin >> cost >> speedUp >> goal;
        printf("Case #%d: %.7f\n",ca,solve(2.0,cost,goal));
    }
}
