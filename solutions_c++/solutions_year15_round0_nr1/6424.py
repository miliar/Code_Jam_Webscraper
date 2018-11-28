#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(int argc, char** argv) {

    int T;
    cin >> T;
    for (int cases = 1; cases <= T; ++cases) {
    int shy;
    cin >> shy;
    
    string rank;
    cin >> rank;
    
    vector<int> v;    
    for (int i = 0; i <= shy; ++i) {
        for (int j = 0; j < rank[i] - '0'; ++j)
            v.push_back(i);
    }
    
    int cur = 0;
    int ans = 0;
    for (int i = 0; i < v.size(); ++i) {
        if (v[i] > ans) {
            ans += v[i]-cur;
            cur = v[i]+1;
        }
        else {
            cur++;
        }
    }
    cout << "Case #" << cases << ": " << ans << endl;
    }
    return 0;
}

