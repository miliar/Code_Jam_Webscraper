#include <iostream>
#include <string>

using namespace std;

int main(){
    int i, j;
    int t, smax, res, sum, d;
    string s;
    
    cin >> t;
    for (i = 0; i < t; i++){
        cin >> smax >> s;
        res = 0;
        sum = 0;
        
        for (j = 0; j < s.size(); j++){
            d = s[j] - '0';
            if (sum < j){
                res += j - sum;
                sum = j;
            }
            sum += d;
        }
        
        cout << "Case #" << i+1 << ": " << res;
        if (i+1 < t) cout << endl;
    }
    
    return 0;
}
