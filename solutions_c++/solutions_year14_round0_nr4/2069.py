#include<cstdio>
#include<iostream>
#include<algorithm>
using namespace std;

int main()
{
    // freopen("ans4.txt","w",stdout);
   // freopen(".in","r",stdin);
    int t,k,n,a,b,c,d,i,j,dec,war;

    scanf("%d",&t);
 for( k=1;k<=t;k++)

    {
        dec=0;
   war=0;
        scanf("%d",&n);
        float arr1[n],arr2[n];
        for(i=0;i<n;i++)
        {
            scanf("%f",&arr1[i]);
        }
        for(j=0;j<n;j++)
        {
           scanf("%f",&arr2[j]);
        }
        sort(arr1,arr1+n);
        sort(arr2,arr2+n);
        a=0;
        b=n-1;
        c=0;
        d=n-1;
       // int ans=0;
       while(a<=b)
       {
        if((arr1[a]>arr2[c])&&(arr2[b]>arr2[d])&&(a==0))
        {

            dec=n;
            break;

        }
        else if(arr1[a]<arr2[c])
        {
            ++a;
            --d;
        }
        else if((arr1[a]>arr2[c])&&(arr1[b]>arr2[d]))

        {
            ++a;
            ++c;
            ++dec;
        }
        else
        {
            ++a;
            --d;
        }
       }
  a=0;
        b=n-1;
        c=0;
        d=n-1;
        while(a<=b)
        {
            if(arr1[b]>arr2[d])
            {
                --b;
                ++c;
               ++war;
            }
            else
            {
             --b;
             --d;
            }
        }
       printf("Case #%d: %d %d\n",k,dec,war);
    }
return 0;
}
