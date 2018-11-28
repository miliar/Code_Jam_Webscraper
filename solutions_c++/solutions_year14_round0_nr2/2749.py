#include <iostream>
#include <iomanip>
#include <string>
#include <map>
#include <vector>
#include <queue>
#include <stack>
#include <algorithm>

using namespace std;
typedef long long ll;



int main(){
    int T;
    cin >> T;
    cout << setprecision(10);
    for(int t=1;t<=T;t++){
        double C, F, X;
        cin >> C >> F >> X;
        
        double R = 2.0;
        double curT = 0;
        double minT = curT + X/R;
        
        while(curT < minT){
            curT+=C/R;
            R+=F;
            minT = min(minT, curT + X/R);
        }
        
        cout << "Case #" << t << ": " << minT << endl;
        
        
    }

    return 0;
}