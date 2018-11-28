#include<cstdio>

int main(void)
{
    int t;
    scanf("%d", &t);
    int grid[4][4], hash[17];
    int i, j, cnt, x, p, c=1;
    while(c<=t)
    {

        for(i=0; i<17; i++)
            hash[i]=0;

        scanf("%d", &x);
        for(i=0; i<4; i++)
            for(j=0; j<4; j++)
                scanf("%d", &grid[i][j]);

        for(i=0; i<4; i++)
            hash[grid[x-1][i]] = 1;

        scanf("%d", &x);
        for(i=0; i<4; i++)
            for(j=0; j<4; j++)
                scanf("%d", &grid[i][j]);
        cnt=0;
        for(i=0; i<4; i++)
        {
            if(hash[grid[x-1][i]] == 1)
            {
                cnt++;
                p = grid[x-1][i];
            }
        }

        printf("Case #%d: ", c);

        if(cnt == 1)
            printf("%d\n", p);

        else if(cnt == 0)
            printf("Volunteer cheated!\n");

        else
            printf("Bad magician!\n" );
        c++;
    }
}
