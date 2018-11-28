#include <cstdio>
#include <cstring>

using namespace std;

int cnt[20];

int main ()
{
    int No; scanf ("%d", &No);

    for (int _i = 0; _i < No; ++_i) {
        memset(cnt, 0, sizeof cnt);

        for (int i = 0; i < 2; ++i) {
            int g; scanf ("%d", &g); --g;
            for (int j = 0; j < 4; ++j) {
                for (int k = 0; k < 4; ++k) {
                    int x; scanf ("%d", &x); --x;
                    if (j == g) ++cnt[x];
                }
            }
        }
        
        printf ("Case #%d: ", _i + 1);
        int dva = 0;
        for (int i = 0; i < 16; ++i)
            if (cnt[i] == 2) ++dva;
        if (dva == 0) printf ("Volunteer cheated!\n");
        else if (dva > 1) printf ("Bad magician!\n");
        else {
            for (int i = 0; i < 16; ++i)
                if (cnt[i] == 2) printf ("%d\n", i + 1);
        }
    }

    return 0;
}

