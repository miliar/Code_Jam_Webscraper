#include <iostream>
using namespace std;

int main() {
    int T,idx;
    double C,F,X,sum_C,time_X,rate,sum_curr,sum_prev,answer;
    
    cin >> T;
    for (idx=1; idx<= T; idx++) {
        cin >> C >> F >> X;
        rate = 2;
        time_X = X/rate;
        sum_C = 0;
        sum_curr = time_X;
        sum_prev = 9999999;
        
        while (sum_prev > sum_curr) {
            sum_prev = sum_curr;
            sum_C += C/rate;
            rate += F;

            time_X = X/rate;
            sum_curr = sum_C + time_X;
        }
        answer = sum_prev;
        
        //cout << "Case #" << idx << ": " << answer << endl << endl;
        printf("Case #%d: %.7f\n",idx,answer);
    }
}
