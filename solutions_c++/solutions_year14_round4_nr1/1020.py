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
 freopen("/Users/youhangtian/Downloads/A-large.in", "r", stdin);
 freopen("/Users/youhangtian/Downloads/output.txt", "w", stdout);
 
 int T;
 cin >> T;
 
 for (int ca = 1; ca <= T; ca ++) {
     int n, x;
     cin >> n >> x;
     
     int s[n];
     rep(i, n) cin >> s[i];
     
     bool b[n];
     mem(b, false);
     
     sort(s, s + n, greater<int>());
     
     int res = 0;
     rep(i, n) if (!b[i]) {
         res ++;
         b[i] = true;
         
         for (int j = i + 1; j < n; j ++) if (!b[j] && s[i] + s[j] <= x) {
             b[j] = true;
             break;
         }
     }
     
     cout << "Case #" << ca << ": " << res << endl;
 }
 
 return 0;
 }