#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <vector>
#include <queue>
#include <numeric>
#include <string>
#include <string.h>
#include <map>
#include <set>
#include <functional>
#include <complex>

using namespace std;

const int INF = (1<<30) - 1;


int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    
    int T; cin >> T;
    for(int t=1; t<=T; t++){
        cout << "Case #" << t << ": ";
        int S; cin >> S;
        string Ss; cin >> Ss;
        int ans = 0;
        int sum = 0;
        for(int i=0; i<=S; i++){
            int x = (Ss[i]-'0');
            if(sum < i){
                ans += (i-sum);
                sum = i;
            }
            sum += x;
        }
        cout << ans << endl;
    }
    
    return 0;
}
