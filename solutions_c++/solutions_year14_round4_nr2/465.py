#include <cstdio>
#include <iostream>
#include <algorithm>
#include <queue>
#include <cmath>
#include <vector>
#include <cstring>
using namespace std;
const int INF = 1000000000+10;
const int N = 1000+10;
int a[N];
vector<int> g;
int b[N], p[N], q[N];
int n;
int work(int v, int &l, int &r) {
    int pos = q[v];
    int ret = 0;
    if (pos <= l) {
        for (int i = pos; i < l; i++) {
            swap(b[i], b[i+1]);
            q[b[i]] = i;
            ret++;
        }
        q[b[l]] = l;
        l--;
        if (v == n-1) r++;
    }else {
        for (int i = pos; i > r; i--) {
            swap(b[i], b[i-1]);
            q[b[i]] = i;
            ret++;
        }
        q[b[r]] = r;
        r++;
        if (v == n-1) l--;
    }

        if (r >= n) r = n-1;

        if (l < 0) l = 0;
   // for (int i = 0; i < n; i++) {
    //    q[b[i]] = i;
    //}
    return ret;

}
void solve() {
    int mi = INF;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            b[j] = a[j]; q[b[j]] = j;
        }
        int l = i, r = i;
        int ans = work(n-1, l, r);

        cout << ans << " *** " << l << " " << r << endl;
        for (int j = n-2; j >= 0; j--) {
            ans += work(j, l, r);
           cout << ans << " *** " << l << " " << r << endl;
        }
      //  cout << ans << endl;
        if (ans < mi) mi = ans;

    }
    printf("%d\n",mi);
}
int main() {

    //freopen("B-small-attempt2.in","r",stdin);
   // freopen("out.txt","w",stdout);
    int T,cas = 0; scanf("%d",&T);
    while (T--) {
        scanf("%d",&n);
        g.clear();
        for (int i = 0; i < n; i++) {
            scanf("%d",a+i);
            g.push_back(a[i]);
        }
        sort(g.begin(), g.end());
        memset(p, 0 ,sizeof(p));
        for (int i = 0; i < n; i++) {
            a[i] = lower_bound(g.begin(), g.end(), a[i]) - g.begin();
            p[a[i]] = i;
       //    cout << a[i] << " " << i << endl;

        }
      //  for (int i = 0; i < n; i++) {
        //    cout << p[i] << " ";
       // }cout << endl;
        printf("Case #%d: ",++cas);
        solve();

    }
    return 0;
}
