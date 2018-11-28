#include <cstdio>

using namespace std;

int main()
{
    int T[20];
    int t, i, j, x, k, ans, sum;
    freopen ("fis.in", "r", stdin);
    freopen ("fis.out", "w", stdout);
    scanf ("%d\n", &t);
    for (k=1; k<=t; k++)
    {
        for (i=0; i<=16; i++) T[i]=0;
        scanf ("%d\n", &ans);
        for (i=1; i<=4; i++)
            for (j=1; j<=4; j++){
                scanf ("%d", &x);
                if (i == ans)
                    T[x]++;
            }
        scanf ("%d\n", &ans);
        for (i=1; i<=4; i++)
            for (j=1; j<=4; j++){
                scanf ("%d", &x);
                if (i == ans)
                    T[x]++;
            }
        sum = 0;
        for (i=0; i<=16; i++)
            if (T[i] == 2)
                sum++, ans=i;
        printf ("Case #%d: ", k);
        if (sum == 0)
            printf ("Volunteer cheated!\n");
        if (sum > 1)
            printf ("Bad magician!\n");
        if (sum == 1)
            printf ("%d\n", ans);
    }
    
    return 0;
}