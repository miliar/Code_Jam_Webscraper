#include <iostream>
#include <string>

using namespace std;
int dp[10];

int main(){
    int T, n, m, tn;
    cin >> T;
    for(int i=0; i<T; i++){
        cin >> n;
        m = n;
        // cout << n << endl;
        if(n==0){
            cout << "Case #" << (i+1) << ": INSOMNIA" << endl;
            continue;
        }
        memset(dp, 0, sizeof(dp));
        int j = 1;
        while(true){
            n = m * j;
            // cout << n << endl;
            j++;
            tn = n;
            while(tn){
                dp[tn % 10]++;
                tn /= 10;
            }
            bool good = true;
            for(int k=0; k<10; k++){
                if(dp[k]==0){
                    good = false;
                    break;
                }
            }
            if(good){
                cout << "Case #" << (i+1) << ": " << n << endl;
                break;
            }
        }
    }
}
