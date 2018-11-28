#include <iostream>
#include <cstdio>

using namespace std;

int T;
int A[4];
int B[4];
int ans;
int main()
{
    freopen("A-small-attempt1.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    scanf("%d", &T);
    for (int i = 1; i <= T; i++) {
        int n;
        scanf("%d", &ans);
        for (int j = 0; j < 16; j++) {
            scanf("%d", &n);
            if (j >= (ans - 1) * 4 && j < ans * 4) A[j % 4] = n;
        }
        scanf("%d", &ans);
        for (int j = 0; j < 16; j++) {
            scanf("%d", &n);
            if (j >= (ans - 1) * 4 && j < ans * 4) B[j % 4] = n;
        }
        int k = 0;
        for (int x = 0; x < 4; ++x) {
            for (int y = 0; y < 4; ++y) {
                if (A[x] == B[y]) {
                    ans = A[x];
                    k++;
                }
            }
        }
        if (k == 0) printf("Case #%d: Volunteer cheated!\n", i);
        else if (k == 1) printf("Case #%d: %d\n", i, ans);
        else printf("Case #%d: Bad magician!\n", i, ans);
    }
}
