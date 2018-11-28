#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <queue>
#include <stack>
#include <vector>
#include <set>
#include <map>
#include <string>
using namespace std;

#define in

typedef long long LL;

#define For(i,b) for(i=0;i<b;i++)
#define Foru(i,a,b) for(i=a;i<=b;i++)
#define Ford(i,a,b) for(i=a;i>=b;i--)
#define mod 1000000007

int a[5][5], b[5][5];
set <int> s;
void solve(){
    int t, ai, bi, ans;
    int i, j, cnt=0;
    cin >> t;
    while(t--){
        ans = 0;
        int res = 0;
        s.clear();
        cin >> ai;
        For(i,4) For(j,4) cin >> a[i][j];
        cin >> bi;
        For(i,4) For(j,4) cin >> b[i][j];
        For(i,4) s.insert(a[ai-1][i]);
        For(i,4) if(s.find(b[bi-1][i]) != s.end()) ans ++, res = b[bi-1][i];
        cout << "Case #" << ++cnt << ": ";
        if(ans == 1) cout << res << endl;
        else if(ans >1) cout << "Bad magician!" << endl;
        else cout << "Volunteer cheated!" << endl;
    }
}
int main(){
    #ifdef in
        freopen("in","r",stdin);
        freopen("out","w",stdout);
    #endif
    solve();
    return 0;
}
