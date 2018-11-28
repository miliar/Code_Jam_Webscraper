#include <iostream>
#include <cstdio>

using namespace std;

int row, card, a[10], b[10];
int m[50][50];

void citire(int v[])
{
    scanf("%d",&row);
    for (int i=1; i<=4; i++)
        for (int j=1; j<=4; j++)
            scanf("%d",&m[i][j]);

    for (int j=1; j<=4; j++)
        v[j] = m[row][j];
}

void solve(int output)
{
    int nr = 0;
    int card;

    for (int i=1; i<=4; i++)
        for (int j=1; j<=4; j++)
            if (a[i] == b[j])
            {
                nr++;
                card = a[i];
            }
    if (nr == 0)
        printf("Case #%d: Volunteer cheated!\n", output);
    else
        if (nr > 1)
            printf("Case #%d: Bad magician!\n", output);
        else
            printf("Case #%d: %d\n",output, card);

}

int main()
{
    freopen("magician.in","r",stdin);
    freopen("magician.out","w",stdout);
    int T;
    scanf("%d",&T);
    for (int input=1; input<=T; input++)
    {
        citire(a);
        citire(b);
        solve(input);
    }
    return 0;
}
