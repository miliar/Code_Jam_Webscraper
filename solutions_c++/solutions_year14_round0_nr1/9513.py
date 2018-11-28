#include<cstdio>
int a[4][4],b[4][4];
int tr[20];
void doit()
{   int op1,op2;
    scanf("%d",&op1);
    for (int i=0;i<=3;i++)
    for (int j=0;j<=3;j++)
        scanf("%d",&a[i][j]);
    scanf("%d",&op2);
    for (int i=0;i<=3;i++)
    for (int j=0;j<=3;j++)
        scanf("%d",&b[i][j]);
    tr[0]=0;
    op1--; op2--;
    for (int i=0;i<=3;i++)
         {
             int now=a[op1][i];
             for (int j=0;j<=3;j++)
             if (b[op2][j]==now)
             tr[++tr[0]]=now;
         }
    if (tr[0]==1){ printf("%d\n",tr[1]);return;}
    if (tr[0]==0){ printf("Volunteer cheated!\n");return;}
    printf("Bad magician!\n");
}
int main()
{    freopen("a.in","r",stdin);
freopen("a.out","w",stdout);
    int cas,i=0;
    scanf("%d",&cas);
    while (cas--)
        {   printf("Case #%d: ",++i);
            doit();
        }
}
