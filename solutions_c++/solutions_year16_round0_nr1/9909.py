#include <iostream>
#include <cstdio>

#include <cstring>

using namespace std;

bool vis[10];

int main() {
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int cases;
    scanf("%d", &cases);
    for (int cas = 1; cas <= cases; cas ++) {
        int n;
        cin >> n;
        printf ("Case #%d: ", cas);
        if (!n) {
            puts("INSOMNIA");
            continue;
        }
        memset(vis, 0, sizeof(vis));
        bool flag = 0;
        int pre = 0;
        while (!flag) {
            pre += n;
            int cur = pre;
            while(cur) {
                vis[cur%10] = 1;
                cur /= 10;
            }
            flag = 1;
            for (int i = 0; i < 10; i++) {
                if (!vis[i]) flag = 0;
            }
        }
        cout << pre << endl;

    }



    return 0;
}
