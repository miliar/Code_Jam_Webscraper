#include<iostream>
#include <cstdio>

using namespace std;
int main()
{
    int T;
    double C, F, X, rate, x_time, farm_time, time, new_x_time;
    cin >> T;
    for(int turn=1; turn<=T; turn++){
        cin >> C >> F >> X;
        rate = 2.0;
        time = 0.0;
        do{
            x_time = X / rate;
            farm_time = C / rate ;
            time = time + farm_time;
            rate += F ;
            new_x_time = farm_time + ( X / rate );
        }while( new_x_time < x_time );
        time = time - farm_time + x_time;
        printf( "Case #%d: %0.7lf\n", turn , time ) ;
    }
}
