#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;
int main()
{       
    freopen("D-small-attempt1.in","r",stdin);
    freopen("out.txt","w",stdout);
    ll t,i;
    scanf("%lld",&t);

    for(i=1;i<=t;i++)
    {  
        int flag =0;
        ll n,r,c ;
        scanf("%lld %lld %lld",&n,&r,&c);


        if((r*c)<n)
        flag=1;

        
        else
        {
            if(((r*c)%n)!=0)
                flag=1;
        
            else
             if(r+c-1<=n)
                flag=1;
        }

        if(n==2&&r*c==2)
        flag=0;

        if(n==4&&r==2&&c==4)
        flag=1;
        
        if(n==1&&r==1&&c==1)
        flag=0;
        
        if(n==4&&r==4&&c==2)
        flag=1;
        
        if(flag)          
            printf("Case #%lld: RICHARD\n",i);
        
        else            
            printf("Case #%lld: GABRIEL\n",i);
    }

    fclose(stdout);
    fclose(stdin);
    return 0;
}
