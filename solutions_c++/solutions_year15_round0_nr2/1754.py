#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <iostream>
#include <algorithm>

using namespace std;
const int Mn = 1000 + 10;
int f[Mn][Mn];
int a[Mn],n;
inline int calc(int val) {
    int res(0);
    for(int i = n; i >= 1; --i)
        res += f[a[i]][val];
    return res;
}
int main() {
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    for(int i = 1; i <= 1000; ++i) {
        for(int j = 1;j <= 1000; ++j) {
            f[i][j] = (i + j - 1) / j - 1;
            //if(i <= 10 && j <= 10)
                //cout << i << " " << j << " " << f[i][j] << endl;
        }
    } 
    int T;
    cin >> T;
    for(int cas = 1; cas <= T; ++cas) {
        cin >> n;
        int ans(0x7fffffff);
        for(int i = 1; i <= n; ++i) {
            cin >> a[i];
        }
        sort(a + 1, a + n + 1);
        for(int i = a[n]; i >= 1; --i) {
            ans = min(ans,i + calc(i));
        }
        cout << "Case #" <<  cas << ": " << ans << endl;  
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}


