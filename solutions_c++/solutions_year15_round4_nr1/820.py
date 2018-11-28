#include <cstdio>

using namespace std;

int t, n, m;
bool ima, imaNegde;
char s[120][120];

int main() {
    freopen("A-large.in","r",stdin);
    freopen("A-out0large.out","w",stdout);
    scanf("%d",&t);
    for (int tp=1; tp<=t; tp++) {
        scanf("%d %d",&n, &m);
        for (int i=1; i<=n; i++) scanf("%s", s[i]+1);
        bool nemoguce = 0;
        int sol = 0;
        for (int i=1; i<=n; i++) {
            for (int j=1; j<=m; j++) {
                if (s[i][j] == '.') continue;
                imaNegde = 0;
                for (int k=1; k<=n; k++) if (k!=i && s[k][j] != '.') imaNegde = 1;
                for (int k=1; k<=m; k++) if (k!=j && s[i][k] != '.') imaNegde = 1;
                if (s[i][j] == '^') {
                    ima = 0;
                    for (int k=1; k<i; k++) if (s[k][j] != '.') ima=1;
                    if (!ima) {
                        if (imaNegde) sol++;
                        else nemoguce=1;
                    }
                }
                else if (s[i][j] == 'v') {
                    ima = 0;
                    for (int k=i+1; k<=n; k++) if (s[k][j] != '.') ima=1;
                    if (!ima) {
                        if (imaNegde) sol++;
                        else nemoguce=1;
                    }
                }
                else if (s[i][j] == '<') {
                    ima = 0;
                    for (int k=1; k<j; k++) if (s[i][k] != '.') ima=1;
                    if (!ima) {
                        if (imaNegde) sol++;
                        else nemoguce=1;
                    }
                }
                else if (s[i][j] == '>') {
                    ima = 0;
                    for (int k=j+1; k<=m; k++) if (s[i][k] != '.') ima=1;
                    if (!ima) {
                        if (imaNegde) sol++;
                        else nemoguce=1;
                    }
                }

                if (nemoguce) break;
             }
             if (nemoguce) break;
        }
        printf("Case #%d: ", tp);
        if (nemoguce) printf("IMPOSSIBLE\n");
        else printf("%d\n", sol);
    }


    return 0;
}
