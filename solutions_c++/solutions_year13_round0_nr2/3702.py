#include<iostream>
#include<cstdio>
#include<algorithm>
using namespace std;
int main()
{
    int t,y=1;
    cin>>t;
    while(t--)
    {
        int n,m;
        cin>>n>>m;
        int a[101][101],mark[101][101],row_max[101],row_min[101],col_max[101],col_min[101],i,j,k;
        for(i=1;i<=n;i++)
        {
            row_max[i]=-1;
            row_min[i]=1000;
            for(j=1;j<=m;j++)
            {
                cin>>a[i][j];mark[i][j]=0;
                row_max[i]=max(row_max[i],a[i][j]);
                row_min[i]=min(row_min[i],a[i][j]);
            }
        }
        for(i=1;i<=m;i++)
        {
            col_max[i]=-1;
            col_min[i]=1000;
            for(j=1;j<=n;j++)
            {
                col_max[i]=max(col_max[i],a[j][i]);
                col_min[i]=min(col_min[i],a[j][i]);
            }
        }
        int marked=0;
        for(i=1;i<=n;i++)
        {
            for(j=1;j<=m;j++)
            {
                if(mark[i][j]==0)
                {
                    if(row_max[i]==row_min[i])
                    {
                            mark[i][j]=1;marked++;
                    }
                    else if(col_max[j]==col_min[j])
                    {
                            mark[i][j]=1;marked++;
                    }
                    else
                    {
                            if(a[i][j]==row_max[i])
                            {mark[i][j]=1;marked++;}
                            else if(a[i][j]==col_max[j])
                            {mark[i][j]=1;marked++;}
                    }
                }
            }
        }
        if(marked==(n*m))cout<<"Case #"<<y<<": YES\n";
        else cout<<"Case #"<<y<<": NO\n";y++;
    }
    return 0;
}
