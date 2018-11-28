#include <string> 
#include <algorithm> 
#include <cfloat> 
#include <climits> 
#include <cmath> 
#include <complex> 
#include <cstdio> 
#include <cstdlib> 
#include <cstring> 
#include <functional> 
#include <iostream> 
#include <map> 
#include <memory> 
#include <queue> 
#include <set> 
#include <sstream> 
#include <stack> 
#include <utility> 
#include <vector> 

#define EACH(i,c) for(__typeof((c).begin()) i=(c).begin(); i!=(c).end(); ++i)
#define ALL(x) (x).begin(),(x).end() 
using namespace std;
const double eps = 1e-10;

//input data
double C, F, X;

void solve(int caseNum){
    //solve problem here
    double cps = 2.0;
    double time = 0.0;
    for(;;){
        double dt = C / cps;
        double dt2 = X / cps;
        double dt3 = X / (cps + F);
        if(dt2 < dt + dt3 || dt3 < 0){
            time += dt2;
            break;
        }
        else{
            cps += F;
            time += dt;
        }
    }
    cout << "Case #" << caseNum << ": ";
    printf("%.10lf\n", time);
}

int main(){
    int T;
    cin >> T;

    for(int t=1; t<=T; ++t){
        //input test case here
        cin >> C >> F >> X;

        solve(t);
    }
    return 0;
}
