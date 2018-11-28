#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

#define rep(i, n)       rep2(i, 0, n)
#define rep2(i, m, n)   for (int i = (int)(m); i < (int)(n); ++i)

int main()
{
    int t;
    cin >> t;
    
    rep(caseno, t) {
        int n, m;
        cin >> n >> m;
        vector<vector<int>> a(n, vector<int>(m)), ok(n, vector<int>(m));
        rep(i, n) rep(j, m) cin >> a[i][j];
        
        rep(i, n) {
            int ma = 1;
            rep(j, m) ma = max(ma, a[i][j]);
            rep(j, m) if (ma == a[i][j]) ok[i][j] = 1;
        }
        rep(i, m) {
            int ma = 1;
            rep(j, n) ma = max(ma, a[j][i]);
            rep(j, n) if (ma == a[j][i]) ok[j][i] = 1;
        }
        
        bool f = true;
        rep(i, n) rep(j, m) if (!ok[i][j]) f = false;
        cout << "Case #" << caseno + 1 << ": ";
        cout << (f ? "YES" : "NO") << endl;
    }
}
