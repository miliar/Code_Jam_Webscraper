#include <iostream>
#include <cstdio>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>
#include <functional>
#include <climits>
#include <cmath>
#include <string>
#include <cstring>
using namespace std;

#define rep(i, n) for (int i = 0; i < n; i ++)
#define mem(s, v) memset(s, v, sizeof(s))
#define sz(v) (int)v.size()
#define pb push_back
#define mp make_pair

int main() {
    freopen("/Users/youhangtian/Downloads/D-large.in", "r", stdin);
    freopen("/Users/youhangtian/Downloads/output.txt", "w", stdout);
    
    int T;
    cin >> T;
    
    for (int ca = 1; ca <= T; ca ++) {
        int n;
        cin >> n;
        
        vector<double> vn, vk;
        rep(i, n) {
            double d;
            cin >> d;
            vn.pb(d);
        }
        rep(i, n) {
            double d;
            cin >> d;
            vk.pb(d);
        }
        sort(vn.begin(), vn.end());
        sort(vk.begin(), vk.end());
        
        int res1 = 0, res2 = 0;
        int pn = 0;
        rep(ik, n) {
            while (pn < n && vn[pn] < vk[ik]) pn ++;
            
            if (pn < n) pn ++;
            else {
                res1 = n - ik;
                break;
            }
        }
        int pk = 0;
        rep(in, n) {
            while(pk < n && vk[pk] < vn[in]) pk ++;
            
            if (pk < n) pk ++;
            else {
                res2 = n - in;
                break;
            }
        }
        
        cout << "Case #" << ca << ": " << n - res1 << " " << res2 << endl;
    }
    
    return 0;
}