#include<iostream>
#include<stdio.h>
#include<climits>
#include<cstring>
#include<math.h>
#include<algorithm>
#include<map>

using namespace std;

int main()
{
    int t,n,m,flag;
    int arr[105][105],row[105],col[105];
    scanf("%d",&t);
    for(int i=1;i<=t;i++)
    {
        flag=0;
        for(int j=1;j<=n;j++)
            row[j]=0;
        for(int j=1;j<=m;j++)
            col[j]=0;
        scanf("%d %d",&n,&m);
        for(int j=1;j<=n;j++)
        {
            for(int k=1;k<=m;k++)
            {
                scanf("%d",&arr[j][k]);
                if(arr[j][k]>row[j])
                    row[j]=arr[j][k];
                 if(arr[j][k]>col[k])
                    col[k]=arr[j][k];
            }
        }
        for(int j=1;j<=n;j++)
        {
            if(flag==1)
                break;
            for(int k=1;k<=m;k++)
            {
                if((arr[j][k]!=row[j])&&(arr[j][k]!=col[k]))
                {
                    flag=1;
                    break;
                }
            }
        }
        if(!flag)
            printf("Case #%d: YES\n",i);
        else
            printf("Case #%d: NO\n",i);
    }
    return 0;
}
