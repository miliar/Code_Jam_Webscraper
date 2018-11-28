#include <iostream>
#include <algorithm>
#include <string>
#include <cstdio>

using namespace std;

int A[4][4], B[4][4];
int rowA, rowB;
int ans;

void init()
{
    scanf("%d", &rowA);
    for (int i=0; i<4; i++)
        for (int j=0; j<4; j++)
            scanf("%d", &A[i][j]);
    scanf("%d", &rowB);
    for (int i=0; i<4; i++)
        for (int j=0; j<4; j++)
            scanf("%d", &B[i][j]);
}

int work()
{
    int res = 0;
    rowA --;
    rowB --;
    for (int i=0; i<4; i++)
        for (int j=0; j<4; j++)
            if (A[rowA][i] == B[rowB][j])
            {
                ans = A[rowA][i];
                res++;
            }
    return res;
}


int main()
{
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small-attempt0.out", "w", stdout);
    
    int T;
    scanf("%d", &T);
    for (int tim=1; tim<=T; tim++)
    {
        init();
        int cnt = work();
        printf("Case #%d: ", tim);
        if (cnt == 0)
            printf("Volunteer cheated!\n");
        else if (cnt > 1)
            printf("Bad magician!\n");
        else
            printf("%d\n", ans);
    }
}
