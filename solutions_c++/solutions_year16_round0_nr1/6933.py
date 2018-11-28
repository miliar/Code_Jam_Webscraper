#include<cstdio>
#include<cmath>
#include<iostream>
#include<algorithm>
#include<vector>
#include<stack>
#include<cstring>
#include<queue>
#include<set>
#include<string>
#include<map>
#define inf 9223372036854775807
#define INF 9e7+5
using namespace std;
typedef long long ll;
typedef double db;
const int maxn = 1e5 + 5;
const int mod = 1e9 + 7;

int main()
{
    //cin.sync_with_stdio(false);
    freopen("A-large.in", "r", stdin);
    freopen("out.in", "w", stdout);
    ll t, n, num, cas = 1, vis[15], tmp;

    cin >> t;
    while (t--) {
        cin >> num;
        printf("Case #%d: ", cas++);
        if (!num) {
            cout << "INSOMNIA\n";
            continue;
        }
        memset(vis, 0, sizeof(vis));
        int cut = 0;
        ll temp = num;
       // cout << num << "+++++";
        while (1) {
            tmp = num;
            while (1) {
                int p = tmp%10;
                if (!vis[p]) {
                    cut++;
                    vis[p] = 1;
                }
                tmp /= 10;
                if (tmp <= 0) break;
            }
            //for (int i = 0; i < 10; i++) cout << vis[i] << " ";
            //cout << endl << num << endl;
            if (cut >= 10) break;
            num += temp;
        }
        cout << num << endl;
    }
}
