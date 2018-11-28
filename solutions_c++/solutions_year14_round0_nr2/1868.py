#include<stdio.h>

int main()
{
/*
    freopen("inp2.in","r+",stdin);
    freopen("out2.out","w+",stdout);

*/

    freopen("ques22.in","r+",stdin);
    freopen("out22.out","w+",stdout);

    int t;
    scanf("%d",&t);

    int k=0;
    while(t--)
     {
         k++;

         double ans=0.00;

         double c,f,x;
         scanf("%lf %lf %lf",&c,&f,&x);

        // printf("c:%lf f:%lf x:%lf\n",c,f,x);

         if(c>x)
           ans=x/2;
         else
         {
            int rate=2;
            int cnt=0;

            while(1)
             {
                cnt++;

                double lhs=(x)/(2+cnt*f);
                double rhs=(x-c)/(2+(cnt-1)*f);

                if(lhs >= rhs)
                    break;
             }

            cnt--;
           //printf("Number of stations : %d\n",cnt);

            int i;
            for(i=0;i<cnt;i++)
              {
                ans+=c/(2+i*f);
              }
            ans+=((x)/(2+cnt*f));

          }

          printf("Case #%d: %.7lf\n",k,ans);
     }
    return 0;
}
