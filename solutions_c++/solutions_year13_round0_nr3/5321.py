#include<stdio.h>
int main()
{
        int test,a,b,ans,K=1,i;
        int arr[]={0,1,4,9,121,484,10201};
        scanf("%d",&test);
        while(test--)
        {
                ans=0;
                scanf("%d %d",&a,&b);
                for(i=0;i<=6;i++)
                {
                        if(arr[i]>=a&&arr[i]<=b)
                                ans++;
                }
                printf("Case #%d: %d\n",K,ans);
                K++;
        }
        return 0;
}
