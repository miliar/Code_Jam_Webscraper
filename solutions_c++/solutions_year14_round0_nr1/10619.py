#include<bits/stdc++.h>
using namespace std;

int main()
{
    int testcases;
    scanf("%d", &testcases);

    for(int i=1; i<=testcases; i++)
    {
        int n1, a1[4][4];
        scanf("%d", &n1);

        for(int j=0; j<4; j++)
            scanf("%d %d %d %d", &a1[j][0], &a1[j][1], &a1[j][2], &a1[j][3]);

        int n2, a2[4][4];
        scanf("%d", &n2);

        for(int j=0; j<4; j++)
            scanf("%d %d %d %d", &a2[j][0], &a2[j][1], &a2[j][2], &a2[j][3]);

        int verify[17]={0};

        for(int j=0; j<4; j++)
            verify[a1[n1-1][j]]++;

        int same=0, value;

        for(int j=0; j<4; j++)
        {
            if(verify[a2[n2-1][j]]==1)
            {
                value=a2[n2-1][j];
                same++;
            }
        }

        if(same==0)
            printf("Case #%d: Volunteer cheated!\n", i);
        else if(same==1)
            printf("Case #%d: %d\n", i, value);
        else
            printf("Case #%d: Bad magician!\n", i);
    }

    return 0;
}
