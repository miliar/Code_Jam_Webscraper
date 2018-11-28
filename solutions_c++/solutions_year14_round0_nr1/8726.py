#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<iostream>

using namespace std;

int check[20];

int main(void)
{
    int T;
    freopen("A-small-attempt0.in","r", stdin);
    freopen("A.out","w", stdout);
    scanf("%d",&T);
    for(int t = 0; t<T; t++)
    {
        int first;
        scanf("%d", &first);
        int a[4][4];
        memset(check, 0, sizeof(check));

        for(int i = 0; i<4; i++)
        {
            for(int j = 0; j<4; j++)
            {
                scanf("%d", &a[i][j]);
            }
        }

        for(int i = 0; i<4; i++)
        {
            check[a[first - 1][i]]++;
        }

        int second;
        scanf("%d", &second);
        int b[4][4];
        for(int i = 0; i<4; i++)
        {
            for(int j = 0; j<4; j++)
            {
                scanf("%d", &b[i][j]);
            }
        }

        int got = 0;
        int ans = 0;
        for(int i = 0; i<4; i++)
        {
            if(check[b[second - 1][i]])
            {
                got++;
                ans = b[second - 1][i];
            }
        }

        printf("Case #%d: ", t+1);
        if(got == 1)
            printf("%d\n", ans);
        else if(got > 1)
            puts("Bad magician!");
        else if(got == 0)
            puts("Volunteer cheated!");
    }
    return 0;
}
