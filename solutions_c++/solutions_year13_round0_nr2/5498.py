#include<stdio.h>
int main()
{
    int t,n,m,i,j,arr[11][11];
    scanf("%d",&t);
    for(int r=1;r<=t;r++)
    {
        int flag=0;
        int result=1;
        scanf("%d%d",&n,&m);
        for(i=0;i<n;i++)
            for(j=0;j<m;j++)
                scanf("%d",&arr[i][j]);
        for(int i=0;i<n;i++)
        {
            int max=0;
            for(int j=0;j<m;j++)
            {
                if(arr[i][j]>max)
                    max=arr[i][j];
            }
            for(int j=0;j<m;j++)
            {
                if(arr[i][j]!=max)
                {
                    for(int k=0;k<n;k++)
                    {
                        if(arr[k][j]!=arr[i][j])
                            result=0;
                    }
                }
            }
        }
        if(result==0) printf("Case #%d: NO\n",r);
        else printf("Case #%d: YES\n",r);
    }
    return 0;
}
