#include<cstdio>
#include<algorithm>
using namespace std;
double a[1001],b[1001];
int n,cnt=0,X=0;
int main()
{ int t,i,j;
    scanf("%d",&t);
    while(t--)
    {X++;
        cnt=0;
        scanf("%d",&n);
        for(i=0;i<n;i++)
        {
            scanf("%lf",&a[i]);
        }
        for(i=0;i<n;i++)
            scanf("%lf",&b[i]);
        std::sort(a,a+n);
        std::sort(b,b+n);
        if(a[n-1]<b[0]){printf("Case #%d: 0 0\n",X);
        continue;
        }
        if(b[n-1]<a[0]){printf("Case #%d: %d %d\n",X,n,n);
        continue;}
        for(i=0,j=0;i<n;)
        {
            if(a[i]>b[j])
            {
                cnt++;
                i++;
                j++;
            }
            else
            {
                i++;
            }

        }
        printf("Case #%d: %d ",X,cnt);

       for(i=0,j=0;i<n && j<n;)
       {
           while(b[j]<a[i] && j<n)
           {
               j++;
           }
           if(j<n)
           {i++;
           j++;
           }
        }


        printf("%d\n",n-i);
    }
return 0;
}
