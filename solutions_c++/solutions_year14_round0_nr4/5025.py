#include<stdio.h>
#include<algorithm>
#include<cmath>
#include<stdlib.h>
#include<time.h>
using namespace std;
int main()
{
     int t,n,i,j,c,d,k,l,var1,var2 ;
      float a[1005],b[1005];
       scanf("%d",&t);
       for(j = 1 ; j<=t ; j++){
       scanf("%d",&n);
        for(i=0 ; i<n ;i++) {
            scanf("%f",&a[i]);
            }
            for(i=0 ; i<n ;i++)
            {
                 scanf("%f",&b[i]);
            }
             std :: sort(a, a + n);
              std :: sort(b, b + n);
              c = 0;
              k =n-1;
              for(i = n-1 ; i>=0 && k>=0; i--)
              {

                  while(a[i] < b[k]&& k >=0)
                      {
                       k--;
                      // printf("%d   hahaah",k);//var1 =1;
                      }
                   if(k >= 0)
                   c++;
                   k--;
              }
              l =0;
              d=0;
              k = 0;
              for(i = 0 ; i<n && k<n ; i++)
              {
                  //var2=0;
                  while(b[k] < a[i] && k <n)
                  {
                      k++;
                       // var2=1;
                  }
                  if(k!=n)
                  d++;
                  k++;
              }

             printf("Case #%d: %d %d\n",j,c,n-d);



    }
    return 0;
}
