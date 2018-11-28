#include<cstdio>
int main()
{
    freopen("input1.txt","r",stdin);
    freopen("output1.txt","w",stdout);
    int t,i,x,r,c;
    scanf("%d",&t);
    for(i=1;i<=t;i++)
    {
        scanf("%d %d %d",&x,&r,&c);
        printf("Case #%d: ",i);
        if(r<c)
        {
            int a=r;
            r=c;
            c=a;
        }
        if(x==1) printf("GABRIEL");
        if(x==2)
        {
            if(r*c%2==0) printf("GABRIEL");
            else printf("RICHARD");
        }
        if(x==3)
        {
            if((r==3 && c==2) || (r==4 && c==3) || (r==3 && c==3)) printf("GABRIEL");
            else printf("RICHARD");
        }
        if(x==4)
        {
            if((r==4 && c==3) || (r==4 && c==4)) printf("GABRIEL");
            else printf("RICHARD");
        }
        printf("\n");
    }
    return 0;
}
