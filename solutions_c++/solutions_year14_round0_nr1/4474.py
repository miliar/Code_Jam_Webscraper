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
    freopen("/Users/youhangtian/Downloads/A-small-attempt0.in", "r", stdin);
    freopen("/Users/youhangtian/Downloads/output.txt", "w", stdout);
    
    int T;
    cin >> T;
    
    for (int ca = 1; ca <= T; ca ++) {
        int a1, a2;
        
        int arr1[4][4], arr2[4][4];
        
        cin >> a1;
        a1 --;
        rep(i, 4) rep(j, 4) cin >> arr1[i][j];
        cin >> a2;
        a2 --;
        rep(i, 4) rep(j, 4) cin >> arr2[i][j];
        
        bool b[17];
        mem(b, false);
        rep(i, 4) b[arr1[a1][i]] = true;
        
        vector<int> v;
        rep(i, 4) {
            int n = arr2[a2][i];
            
            if (b[n]) v.pb(n);
        }
        
        cout << "Case #" << ca << ": ";
        if (sz(v) == 0) cout << "Volunteer cheated!" << endl;
        else if (sz(v) == 1) cout << v[0] << endl;
        else cout << "Bad magician!" << endl;
    }
    
    return 0;
}