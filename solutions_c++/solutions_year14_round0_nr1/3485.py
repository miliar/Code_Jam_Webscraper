#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

int t, card1[10][10], card2[10][10], a1, a2;

int main(void)
{
    freopen("A-small-attempt1.in", "r", stdin);
    freopen("A-small-attempt1.out", "w", stdout);

    int i, j, k, ans, cas=1;

    scanf("%d", &t);
    while(t--)
    {
        scanf("%d", &a1);
        for(i=1; i<=4; ++i)
            for(j=1; j<=4; ++j) scanf("%d", &card1[i][j]);
        scanf("%d", &a2);
        for(i=1; i<=4; ++i)
            for(j=1; j<=4; ++j) scanf("%d", &card2[i][j]);

        k=0;
        for(i=1; i<=4; ++i)
            for(j=1; j<=4; ++j)
            {
                if(card1[a1][i]==card2[a2][j])
                {
                    ans=card1[a1][i]; k++;
                }
            }

        if(k==0) printf("Case #%d: Volunteer cheated!\n", cas++);
        else if(k==1) printf("Case #%d: %d\n", cas++, ans);
        else printf("Case #%d: Bad magician!\n", cas++);
    }

    return 0;
}
