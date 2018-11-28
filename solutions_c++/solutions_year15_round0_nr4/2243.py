#include<bits/stdc++.h>
using namespace std;
int main()
{
    //freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int T,t,i,j,k,a,r,c;
    scanf("%d",&T);
    int fu=0;
    for(t=0;t<T;t++)
    {
        scanf("%d %d %d",&a,&r,&c);
        fu=0;
        printf("Case #%d: ",t+1);
        switch(a)
        {
        case 1:
            printf("GABRIEL\n");
            break;
        case 2:
            if((r*c)%2==0&&r*c>1)
            {
                printf("GABRIEL\n");
            }
            else
                printf("RICHARD\n");
            break;
        case 3:
            if(3>r&&3>c)
            {
                printf("RICHARD\n");
            }
            else if(r==1||c==1)
            {
                printf("RICHARD\n");
            }
            else
            {
                if((r*c)%3==0)
                    printf("GABRIEL\n");
                else
                    printf("RICHARD\n");
            }
            break;
        case 4:
            if(4>r&&4>c)
            {
                printf("RICHARD\n");
            }
            else if(r==1||c==1)
            {
                printf("RICHARD\n");
            }
            else if((r==4&&c==2)||(r==2&&c==4))
            {
                printf("RICHARD\n");
            }
            else
            {
                if((r*c)%4==0)
                    printf("GABRIEL\n");
                else
                    printf("RICHARD\n");
            }
            break;
        }


    }
}
