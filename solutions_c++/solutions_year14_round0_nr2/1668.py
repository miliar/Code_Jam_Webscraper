#include <iostream>
#include <cstring>
#include <stdio.h>
#include <algorithm>
#include <cmath>
#include <vector>
using namespace std;
#define pb push_back
#define mp make_pair

#define ll long long

double c, f, x;

int main(){
    freopen("Bin.txt", "r", stdin );
    freopen("Bout.txt", "w", stdout );
    int tcase;
    int tno= 0;
    cin>>tcase;
    while(tcase--){
        cin>>c>>f>>x;
        double inc =  0;
        double res, pre, curr;
        res = x * 0.5;//max time required
        pre = res;
        for(int k = 1; ; ++k){
            inc += c / ( 2 + (k - 1) * f );
            if( inc > res || fabs( inc - res ) < 1e-6 )
                break;
            curr = inc + x / ( 2 + k * f );
            res = min(res, curr);
            pre = curr;
        }
        printf("Case #%d: %.7f\n", ++tno, res );
    }
    return 0;
}
