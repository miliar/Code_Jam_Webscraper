#include<stdio.h>

int ans[10],cnt[300];
char str[2010];

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("txt.txt","w",stdout);
    int t,ti,i,j;
    scanf ("%d",&t);
    for (ti=0;ti<t;++ti)
    {
        scanf ("%s",str);
        for (i=0;i<300;++i)cnt[i]=0;
        for (i=0;str[i];++i)cnt[str[i]]++;
        ans[0] = cnt['Z'];
        ans[2] = cnt['W'];
        ans[4] = cnt['U'];
        ans[6] = cnt['X'];
        ans[8] = cnt['G'];
        ans[1] = cnt['O'] - ans[0] - ans[2] - ans[4];
        ans[3] = cnt['T'] - ans[2] - ans[8];
        ans[5] = cnt['F'] - ans[4];
        ans[7] = cnt['S'] - ans[6];
        ans[9] = cnt['I'] - ans[8] - ans[6] - ans[5];
        printf ("Case #%d: ",ti+1);
        for (i=0;i<10;++i)
        {
            for(j=0;j<ans[i];++j)printf ("%d",i);
        }
        printf ("\n");

    }
    return 0;
}
