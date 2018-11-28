#include<bits/stdc++.h>
using namespace std;
int main()
{
    long long t,i;
    scanf("%lld",&t);
    for(i=1;i<=t;i++)
    {
        long long x,r,c;
        long long j,k,l;
        scanf("%lld%lld%lld",&x,&r,&c);
       if(x==1)
       printf("Case #%lld: GABRIEL\n",i);
       if(x==2)
       {
           if((r*c)%2==0)
            printf("Case #%lld: GABRIEL\n",i);
           else printf("Case #%lld: RICHARD\n",i);
       }
       if(x==3)
       {
           if(r==2 && c==3) printf("Case #%lld: GABRIEL\n",i);
          else if(r==4 && c==3) printf("Case #%lld: GABRIEL\n",i);
           else if(r==3 && c==4) printf("Case #%lld: GABRIEL\n",i);
           else if(r==3 && c==3)printf("Case #%lld: GABRIEL\n",i);
           else if(r==3 && c==2) printf("Case #%lld: GABRIEL\n",i);
           else printf("Case #%lld: RICHARD\n",i);
       }
       if(x==4)
       {
           if(r==4 && c==4) printf("Case #%lld: GABRIEL\n",i);
           else
            if(r==3 && c==4) printf("Case #%lld: GABRIEL\n",i);
           else if(r==4 && c==3) printf("Case #%lld: GABRIEL\n",i);
           else printf("Case #%lld: RICHARD\n",i);
       }
    }
    return 0;
}
