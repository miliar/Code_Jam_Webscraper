#include<stdio.h>
int main()
{
    freopen("C:\\Users\\Gaurav\\Desktop\\A.in","r",stdin);
    freopen("C:\\Users\\Gaurav\\Desktop\\output.txt","w",stdout);
    int t;
    scanf("%d",&t);
    int ca=0;
    while(t--)
    {
        ca++;
        int arr[17]={0};
        int fr,i,j;
        scanf("%d",&fr);
        for(i=1;i<=4;i++)
        for(j=1;j<=4;j++)
        {
            int a;
            scanf("%d",&a);
            if(i==fr)
            arr[a]++;
        }
        scanf("%d",&fr);
        for(i=1;i<=4;i++)
        for(j=1;j<=4;j++)
        {
            int a;
            scanf("%d",&a);
            if(i==fr)
            arr[a]++;
        }
        int cnt=0,idx=0;
        for(i=1;i<=16;i++)
        if(arr[i]==2)
        {
            cnt++;
            idx=i;
        }
        if(cnt==0)
        printf("Case #%d: Volunteer cheated!\n",ca);
        else if(cnt>1)
        printf("Case #%d: Bad magician!\n",ca);
        else
        printf("Case #%d: %d\n",ca,idx);
    }
    return 0;
}
