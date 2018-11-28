#include <cstdio>
#include <queue>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <vector>
#include <ctime>
#define LL long long
using namespace std;

const int N = 1000100, INF = 0x3f3f3f3f;

//LL res[N];
int d[4200];

char s[N];

int main () {
//    freopen ("A-large.in", "r", stdin);
    freopen ("B-small-attempt1.in", "r", stdin);
    freopen ("out.txt", "w", stdout);
    int T, cas = 1;
    cin >> T;
//    cout << (int)'+' << ' ' << (int)'-' << endl;
    while (T--) {
        scanf ("%s", s);
        int l = strlen (s), st = 0;
        for (int i = 0; i < l; i++) {
            if (s[i] == '-') st |= (1 << i);
        }
        queue <int> q;
//        cout << st << endl;
        q.push (st);
        memset (d, 0x3f, sizeof d);
        d[st] = 0;
        while (!q.empty ()) {
            int u = q.front();
            q.pop();
            int t = u;
            for (int i = 0; i < l; i++) {
                u ^= (1 << i);
                if (d[u] == INF) {
                    d[u] = d[t] + 1;
                    q.push (u);
                }
            }
        }
        printf ("Case #%d: %d\n", cas++, d[0]);
//        int n;
//        cin >> n;
//        scanf ("%s", s);
//        int l = strlen (s), c = 0;
//        for (int i = l - 1; i >= 0; i--) {
////            cout << s[i];
//            if (s[i] == '-') {
//                c++;
//                if (s[0] == '+') c++, s[0] = '+' + '-' - s[0];
//                for (int j = 0, k = i; j < k; j++, k--) swap (s[j], s[k]);
//                for (int j = 0; j <= i; j++) s[j] = '+' + '-' - s[j];
//            }
//        }
//        printf ("Case #%d: %d\n", cas++, c);
//        for (int i = 1; i <= n; i++) {
//            scanf ("%d", &a[i]);
//        }
    }
}
