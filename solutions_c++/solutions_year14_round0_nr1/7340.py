#include <cstdio>
using namespace std;

int T, R1, R2, X, Freq[20], Cnt;

int main()
{
   // freopen("test.in", "r", stdin);
   // freopen("test.out", "w", stdout);

    scanf("%i", &T);
    for(int t = 1; t <= T; ++ t)
    {
        for(int i = 1; i <= 16; ++ i) Freq[i] = 0;
        Cnt = 0;

        scanf("%i", &R1);
        for(int i = 1; i <= 4; ++ i)
            for(int j = 1; j <= 4; ++ j)
            {
                scanf("%i", &X);
                if(i == R1)
                    Freq[X] ++;
            }

        scanf("%i", &R2);
        for(int i = 1; i <= 4; ++ i)
            for(int j = 1; j <= 4; ++ j)
            {
                scanf("%i", &X);
                if(i == R2)
                    Freq[X] ++;
            }

        for(int i = 1; i <= 16; ++ i)
            Cnt += Freq[i] == 2;

        if(Cnt == 1)
        {
            for(int i = 1; i <= 16; ++ i)
                if(Freq[i] == 2)
                    printf("Case #%i: %i\n", t, i);
        }else
        {
            if(Cnt == 0) printf("Case #%i: Volunteer cheated!\n", t);
            else printf("Case #%i: Bad magician!\n", t);
        }
    }
    return 0;
}
