#include<iostream>
#include<cstdio>
#include<string>
using namespace std;
int arr[110][110],temp[110][110],n,m;

inline int chkrow(int i)
{
    for(int j=0;j<m;j++)
        if(arr[i][j]!=arr[i][0])
            return 0;
    return 1;
}
inline int chkcol(int j)
{
    for(int i=0;i<n;i++)
        if(arr[i][j]!=arr[0][j])
            return 0;
    return 1;
}
int main()
{
    freopen("2.txt","r",stdin);
    freopen("a2.txt","w",stdout);
    int tc,flag,c;
    scanf("%d",&tc);
    for(int t=1;t<=tc;t++)
    {
        flag=1;
        scanf("%d%d",&n,&m);
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<m;j++)
                scanf("%d",&arr[i][j]);
        }
        int max=arr[0][0];
        for(int i=0;i<n;i++)
            for(int j=0;j<m;j++)
                 if(arr[i][j]>max) max=arr[i][j];
        for(int i=0;i<n;i++)
            for(int j=0;j<m;j++)
                  temp[i][j]=max;
        for(int i=0;i<n;i++)
            if(chkrow(i)==1) {
              for(int j=0;j<m;j++)
                   temp[i][j]=arr[i][0];
              }
         for(int j=0;j<m;j++)
            if(chkcol(j)==1) {
              for(int i=0;i<n;i++)
                   temp[i][j]=arr[0][j];
              }
        for(int i=0;i<n;i++)
           for(int j=0;j<m;j++)
               if(arr[i][j]!=temp[i][j])
                {
                    flag=0;break;
                }
    if(flag==1)
        printf("Case #%d: YES\n",t);
    else
        printf("Case #%d: NO\n",t);

    }

}

