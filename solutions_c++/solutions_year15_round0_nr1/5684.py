#include<stdio.h>
#include<stdlib.h>
main()
{
    int ttt;
    scanf("%d",&ttt);
    for(int tttt=0;tttt<ttt;tttt++)
    {
        printf("Case #%d: ",tttt+1);
        int n;
        scanf("%d",&n);
        char arr[n+1];
        scanf("%s",arr);
        int cnt=0;
        for(int i=0;i<=n;i++)arr[i]-='0';
        //if(arr[0]==0)cnt++;
        int sum=arr[0];
        for(int i=1;i<=n;i++)
        {
            //printf("%d ",arr[i]);
            if(i>sum&&arr[i]!=0)
            {
               int tmp=i-sum;
               sum+=tmp;
               cnt+=tmp;
            }
            sum+=arr[i];
        }
        printf("%d",cnt);
        printf("\n");
    }
}
