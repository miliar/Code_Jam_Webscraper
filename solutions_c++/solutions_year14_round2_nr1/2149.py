#include <iostream>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>
#include <string>
#include <set>
#include <map>
#include <list>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <cstdio>
#include <cmath>
typedef long long ll;
#define FOR(i, b, e) for(int i = b; i < e; i++)
using namespace std;




int main()
{
    int T, n;
    int cnt[110];
    int t[110][110];
    char ch[110][110];
    string str[110];
    int l[110];
    scanf("%d", &T);
    for (int tt = 1; tt <= T; tt++) {
        int ans = 0;
        memset(t, 0, sizeof(t));
        memset(cnt, 0, sizeof(cnt));
        int mini[110], maxi[110];

        cin >> n;
        for (int i = 0; i < n; i++) cin >> str[i];
        

        for (int i = 0; i < n; i++) {
            int p = 0;
            t[i][0] = 1;
            ch[i][0] = str[i][0];
            for (int j = 1; j < str[i].length(); j++) {
                if (str[i][j] == str[i][j-1]) {
                    t[i][p]++;
                }
                else {
                    p++;
                    t[i][p] = 1;
                    ch[i][p] = str[i][j];
                }
            }
            cnt[i] = p+1;
        }
        int ok = 1;
        for (int i = 1; i < n; i++) {
            if (cnt[i] != cnt[i-1]) {
                ok = 0;break;
            }
        }
        if (ok) {
            for (int i = 0; i < cnt[0]; i++) {
                for (int j = 1; j < n; j++) {
                    if (ch[j][i] != ch[j-1][i]) {
                        ok = 0;break;
                    }
                }
            }
        }
        // if (ok) {
        //     for (int i = 0; i < n; i++) {
        //         for (int j = 0; j < cnt[0]; j++) {
        //             printf("%2d", t[i][j]);
        //         }
        //         printf("\n");
        //     }
        // }


        if (ok) {
            for (int i = 0; i < cnt[0]; i++) {
                mini[i] = maxi[i] = t[0][i];
                for (int j = 1; j < n; j++) {
                    mini[i] = min(mini[i], t[j][i]);
                    maxi[i] = max(maxi[i], t[j][i]);
                }
            }
            // for (int i = 0; i < cnt[0]; i++)
            //     printf("%2d", mini[i]);
            // printf("\n");
            // for (int i = 0; i < cnt[0]; i++)
            //     printf("%2d", maxi[i]);
            

            for (int i = 0; i < cnt[0]; i++) {
                int t_min = 1000;
                for (int lv = mini[i]; lv <= maxi[i]; lv++) {
                    int t_ans = 0;
                    for (int j = 0; j < n; j++) {
                        t_ans += abs(t[j][i] - lv);
                    }
                    t_min = min(t_min, t_ans);
                }
                ans += t_min;
            }
        }
        if (ok)         printf("Case #%d: %d\n", tt, ans);
        else            printf("Case #%d: Fegla Won\n", tt);

    }
       
    return 0;
}
