#include<cstdio>

int main()
{
    freopen("A-small-attempt1.in", "r", stdin);
    int T, ans1, ans2, arr1[5][5], arr2[5][5];
    scanf("%d", &T);
    for(int cnt = 1; cnt<=T; ++cnt)
    {
        scanf("%d", &ans1);
        for(int i = 1; i<=4; ++i)
        {
            for(int j = 1; j<=4; ++j)
                scanf("%d", &arr1[i][j]);
        }
        scanf("%d", &ans2);
        for(int i = 1; i<=4; ++i)
        {
            for(int j = 1; j<=4; ++j)
                scanf("%d", &arr2[i][j]);
        }
        int num = arr1[ans1][1], numcnt = 0;
        for(int i = 1; i<=4; ++i)
        {
            for(int j = 1; j<=4; ++j)
            {
                if(arr1[ans1][i]==arr2[ans2][j])
                {
                    ++numcnt;
                    num = arr1[ans1][i];
                }
            }
        }
        FILE* p = fopen("out.txt", "a+");
        if(numcnt == 0)
            fprintf(p, "Case #%d: Volunteer cheated!\n", cnt);
        else if(numcnt > 1)
            fprintf(p, "Case #%d: Bad magician!\n", cnt);
        else
            fprintf(p, "Case #%d: %d\n", cnt, num);
    }
    return 0;
}