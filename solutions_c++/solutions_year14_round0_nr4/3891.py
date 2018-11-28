#include <iostream>

using namespace std;

int main()
{
    int tc,n,i,t,war,dwar,j;
    double arr[1001],brr[1001];
    //freopen("input.txt","r",stdin);
    //freopen("out.txt","w",stdout);
    scanf("%d",&tc);
    for(t=1;t<=tc;t++)
    {
        war=0;
        dwar=0;
        scanf("%d",&n);
        for(i=0;i<n;i++)
        {
            scanf("%lf",&arr[i]);
        }
        for(i=0;i<n;i++)
        {
            scanf("%lf",&brr[i]);
        }
        if(n==1)
        {
            if(arr[0]>brr[0])
            {
                printf("Case #%d: 1 1\n",t);
            }
            else
            {
                printf("Case #%d: 0 0\n",t);
            }
            continue;
        }
        sort(arr,arr+n);
        sort(brr,brr+n);
       /* for(i=0;i<n;i++)
        {
            printf("%lf %lf\n",arr[i],brr[i]);
        }*/
        j=n-1;
        for(i=n-1;i>=0;i--)
        {
            if((arr[i]<brr[0])||(j<0))
                break;
            if(arr[i]>brr[j])
                dwar++;
            else
            {
                 while (brr[j]>arr[i])
                 {
                     j--;
                     if(j<0)
                        break;
                 }
                 if(j>=0)
                    dwar++;
            }
            j--;
        }
        for(i=n-1;i>=0;i--)
        {
            for(j=n-1;j>=0;j--)
            {
                 if(brr[i]>arr[j])
                 {
                     war++;
                     arr[j]=100.0;
                     break;
                 }
            }
        }
        printf("Case #%d: %d %d\n",t,dwar,n-war);
    }
    return 0;
}

