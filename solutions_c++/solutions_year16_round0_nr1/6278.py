#include <bits/stdc++.h>
#define LL long long int
using namespace std;

int main()
{
    freopen("input_file_name.in","r",stdin);
    freopen("output_file_name.out","w",stdout);
    LL T,t=1;
    scanf("%lld",&T);
    while(T--)
    {
       LL n,n2,i,j,k,l,cnt1=0,cnt2=0;
       LL arr[10];
       memset(arr,0,sizeof(arr));

       scanf("%lld",&n);
       n2=n;
       l=0;j=1;
       LL r;

       if (n==0)
       {
          printf("Case #%lld: INSOMNIA\n",t);
t++;
       }
       else
       {
             while(l<1)
       {
           cnt1=0;

         while(n!=0)
         {
            r=n%10;
            arr[r]=1;

            n=n/10;
         }

            for (i=0;i<10;i++)
              {

                  if (arr[i]==1) cnt1++;
              }

           if (cnt1==10)
           {

               break;
           }
           else {
                 j++;
              n=j*n2;
            l=0;
           }

       }

printf("Case #%lld: %lld\n",t,j*n2);
t++;
       }



    }
    return 0;
}
