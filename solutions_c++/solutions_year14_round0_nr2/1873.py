#include <iostream>
#include <stdio.h>
#include <iomanip>
using namespace std;

int main(){
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);

    int t,tt=1;
    cin >> t;

    double c,f,x;
    double rate;
    double seconds;

    while( tt <= t ){
        cin >> c >> f >> x;
        rate = 2;
        seconds = 0;

        if ( x <= c )
            seconds = x/rate;
        else{
            seconds += c/rate;

            while ( true ){
                if ( (x-c)/rate < x/(rate+f) ) {// no buy farm
                    seconds += (x-c)/rate;
                    break;
                }else{
                    rate += f;
                    seconds += c/rate;
                }
            }
        }
        printf("Case #%d: %.7f\n",tt,seconds);
        //cout << "Case #" << tt << ": " << setprecision(7) << seconds << endl;
        tt++;
    }
}
