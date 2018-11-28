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
    freopen("B-large.in", "r", stdin);
    freopen("out.in", "w", stdout);
    ll t, cas = 1;
    char str[maxn];

    cin >> t;
    while (t--) {
        cin >> str;
        ll ans = 0;
        char flag = str[0];
        int len = strlen(str);
        for (int i = 1; i < len; i++) {
            if (str[i] != flag) {
                flag = str[i];
                ans++;
            }
        }
        if (flag == '-') ans++;
        printf("Case #%d: ", cas++);
        cout << ans << endl;
    }
}
