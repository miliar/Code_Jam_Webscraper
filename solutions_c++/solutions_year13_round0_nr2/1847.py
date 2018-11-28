#include <iostream>
#include <cstring>

using namespace std;

enum Result {
     Draw, NC, XW, OW
};

int dirtx[100], dirty[100], a[100][100];

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int N;
    scanf("%d", &N);
    for (int caseNumber = 0; caseNumber < N; caseNumber++) {
        int m, n;
        scanf("%d%d", &m, &n);
        memset(dirtx, 0, sizeof(dirtx));
        memset(dirty, 0, sizeof(dirty));
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++) {
                scanf("%d", &a[i][j]);
                dirtx[i] = max(dirtx[i], a[i][j]);
                dirty[j] = max(dirty[j], a[i][j]);
            }
        bool possible = true;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++)
                if (a[i][j] < dirtx[i] && a[i][j] < dirty[j]) {
                    possible = false;
                    break;
                }
            if (!possible)
                break;
        }

        if (possible)
            printf("Case #%d: YES\n", caseNumber + 1);
        else printf("Case #%d: NO\n", caseNumber + 1);
    }
}

