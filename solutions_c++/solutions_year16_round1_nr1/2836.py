#include "iostream"
#include "cstdio"
#include "string.h"
#include "cstring"
#include "algorithm"
#include "vector"
#include "unordered_set"
#include "unordered_map"

using namespace std;

int main() {
    int n, c, p;
    int num;
    unordered_map<int, int> um;
    vector<int> ans;
    cin>>n;
    for(int cases = 1; cases <= n; cases ++ ) {
        cin>>c>>p;
        um.clear();
        ans.clear();
        for(int i = 0; i < p; i ++ ) {
            cin>>num;
            auto pos = um.find(c - num);
            if(pos != um.end()) {
                ans.push_back(pos);
                ans.push_back(i + 1);
            }

            um[num] = i + 1;
        }

        cout<<"Case #" << cases << ": " << ans[0]<<" "<<ans[1]<<'\n';
    }
    return 0;
}
