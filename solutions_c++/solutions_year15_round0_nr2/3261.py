#include <iostream>
using namespace std;
int main(int argc, const char * argv[]) {
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    cin >> t;
    for (int tt = 1; tt <= t; tt++){
        int d, sum = 0,maxNumber = 0, ans = 1000000;
        int p[1001] = {0};
        cin >> d;
        for(int i = 1; i <= d; i++){
            cin >> p[i];
            if(p[i] > maxNumber) maxNumber = p[i];
        }
        for(int i = 1; i <= maxNumber; i++){
            sum = 0;
            for(int j = 1; j <= d; j++){
                if(p[j] > i){
                    sum += p[j] / i;
                    if(p[j] % i == 0) sum--;
                }
            }
            if(ans > sum + i){
                ans = sum + i;
            }
        }
        cout << "Case #" << tt << ": " << ans <<endl;
    }
    return 0;
}
