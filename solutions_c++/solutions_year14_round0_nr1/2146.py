#include<cstdio>
int main()
{
int test,n;
freopen("A-small-attempt0.in","r",stdin);
freopen("out.txt","w",stdout);
scanf("%d",&test);
for(int n=1;n<=test;n++)
{
    int A[5][5],a;
    scanf("%d",&a);a--;
    for(int i=0;i<4;i++)
        for(int j=0;j<4;j++)
            scanf("%d",&A[i][j]);
    int B[5][5],b;
    scanf("%d",&b);b--;
    for(int i=0;i<4;i++)
        for(int j=0;j<4;j++)
            scanf("%d",&B[i][j]);
    int same=0,ans;
    for(int i=0;i<4;i++)
        for(int j=0;j<4;j++)
            if(A[a][i]==B[b][j])
            {
                same++;
                ans=A[a][i];
            }
    printf("Case #%d: ",n);
    if(same==0)
        puts("Volunteer cheated!");
    else if(same==1)
        printf("%d\n",ans);
    else
        puts("Bad magician!");

}
return 0;
}
