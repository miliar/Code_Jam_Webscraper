#include<bits/stdc++.h>
using namespace std;

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);

   int t,ts;
   scanf("%d",&ts);

   for(t=1;t<=ts;t++)
   {
       long long int i,j,k,mx=1023,msk=0,num,ans=-1;

       scanf("%lld",&num);

       for(i=1;i<=1000000;i++)
       {

           k=num*i;
           while(k!=0)
           {
               j=k%10;
               msk=msk|(1<<(j));
               k=k/10;
           }

           if(msk==mx)
           {
               ans=i*num;
               break;
           }
       }
       if(ans==-1)
        printf("Case #%d: INSOMNIA\n",t);
       else
        printf("Case #%d: %lld\n",t,ans);
   }
}
