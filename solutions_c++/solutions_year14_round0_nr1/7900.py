#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;
const int N = 4;
int a[N][N], b[N][N];
int main(){
    int T, cas = 0;
    freopen("A-small-attempt2.in","r",stdin);
    freopen("out.txt","w",stdout);
    cin >> T;
    while (T--) {
        int n, m;
        cin >> n;
        for (int i = 0; i < 4; i++)
            for (int j = 0; j < 4; j++) cin >> a[i][j];
        cin >> m;
        for (int i = 0; i < 4; i++)
            for (int j = 0; j < 4; j++) cin >> b[i][j];
        int ans = -1;
        printf("Case #%d: ",++cas);
        int ffg = 0;
        for (int i = 0; i < 4; i++) {
            int fg = 0;
            for (int j = 0; j < 4; j++) {
                if (a[n-1][i] == b[m-1][j]) {
                    fg = 1;
                    break;
                }
            }
            if (fg) {
                if (ans == -1) ans = a[n-1][i];
                else {
                    printf("Bad magician!\n");
                    ffg = 1;
                    break;
                }
            }
        }
        if (ffg == 0){
            if (ans == -1) {
                printf("Volunteer cheated!\n");
            }else printf("%d\n",ans);
        }
    }
    return 0;
}
