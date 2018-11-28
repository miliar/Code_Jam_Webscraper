#include <iostream>
// #include <deque>
#include <vector>
#include <algorithm>
#include <string>
#define pb push_back
using namespace std;
int main() {
    int t;
    cin >> t;
    for(int tt=1;tt<=t;tt++) {
        string s;
        cin >> s;
        int vis[1001];
        memset(vis, 0, sizeof vis);
        int n = s.size();
        vector<char> res;
        vector<pair<char, int>> max1;
        int ind = n;
        while(1) {
            char c = s[0];
            int tind = 0;
            max1.push_back(make_pair(c, 0));
            for(int i=1;i<ind;i++) {
                if(s[i] > c)max1.clear(), c = s[i], tind = i, max1.pb(make_pair(c, i));
                else if(s[i] == c)max1.pb(make_pair(c, i));
            }
            ind = tind;
            for(int i=0;i<(int)max1.size();i++)
                res.pb(max1[i].first), vis[max1[i].second] = 1;
            if((int)max1.size() == 0 or ind == 0)break;
            max1.clear();
        }
        
        for(int i=0;i<n;i++)
            if(!vis[i])res.pb(s[i]);
        
        cout << "Case #" << tt << ": ";
        for(int i=0;i<n;i++)
            cout << res[i];
        cout << "\n";
    }
    return 0;
}