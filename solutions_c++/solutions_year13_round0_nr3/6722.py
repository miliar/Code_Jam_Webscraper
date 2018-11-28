#include<stdio.h>
int X=0;
void pp(int m,int n)
{
    if(1>=m&&1<=n) X++;
    if(4>=m&&4<=n) X++;
    if(9>=m&&9<=n) X++;
    if(121>=m&&121<=n) X++;
    if(484>=m&&484<=n) X++;
}
int main()
{
//    freopen("E:\\C-small-attempt0.in.txt","r",stdin);
//    freopen("E:\\C-samll-practice.txt","w",stdout);
    int m,n,N,W=0;
    scanf("%d",&N);
    while(N--)
    {
        X=0;W++;
        scanf("%d %d",&m,&n);
        pp(m,n);
        printf("Case #%d: %d\n",W,X);
    }
}
