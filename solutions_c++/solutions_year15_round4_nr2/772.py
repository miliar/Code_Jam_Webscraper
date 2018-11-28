#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <cstdio>
#include <string>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <string.h>
#include "gcj.h"
using namespace std;


const int MAXN = 110;

int sgn(double a)
{
    return a > 1e-8 ? 1 : ( a < -(1e-8) ? -1 : 0);
}

int main(){
    useFile("B");
    int T, N, M, Q, K;
    cin >> T;
    double V0, X0;
    double r[3], c[3];
    for(int ca = 1; ca <= T; ca++){
        cin >> N >> V0 >> X0;
        for(int i=0; i<N; i++)
            cin >> r[i] >> c[i];
        bool can = false;
        double res;
        if(N == 1){
            if( fabs(c[0] - X0) < 1e-8){
                can = true;
                res = V0 / r[0];
            }else{
                can = false;
            }
        }else{
            if(fabs(c[0] - c[1]) < 1e-8){
                if( fabs(c[0] - X0) < 1e-8){
                    can = true;
                    res = V0 / (r[0] + r[1]);
                }
                else can = false;
            }else{
                if( sgn(c[0] - X0) == sgn(c[1] - X0)){
                    can = false;
                }else{
                    can = true;
                    double t1 = (X0 * V0 - c[1]*V0) / r[0] / (c[0] - c[1]);
                    double t2 = (V0 - r[0]*t1) / r[1];
                    res = max(t1, t2);
                }
            }
        }
        cout << "Case #" << ca << ": ";
        if(!can) cout << "IMPOSSIBLE" << endl;
        else {
                //cout << fixed << res << endl;
            printf("%.8f\n", res);
        }
    }
}
