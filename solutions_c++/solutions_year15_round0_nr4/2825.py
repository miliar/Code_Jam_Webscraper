#include<bits/stdc++.h>
using namespace std;
int main()
{
    long long int t,n,r,c,j;
    scanf("%lld",&t);
    for(j=1;j<=t;j++)
    {
        scanf("%lld%lld%lld",&n,&r,&c);
        if(n==1)
            {
              printf("Case #%lld: GABRIEL\n",j);
            }
        else if(n==2)
        {
            if((r*c)%2!=0)
                printf("Case #%lld: RICHARD\n",j);
            else
                printf("Case #%lld: GABRIEL\n",j);
        }
        else if(n==3)
        {
           if((r*c)%3!=0)
                printf("Case #%lld: RICHARD\n",j);
           else
           {
             if((r==3&&c==1)||(c==3&&r==1)||(c==2&&r==2)||(r==4&&c==4))
               printf("Case #%lld: RICHARD\n",j);
             else
                printf("Case #%lld: GABRIEL\n",j);

           }

        }
        else if(n==4)
        {
            if((r==3&&c==4)||(c==3&&r==4)||(r==4&&c==4))
                 printf("Case #%lld: GABRIEL\n",j);
            else
                 printf("Case #%lld: RICHARD\n",j);
        }

    }
    return 0;
}
