#include <iostream>
#include <cstdio>
using namespace std;
int n,m;
int s[102][102];
int line[102];
int row[102];

int get_line(int x)
{
    int line_max=-1;
    for(int j=1;j<=m;j++)
    {
        line_max=max(line_max,s[x][j]);
    }
    return line_max;
}
int get_row(int x)
{
    int row_max=-1;
    for(int i=1;i<=n;i++)
    {
        row_max=max(row_max,s[i][x]);
    }
    return row_max;
}

int main()
{
  // freopen("in.txt","r",stdin);
   // freopen("out.txt","w",stdout);
    int num=1;
    int cas;
    cin >> cas;
    while(cas--)
    {
        cin >> n >> m;
        for(int i=1;i<=n;i++)
        {
            for(int j=1;j<=m;j++)
            {
                cin >> s[i][j];
            }
        }
        for(int i=1;i<=n;i++)
        {
            line[i]=get_line(i);
        }
        for(int j=1;j<=m;j++)
        {
            row[j]=get_row(j);
        }
        int flag=0;
        for(int i=1;i<=n;i++)
        {
            for(int j=1;j<=m;j++)
            {
                if(s[i][j]<line[i] && s[i][j]<row[j])
                {
                    printf("Case #%d: NO\n",num++);
                    flag=1;
                    break;
                }
            }
            if(flag==1)break;
        }
        if(flag==0)
        printf("Case #%d: YES\n",num++);
    }
    return 0;
}
