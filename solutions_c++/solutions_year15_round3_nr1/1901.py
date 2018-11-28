#include<stdio.h>
int main()
{
    freopen("A-small-attempt3.in","r",stdin);
    freopen("output.txt","w",stdout);
    int i,r,c,w,t;
    scanf("%d",&t);
    for(i=0;i<t;i++)
    {
        scanf("%d%d%d",&r,&c,&w);
        if(w==c)
            printf("Case #%d: %d\n",i+1,w);
        else if(w>c/2||(w==c/2&&c%2==0))
            printf("Case #%d: %d\n",i+1,w+1);
        else if(c%w)
            printf("Case #%d: %d\n",i+1,c/w+w);
        else
            printf("Case #%d: %d\n",i+1,c/w+w-1);
    }
}
            
