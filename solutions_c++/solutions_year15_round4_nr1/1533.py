#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;
char arr[110][110];
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int T;
    int ans;
    int n,m;
    cin>>T;
    for(int t=1;t<=T;t++)
    {
        printf("Case #%d: ",t);
        memset(arr,'.',sizeof(arr));
        cin>>n>>m;
        for(int i=0;i<n;i++)
        {
                scanf("%s",arr[i]);
        }
        ans=0;
        for(int i=0;i<n;i++)
        {
            if(ans==-1)
                break;
            for(int j=0;j<m;j++)
            {
                if(arr[i][j]!='.')
                {
                    int s=0;
                    bool change=false;
                    int k;
                    for(k=0;k<j;k++)
                    {
                        if(arr[i][k]!='.')
                        {
                            break;
                        }
                    }
                    if(k==j)
                        {
                            s++;
                            if(arr[i][j]=='<')
                                change=true;
                        }
                    for(k=j+1;k<m;k++)
                    {
                        if(arr[i][k]!='.')
                            break;
                    }
                    if(k>=m)
                        {
                            s++;
                            if(arr[i][j]=='>')
                                change=true;
                        }
                    for(k=0;k<i;k++)
                    {
                        if(arr[k][j]!='.')
                            break;
                    }
                    if(k==i)
                    {
                        s++;
                        if(arr[i][j]=='^')
                            change=true;
                    }
                    for(k=i+1;k<n;k++)
                    {
                        if(arr[k][j]!='.')
                            break;
                    }
                    if(k>=n)
                    {
                        s++;
                        if(arr[i][j]=='v')
                            change=true;
                    }
                    if(s==4)
                    {
                        ans=-1;
                        break;
                    }
                    if(change)
                        ans++;
                }
            }
        }
        if(ans==-1)
            printf("IMPOSSIBLE\n");
        else
            printf("%d\n",ans);
    }
    return 0;
}
