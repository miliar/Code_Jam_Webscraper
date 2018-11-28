#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <string>
#include <cmath>
#include <cstring>

using namespace std;

typedef long long ll;
typedef long double ldb;

#define forab(i, a, b) for(int i = int(a); i < int(b); ++i)
#define forba(i, b, a) for(int i = int(b) - 1; i >= int(a); --i)
#define forn(i, n) forab(i, 0, n)

int k[20];

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int T;
    scanf("%d ", &T);
    forn(t, T) {
        printf("Case #%d: ", t + 1);
        memset(k, 0, sizeof(k));
        forn(q, 2) {
            int x;
            scanf("%d", &x);
            x--;
            forn(i, 4)
                forn(j, 4) {
                    int tmp;
                    scanf("%d", &tmp);
                    if (x == i)
                        k[tmp]++;
                }
        }

        int ans = -1;

        forn(i, 16)
            if (k[i + 1] == 2) {
                if (ans == -1)
                    ans = i + 1;
                else ans = -2;
            }

        if (ans == -1)
            printf("Volunteer cheated!\n");
        else if (ans == -2)
            printf("Bad magician!\n");
        else 
            printf("%d\n", ans);
    }
    return 0;
}
