#include<stdio.h>

int main()
{
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A_out.txt", "w", stdout);
    int T;
    int id = 1, ans1, ans2, poss, ans, count;
    int A[4];
    int a[4];
    int B[4];
    int b[4];
    scanf("%d",&T);
    while(T--)
    {
        scanf("%d",&ans1);
        poss = 1;
        while(poss <= 4)
        {
            if(poss == ans1) scanf("%d %d %d %d", &A[0], &A[1], &A[2], &A[3]);
            else scanf("%d %d %d %d", &a[0], &a[1], &a[2], &a[3]);
            poss++;
        }
        scanf("%d",&ans2);
        poss = 1;
        while(poss <= 4)
        {
            if(poss == ans2) scanf("%d %d %d %d", &B[0], &B[1], &B[2], &B[3]);
            else scanf("%d %d %d %d", &b[0], &b[1], &b[2], &b[3]);
            poss++;
        }
        count = 0;
        for(int i=0; i<4; ++i)
        {
            for(int j=0; j<4; ++j)
            {
                if(A[i] == B[j])
                {
                    count++;
                    ans = A[i];
                    break;
                }
            }
        }
        printf("Case #%d: ", id);
        if(count == 1) printf("%d\n", ans);
        else if(count == 0) printf("Volunteer cheated!\n");
        else printf("Bad magician!\n");
        id++;
    }
    return 0;
}