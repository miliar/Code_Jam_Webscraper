#include<bits/stdc++.h>
int main()
{
    int t,x,r,c,i,row,col;
    scanf("%d",&t);
    for(i=1;i<=t;i++)
    {
        scanf("%d %d %d",&x,&row,&col);
        r=row>col?row:col;
        c=row+col-r;
        if(r<x)
            printf("Case #%d: RICHARD\n",i);
        else
        {
            if(x==1)
                printf("Case #%d: GABRIEL\n",i);
            else if(x==2)
            {
                if((r*c)%2==0)
                    printf("Case #%d: GABRIEL\n",i);
                else
                    printf("Case #%d: RICHARD\n",i);
            }
            else if(x==3)
            {
                if(r==3)
                {
                    if(c==1)
                        printf("Case #%d: RICHARD\n",i);
                    else
                        printf("Case #%d: GABRIEL\n",i);
                }
                else if(r==4)
                {
                    if(c==3)
                        printf("Case #%d: GABRIEL\n",i);
                    else
                        printf("Case #%d: RICHARD\n",i);
                }
            }
            else
            {
                if(c>2)
                    printf("Case #%d: GABRIEL\n",i);
                else
                    printf("Case #%d: RICHARD\n",i);
            }
        }
    }
    return 0;
}
