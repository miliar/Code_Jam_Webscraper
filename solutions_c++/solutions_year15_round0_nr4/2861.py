#include<stdio.h>
#include<iostream>
int main()
{
    int i,j,t,c,r,x;
    FILE *out;
    FILE *in;
    in=freopen("D-small-attempt0.in","r",stdin);
    out=freopen("out.txt","w",stdout);
    scanf("%d",&t);
    for(i=0;i<t;i++)
    {
        scanf("%d%d%d",&x,&r,&c);
        if(x==1)
            printf("Case #%d: GABRIEL\n",i+1);
        else if(x==2 && (r*c)%2==0)
            printf("Case #%d: GABRIEL\n",i+1);
        else if(x==3 && ((r*c)==9 || (r*c)==12 || (r*c)==6))
                printf("Case #%d: GABRIEL\n",i+1);
        else if(x==4 && ((r*c)==12 || (r*c)==16))
            printf("Case #%d: GABRIEL\n",i+1);
        else
            printf("Case #%d: RICHARD\n",i+1);
    }
}
