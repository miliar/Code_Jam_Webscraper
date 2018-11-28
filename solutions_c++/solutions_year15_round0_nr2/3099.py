#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

int main(){
    int T;
    cin >> T;
    for(int t = 1; t <= T; t++){
        int n;
        cin >> n;
        vector<int> v(n);
        for(int i = 0; i < n; i++){
            cin >> v[i];
        }
        int ans = *max_element(v.begin(), v.end());
        for(int i = 2; i < ans; i++){
            int cnt = 0;
            for(int j = 0; j < v.size(); j++){
                cnt += (v[j] - 1) / i;
            }
            ans = min(ans, cnt + i);
        }
        cout << "Case #" << t << ": " << ans << endl;
    }
    return 0;
}


