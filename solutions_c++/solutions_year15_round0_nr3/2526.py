#include <stdio.h>
#include <string.h>
#include <algorithm>

using namespace std;

char ss[11000];
char buf[11000];
bool vis[11000];

int table[300][300];

int main()
{
    int T;

    //freopen("input.txt", "r", stdin);
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("C-small-attempt0.out", "w", stdout);

    table['1']['1'] = '1';
    table['1']['i'] = 'i';
    table['1']['j'] = 'j';
    table['1']['k'] = 'k';
    
    table['i']['1'] = 'i';
    table['i']['i'] = -1 * '1';
    table['i']['j'] = 'k';
    table['i']['k'] = -1 * 'j';


    table['j']['1'] = 'j';
    table['j']['i'] = -1 * 'k';
    table['j']['j'] = -1 * '1';
    table['j']['k'] = 'i';

    table['k']['1'] = 'k';
    table['k']['i'] = 'j';
    table['k']['j'] = -1 * 'i';
    table['k']['k'] = -1 * '1';

    
    scanf("%d", &T);

    for (int cn = 1; cn <= T; cn++) {

        int L, X;
        scanf("%d%d", &L, &X);

        scanf("%s", buf);

        ss[0] = 0;

        for (int i = 0; i < X; i++) {
            strcat(ss, buf);
        }

        memset(vis, false, sizeof(vis));

        int n = L * X;

        int v = '1';
        int sign = 1;

        for (int i = n - 1; i >= 0; i--) {
            int x = table[ss[i]][v];
            if (x < 0) {
                sign *= -1;
                v = -x;
            } else {
                v = x;
            }
            if (v == 'k' && sign == 1) {
                vis[i] = true;
            }
        }
        bool ok = false;
        int I = '1', signI = 1;
        for (int i = 0; i < n; i++) {
            int x = table[I][ss[i]];
            if (x < 0) {
                signI *= -1;
                I = -x;
            } else {
                I = x;
            }
            if (I == 'i' && signI == 1) {
                int J = '1', signJ = 1;
                for (int j = i + 1; j < n; j++) {
                    int x = table[J][ss[j]];
                    if (x < 0) {
                        signJ *= -1;
                        J = -x;
                    } else {
                        J = x;
                    }

                    if (J == 'j' && signJ == 1 && vis[j + 1]) {
                        ok = true;
                        break;
                    }
                    
                }

                if (ok) {
                    break;
                }
            }
        }

        printf("Case #%d: %s\n", cn, ok ? "YES" : "NO");
        
        
    }
    
    return 0;
}
