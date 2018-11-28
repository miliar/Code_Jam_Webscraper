#include<bits/stdc++.h>
using namespace std;
int t,r,c,x,X;
int main()
{
    freopen("inp.txt","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&t);
    while(t--)
    {X++;
        scanf("%d %d %d",&x,&r,&c);
        switch(x)
        {
            case 1: printf("Case #%d: GABRIEL\n",X);
                break;
            case 2: if((r*c)%2==0)
                        printf("Case #%d: GABRIEL\n",X);
                    else
                     printf("Case #%d: RICHARD\n",X);
                    break;
            case 3: if(((r*c)%3==0)&&(r*c)>=6)
                      printf("Case #%d: GABRIEL\n",X);
                    else
                     printf("Case #%d: RICHARD\n",X);
                     break;
            case 4: if(((r*c)%4==0)&&(r*c)>=12)
                     printf("Case #%d: GABRIEL\n",X);
                    else
                     printf("Case #%d: RICHARD\n",X);
                     break;
            }
    }
return 0;
}
