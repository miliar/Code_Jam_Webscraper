#include<iostream>
#include<stdio.h>
#include<math.h>
#include<vector>
#include<algorithm>
#include<set>

using namespace std;

int main(){
    freopen("B-large.in", "r", stdin);
    freopen("B.out", "w", stdout);
    int T;
    double C, F, X;
    double MIN;

    double time;

    double rate;
    cin>>T;
    for(int i=1; i<=T; i++){
        cin>>C>>F>>X;
        MIN=10000000000.0;
        time=0.0;
        rate=2.0;
        while(time+X/rate<MIN){
            MIN=time+X/rate;
            time+=C/rate;
            rate+=F;
        }
        printf("Case #%d: %.8f\n", i, MIN);


    }
}
