#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<string>
#include<cstring>

using namespace std;

int c1[5][5], c2[5][5];
int r1, r2;
int est[20];

int main()
{
    freopen("x.in","r",stdin);
    freopen("x.txt","w",stdout);
    int T;
    scanf("%d", &T);
    for(int cas = 1 ; cas <= T ; cas++)
    {
        scanf("%d", &r1);
        r1--;
        for(int i = 0 ; i < 4 ; i++)
            for(int j = 0 ; j < 4 ; j++)
                scanf("%d", &c1[i][j]);
        scanf("%d", &r2);
        r2--;
        for(int i = 0 ; i < 4 ; i++)
            for(int j = 0 ; j < 4 ; j++)
                scanf("%d", &c2[i][j]);
        for(int i = 0 ; i < 16 ; i++)est[i] = 0;
        for(int i = 0 ; i < 4 ; i++)est[c1[r1][i] - 1]++;
        for(int i = 0 ; i < 4 ; i++)est[c2[r2][i] - 1]++;
        printf("Case #%d: ", cas);
        int ans = -1;
        for(int i = 0 ; i < 16 ; i++)
        if(est[i] == 2)
        {
            if(ans != -1){ans = -2;break;}
            ans = i + 1;
        }
        if(ans == -1)puts("Volunteer cheated!");
        else         if(ans == -2)puts("Bad magician!");
                     else         printf("%d\n", ans);
    }
    return 0;
}
