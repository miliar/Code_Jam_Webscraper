#include<cstdio>
#include<cstdlib>

int main()
{
    int cnt=0,t=0,i=0,j=0,k=0,n=0,m=0,ans=0;
    int arr[4][4],ar[4][4];
    scanf("%d",&k);
    for(t=0;t<k;t++)
    {
        cnt=0;
        scanf("%d",&n);
        for(i=0;i<4;i++)
            for(j=0;j<4;j++)
                scanf("%d",&arr[i][j]);
        scanf("%d",&m);
        for(i=0;i<4;i++)
            for(j=0;j<4;j++)
                scanf("%d",&ar[i][j]);
        for(i=0;i<4;i++){
            for(j=0;j<4;j++){
                if(ar[m-1][i]==arr[n-1][j])
                {
                    cnt++;
                    ans=ar[m-1][i];
                }}}
        if(cnt==0)
            printf("Case #%d: Volunteer cheated!\n",t+1);
        else if(cnt==1)
            printf("Case #%d: %d\n",t+1,ans);
        else
        {
            printf("Case #%d: Bad magician!\n",t+1);
        }
    }
    return 0;
}
