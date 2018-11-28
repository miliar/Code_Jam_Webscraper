#include<bits/stdc++.h>
#define all(a) a.begin(), a.end()
#define int long long
int inf = 1e12;
using namespace std;


signed main(int argc, char *argv[])
{
    freopen("B-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    ios::sync_with_stdio(0);
    int T;
    cin >> T;
    for(int q = 1; q <= T; q++){
    int D;
    cin >> D;
    vector<int> a(D);
    for(int i = 0; i < D; i++)
        cin >> a[i];
    sort(all(a));
    reverse(all(a));
    int ans = inf;
    for(int j = 1; j <= a[0] + 1; j++){
        int aans = 0;
        for(int k = 0; k < D; k++)
        if(a[k] > j)
            aans += (a[k] - j) / j + (bool)((a[k] - j)%j) ;
        aans += min(a[0], j);
        ans = min(ans, aans);
    }
    cout << "Case #" << q << ": " << ans << '\n';
    }
    return 0;
}
