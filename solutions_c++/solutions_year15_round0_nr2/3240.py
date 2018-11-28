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
        int D; cin >> D;
        vector<int> v(D);
        for(int i=0; i<D; i++)
            cin >> v[i];
        
        int ans = INF;
        for(int i=1; i<=1000; i++){
            int tans = i;
            for(int j=0; j<D; j++){
                tans += (v[j]+i-1)/i-1;
            }
            ans = min(ans, tans);
        }
        cout << ans << endl;
    }
    
    return 0;
}
