#include <iostream>
#include <stdio.h>
using namespace std;
int data[100][100];
int row[100];
int col[100];
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int cas;
    scanf("%d",&cas);
    for(int ci=1;ci<=cas;ci++)
    {
        int n,m;
        scanf("%d%d",&n,&m);
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<m;j++)
            {
                scanf("%d",&data[i][j]);
            }
        }
        for(int i=0;i<n;i++)
        {
            row[i]=data[i][0];
            for(int j=1;j<m;j++)
            {
                if(data[i][j]>row[i]) row[i]=data[i][j];
            }
        }
        for(int i=0;i<m;i++)
        {
            col[i]=data[0][i];
            for(int j=1;j<n;j++)
            {
                if(data[j][i]>col[i]) col[i]=data[j][i];
            }
        }
        bool ans=true;
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<m;j++)
            {
                if(row[i]>data[i][j] && col[j]>data[i][j])
                {
                    ans= false;
                    break;
                }
            }
        }
        printf("Case #%d: ",ci);
        if(ans) printf("YES\n");
        else printf("NO\n");
    }
}
