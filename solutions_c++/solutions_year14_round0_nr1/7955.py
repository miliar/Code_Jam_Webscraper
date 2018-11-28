#include<bits/stdc++.h>
using namespace std;

int main()
{
    int testcases;
    scanf("%d", &testcases);

    for(int i=1; i<=testcases; i++)
    {
        int n1, arr1[4][4];
        scanf("%d", &n1);

        for(int j=0; j<4; j++)
            scanf("%d %d %d %d", &arr1[j][0], &arr1[j][1], &arr1[j][2], &arr1[j][3]);

        int n2, arr2[4][4];
        scanf("%d", &n2);

        for(int j=0; j<4; j++)
            scanf("%d %d %d %d", &arr2[j][0], &arr2[j][1], &arr2[j][2], &arr2[j][3]);

        int check[17]={0};

        for(int j=0; j<4; j++)
            check[arr1[n1-1][j]]++;

        int same=0, ans;

        for(int j=0; j<4; j++)
        {
            if(check[arr2[n2-1][j]]==1)
            {
                ans=arr2[n2-1][j];
                same++;
            }
        }

        if(same==0)
            printf("Case #%d: Volunteer cheated!\n", i);
        else if(same==1)
            printf("Case #%d: %d\n", i, ans);
        else
            printf("Case #%d: Bad magician!\n", i);
    }

    return 0;
}
