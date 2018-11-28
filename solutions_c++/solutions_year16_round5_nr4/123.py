#include <bits/stdc++.h>

using namespace std;

typedef pair<int, int> ii;

int T, C=1;
int n, L;
set<string> G;
char s[1024];

int main() {

    for(scanf("%d",&T);T--;) {
        printf("Case #%d: ",C++);
        scanf("%d %d",&n,&L);
        G.clear();
        for (int i=0;i<n;i++) {
            scanf("%s",s);
            string good = s;
            G.insert(good);
        }
        scanf("%s",s);
        string bad = s;
        if (G.find(bad) != G.end()) {
            printf("IMPOSSIBLE\n");
        } else {
            if (L == 1)
                printf("? 0\n");
            else {
                for (int i=0;i<L-1;i++)
                    printf("?");
                printf(" 10?1");
                int t=0;
                for (int i=0;i<198-(L-1)-4;i++) {
                    printf("%d",t);
                    t ^= 1;
                }
                printf("\n");
            }
        }

    }

    return 0;
}
