#include <cstdio>
using namespace std;

int main()
{
    int T;
    scanf("%d", &T);

    for(int tt = 1; tt <= T; tt++)
    {
        printf("Case #%d: ", tt);

        int times[20] = {};
        for(int k = 0; k < 2; k++)
        {
        int r;
        scanf("%d", &r);
        for(int i = 0; i < 4; i++)
            for(int j = 0; j < 4; j++)
            {
                int v;
                scanf("%d", &v);

                if(i + 1 == r)
                    times[v]++;
            }
        }

        int ans = 0;
        for(int i = 1; i <= 16; i++)
            if(times[i] == 2)
            {
                if(ans)
                    ans = -1;
                else
                    ans = i;
            }
        if(ans == -1)
            puts("Bad magician!");
        else if(!ans)
            puts("Volunteer cheated!");
        else
            printf("%d\n", ans);
            
    }

    return 0;
}
