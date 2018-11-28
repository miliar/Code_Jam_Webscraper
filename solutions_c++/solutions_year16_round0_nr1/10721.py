#include<cstdio>
#include<algorithm>
#include<iostream>
#include<queue>
#include<cstring>

using namespace std;
typedef long long LL;
const int MAXN = 1000010;

int vis[11];

int cnt = 0;
int old[MAXN];

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    memset(old, -1, sizeof old);
    int T;
    cin >> T;
    int ca = 1;
    while(T--) {
        LL n;
        cin >> n;
        if(n == 0) {
            cout << "Case #" << ca++ << ": INSOMNIA\n";
            continue;
        }
        memset(vis, 0, sizeof vis);
        cnt = 0;
        LL ans;
        if(old[n] != -1) {
            cout << "Case #" << ca++ << ": " << old[n] << endl;
            continue;
        }
        for(int i = 1 ; ; i++) {
            LL tmp = n * i;
            while(tmp) {
                if(!vis[tmp % 10]) {
                    vis[tmp % 10] = true;
                    cnt++;
                }
                tmp /= 10;
            }
            if(cnt >= 10) {
                ans = n * i;
                break;
            }
        }
        old[n] = ans;
        cout << "Case #" << ca++ << ": " << ans << endl;
    }
    return 0;
}
