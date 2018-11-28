#include<stdio.h>
#include<string.h>
int frq[20];
int mat[5][5];
void go()
{
    int row;
    scanf("%d",&row);
    for(int i = 0;i<4;i++)
    for(int j=0;j<4;j++)
        scanf("%d",&mat[i][j]);

    row--;
    for(int j = 0; j<4;j++)
        frq[mat[row][j]]++;
}
int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("out.out","w",stdout);
    int T;
    scanf("%d",&T);
    int casenum = 0;
    while(T--)
    {
        casenum ++;
        printf("Case #%d: ",casenum);
        memset(frq,0,sizeof frq);
        go();
        go();
        int c = 0,sv;
        for(int i=1;i<=16;i++)
        if(frq[i] == 2)
        {
            //printf("%d %d\n",i,frq[i]);
            sv = i;
            c++;
        }
        if(c == 1)
            printf("%d\n",sv);
        if(c >= 2)
            printf("Bad magician!\n");
        if(c == 0)
            printf("Volunteer cheated!\n");
    }

}
