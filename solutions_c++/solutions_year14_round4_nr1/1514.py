#include<cstdio>
#include<algorithm>
using namespace std;
int main()
{
    int t,x,n,j,k,count;
    int arr[20000];
    scanf("%d",&t);
    for(int i=1;i<=t;i++)
    {
        scanf("%d%d",&n,&x);
        for(j=0;j<n;j++)
        {
            scanf("%d",&arr[j]);
        }
        sort(&arr[0],&arr[n]);
        j=0;
        k=n-1;
        count=0;
        while(j<k)
        {
            if(arr[j]+arr[k]<=x)
            {
                count++;
                j++;
                k--;
            }
            else
            {
                while(j<k&&arr[j]+arr[k]>x)
                {
                    count++;
                    k--;
                }
            }
        }
        if(j==k)
        {
            count++;
        }
        printf("Case #%d: %d\n",i,count);
    }
    return 0;
}
