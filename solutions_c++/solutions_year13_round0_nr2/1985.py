#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>

using namespace std;

int n,m;
int a[105][105];

bool check(int x,int y)
{
    int tmp=a[x][y];
    int flg1=1,flg2=1;
    for(int i=1;i<=n;i++)
    {
        if(a[i][y]>tmp)
        {
            flg1=0;
            break;
        }
    }
    for(int i=1;i<=m;i++)
    {
        if(a[x][i]>tmp)
        {
            flg2=0;
            break;
        }
    }
    //cout<<flg1<<" "<<flg2<<endl;
    if(0==flg1 && 0==flg2)return true;
    return false;
}

int main()
{
    //freopen("B-large.in","r",stdin);
    //freopen("B.out.txt","w",stdout);
    int t;
    cin>>t;
    for(int ii=1;ii<=t;ii++)
    {
        cin>>n>>m;
        for(int i=1;i<=n;i++)
          for(int j=1;j<=m;j++)
          {
              cin>>a[i][j];
          }
        int flag=0;
        for(int i=1;i<=n;i++)
        {
          if(flag)break;
          for(int j=1;j<=m;j++)
          {
              //cout<<"check "<<i<<" "<<j<<endl;
              if(check(i,j))
              {
                  flag=1;
                  break;
              }
          }
        }
        cout<<"Case #"<<ii<<": ";
        if(flag)
        {
            printf("NO\n");
        }
        else
        {
            printf("YES\n");
        }
    }
    return 0;
}
