#include <iostream>

using namespace std;

int main()
{
    int tc,a1,a2,arr[4][4],brr[4][4],t,cnt=0,val,i,j;
    freopen("input.txt","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&tc);
    for(t=1;t<=tc;t++)
    {
        cnt=0;
        val=0;
        scanf("%d",&a1);
        a1--;
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                scanf("%d",&arr[i][j]);
            }
        }
        scanf("%d",&a2);
        a2--;
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                scanf("%d",&brr[i][j]);
            }
        }
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                if(arr[a1][i]==brr[a2][j])
                {
                    cnt++;
                    val=arr[a1][i];
                }
            }
        }
        if(cnt==0)
            printf("Case #%d: Volunteer cheated!\n",t);
        if(cnt==1)
            printf("Case #%d: %d\n",t,val);
        if(cnt>1)
            printf("Case #%d: Bad magician!\n",t);
    }
    return 0;
}
