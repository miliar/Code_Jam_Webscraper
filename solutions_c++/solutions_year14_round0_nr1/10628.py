#include <cstdio>
#include <cstring>
#define MAXN 4

int used[MAXN*MAXN];

int main(void){
    int test; scanf ("%d", &test);
    for (int _test=0; _test<test; _test++){
        memset(used, 0, sizeof(used));

        int ans1; scanf ("%d", &ans1);
        for (int i=0; i<4; i++)
            for (int j=0; j<4; j++){
                int a; scanf ("%d", &a);
                if (i+1 == ans1) used[a-1]++;
            }

        int ans2; scanf ("%d", &ans2);
        for (int i=0; i<4; i++)
            for (int j=0; j<4; j++){
                int a; scanf ("%d", &a);
                if (i+1 == ans2) used[a-1]++;
            }

        printf ("Case #%d: ", _test+1);

        int sol = -1;
        bool ok = true;
        for (int i=0; i<16; i++)
        if (used[i] == 2){
            if (sol != -1) { printf ("Bad magician!\n"); ok = false; break; }
            sol = i + 1;
        }

        if (!ok) continue;

        if (sol == -1) printf ("Volunteer cheated!\n");
        else printf ("%d\n", sol);

    }



    return 0;
}
