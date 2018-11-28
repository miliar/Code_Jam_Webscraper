#include <stdio.h>
#include <algorithm>

int  idx[100];
char A[100][110];
int  r[100];

using std::min;
using std::max;

int modulo(int x) { return x<0? -x : x; }
int main() {
    int tc,t,n,i;

    scanf("%d",&t);
    for(tc=1; tc<=t; ++tc)
    {
        scanf("%d",&n);
        for(i=0; i<n; ++i) {
            scanf("%s",A[i]);
            idx[i] = 0;
        }

        int  moves = 0;
        bool win   = true;

        while (win)
        {
            int a = 999;
            int b = 0;

            char x = A[0][idx[0]];
            for(i=0; i != n; ++i) {
                win = win && A[i][idx[i]] == x;

                r[i] = -1;
                while (A[i][idx[i]] && A[i][idx[i]] == x) {
                    ++ r[i];
                    ++ idx[i];
                }

                a = min(a, r[i]);
                b = max(b, r[i]);
            }

            if(!x) {
                break;
            }
            else if(win) {
                int ans = 999999;
                for(int k=a; k <= b; ++k) {
                    int need = 0;
                    for (i=0; i != n; ++i) {
                        need+= modulo(r[i] - k);
                    }
                    ans = min(ans, need);
                }
                moves+= ans;
            }
        }

        printf("Case #%d: ", tc);
        if(!win)  printf("Fegla Won\n");
        else      printf("%d\n", moves);
    }
    return 0;
}
