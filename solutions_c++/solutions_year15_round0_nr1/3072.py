#include <iostream>
#include <cmath>
#include <string>

using namespace std;

int t, smax;
string str;

int main(){
    cin >> t;
    for(int ti = 1; ti <= t; ti++){
        cin >> smax;
        cin >> str;
        int curSum = 0, extra = 0;
        for(int si = 0; si <= smax; si++){
            int curCount = (int)(str[si]-'0'); 
            if(curSum < si){
               extra += si-curSum;
               curSum += si-curSum;
            }
            curSum += curCount;
        }
        cout << "Case #" << ti << ": " << extra << "\n";
    }
    return 0;
}


