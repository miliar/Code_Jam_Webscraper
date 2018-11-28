/// In the name of God

#include <bits/stdc++.h>

#define int long long

using namespace std;
typedef pair<int,int> pii;
typedef long long ll;
typedef long double ld;
typedef vector<int> vi;

#define X first
#define Y second
#define all(o) o.begin(), o.end()
const int maxn = 200 + 10;
ld dp[maxn][maxn], p[maxn];
ld get(vector<ld>v){
    int n = v.size();
    for(int i=0; i<maxn; i++)
        for(int j=0; j<maxn; j++) dp[i][j] = 0.0;
    dp[1][1] = v[0];
    dp[1][0] = 1.0 - v[0];
    for(int i=2; i<=n; i++){
        ld yp = v[i - 1];
        ld np = 1.0 - yp;
        for(int j=0; j<=i; j++){
            if(j == 0) dp[i][j] = dp[i - 1][0] * np;
            else dp[i][j] = dp[i - 1][j - 1] * yp + dp[i - 1][j] * np;
        }
    }
    return dp[n][n/2];
}
ld doo(){
    int n, k;
    cin >> n >> k;
    for(int i=0; i<n; i++)
        cin >> p[i];
    sort(p, p+n);
    vector<ld>v;
    if(k == n){
        for(int i=0; i<n; i++)
            v.push_back(p[i]);
        return get(v);
    }
    int len = n - k;
    ld ans = 0.0;
    for(int i=0; i+len<=n; i++){
        v.clear();
        for(int j=0; j<n; j++){
            if(!(j >= i && j < i + len))
                v.push_back(p[j]);
        }
        ans = max(ans, get(v));
    }
    return ans;
}
main(){
    freopen("BLi.in", "r", stdin);
    freopen("BLo.txt", "w", stdout);
    ios::sync_with_stdio(0);
    cin.tie(0);
    int T;
    cin >> T;
    for(int i=0; i<T; i++){
        cout << "Case #" << i + 1 << ": ";
        cout << setprecision(12) << doo() << endl;
    }

}
