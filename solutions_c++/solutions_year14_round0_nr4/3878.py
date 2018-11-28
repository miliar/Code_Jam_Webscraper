#include <stdio.h>
#include <vector>
#include <algorithm>

bool func(const float& a, const float& b)
{
    return (a>b);
}

using namespace std;
 int main()
 {
      int t,n,i,j,count=1;

      scanf("%d",&t);
      while(t--)
      {
          scanf("%d",&n);
          vector <float> naomi(n);
          vector <float> ken(n);

         for(i=0;i<n;i++)
            {scanf("%f",&naomi[i]);}
         for(i=0;i<n;i++)
            scanf("%f",&ken[i]);

        sort(naomi.begin(),naomi.end(),func);
        sort(ken.begin(),ken.end(),func);

        int dw=0,w=0;
        j=0;
        for(i=0;i<n;i++)
        {
            if(naomi[j]>ken[i])
                {
                    dw++;
                    j++;
                }
            //printf("%f %f",ken[i],naom[i]);
        }
        w=0;
        j=0;
        for(i=0;i<n;i++)
        {
           // printf("Pass %d: ",i);

            while(j<n)
              {

               if(func(ken[i],naomi[j]))
                {
                  //  printf("ken- %f  naomi- %f",ken[i],naomi[j]);
                    w++;
                 //   printf("%d\n",j);
                    j++;
                    goto out;
                }
                else
                    j++;

              }
                out:;

        }
        printf("Case #%d: %d %d\n",count,dw,n-w);
        count++;
      }
 }
