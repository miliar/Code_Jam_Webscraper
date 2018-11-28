#include<stdio.h>

int table[2][5][5];

void play(int t)
{
    int cnttable[20]={0},i,j,k,row[2],cnt=0,ans;
    for (i=0;i<2;++i)
    {
        scanf ("%d",&row[i]);
        row[i]--;
        for (j=0;j<4;++j)
        {
            for (k=0;k<4;++k)scanf ("%d",&table[i][j][k]);
        }
    }
    for (i=0;i<2;++i)
    {
        for (j=0;j<4;++j)
        {
            cnttable[table[i][row[i]][j]]++;
        }
    }
    for (i=1;i<=16;++i)
    {
        if (cnttable[i]>1)
        {
            ans = i;
            cnt++;
        }
    }
    if (cnt == 0)printf ("Case #%d: Volunteer cheated!\n",t);
    else if (cnt == 1)printf ("Case #%d: %d\n",t,ans);
    else printf ("Case #%d: Bad magician!\n",t);
    //return 0;
}

int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("txt.txt","w",stdout);
    int n,i;
    scanf ("%d",&n);
    for (i=0;i<n;++i)play(i+1);
    return 0;
}
