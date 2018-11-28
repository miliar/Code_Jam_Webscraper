#include <iostream>
#include <stdio.h>
#include <cstring>
using namespace std;

bool vis[2050];
char st[20];
int step[2050], que[2050];
int dig[20], dig1[20];

int main(){
        freopen("b.in", "r", stdin);
        freopen("b.out", "w", stdout);

        int tt, ca = 0;
        scanf("%d", &tt);
        while (tt--) {
                scanf("%s", st);
                int n = strlen(st);
                int s0 = 0;
                for (int i = 0; i < n; i++) {
                        int d;
                        if (st[i] == '+') d = 1;
                        else d = 0;
                        s0 = (s0 << 1) + d;
                }


                int res = (1 << n) - 1;
                memset(vis, 0, sizeof(vis));
                que[0] = s0;
                vis[s0] = 1;
                step[s0] = 0;
                int L = 0, R = 1;

                while (L < R && !vis[res]){
                        int s = que[L];
                        L ++;
                        for (int i = 0; i < n; i ++){
                                int t = s;
                                for (int j = 0; j < n; t >>= 1, j ++) dig[j] = t & 1;
                                
                                for (int j = 0; j < i; j ++) dig1[j] = dig[j];
                                for (int j = i; j < n; j ++) dig1[j] = dig[n - 1 - j + i] ^ 1;

                                //cout << i << " : ";for (int j = 0; j < n; j ++) cout << dig[n - j - 1];cout << endl;
                                //cout << i << " : ";for (int j = 0; j < n; j ++) cout << dig1[n - j - 1];cout << endl;
                                
                                int s1 = 0;
                                for (int j = n - 1; j >= 0; j --) s1 = (s1 << 1) | dig1[j];
                                if (!vis[s1]){
                                        vis[s1] = true;
                                        //cout << "s1: " << s1 << endl;
                                        step[s1] = step[s] + 1;
                                        que[R ++] = s1;
                                }
                                
                        }
                }
                
                printf("Case #%d: ", ++ca);
                printf("%d\n", step[res]);
        }
}
