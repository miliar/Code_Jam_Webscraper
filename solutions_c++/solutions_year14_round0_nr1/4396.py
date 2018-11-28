#include <cstdio>
#include <cstring>

bool invalid[16];
int tiles[4][4];

int main()
{
    int TC = 0;
    scanf("%d", &TC);

    for(int tc = 1; tc <= TC; ++tc)
    {
        memset(invalid, false, sizeof(invalid));
        int ans = -1;
        for(int i = 0; i < 2; i++)
        {

            int row = 0;
            scanf("%d", &row);
            for(int a = 0; a < 4; a++)
                for(int b = 0; b < 4; b++)
                    scanf("%d", &tiles[a][b]);
            --row;

            for(int a = 0; a < 4; a++)
            {
                if(a == row) continue;
                for(int b = 0; b < 4; b++)
                    invalid[ tiles[a][b]-1 ] = true;
            }
        }
        for(int i = 0; i < 16; i++)
            if(!invalid[i])
            {
                if(ans == -1) ans = i;
                else
                {
                    ans = -2;
                    break;
                }
            }

        if(ans == -2)
            printf("Case #%d: Bad magician!\n", tc); 
        else if(ans == -1)
            printf("Case #%d: Volunteer cheated!\n", tc); 
        else
            printf("Case #%d: %d\n", tc, ans+1); 
    }
    return 0;
}
