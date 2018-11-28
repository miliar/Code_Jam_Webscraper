#include<stdio.h>
#include<stdlib.h>

main()
{
    int a,t;
    scanf("%d",&t);
    for(a=0;a<t;a++)
    {
        int x,r,c;
        scanf("%d %d %d",&x,&r,&c);
        printf("Case #%d: ",a+1);
        int area=r*c;
        if(area%x==0)
        {
            if(x==4)
            {
                if(r<=2 || c<=2) printf("RICHARD\n");
                else printf("GABRIEL\n");
            }
            else if(x==3)
            {
                if(r==1 || c==1) printf("RICHARD\n");
                else printf("GABRIEL\n");
            }
            else printf("GABRIEL\n");
        }
        else printf("RICHARD\n");
    }
}
