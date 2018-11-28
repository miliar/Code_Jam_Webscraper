#include<iostream>
using namespace std;
int main()
{
    freopen("2.in","r",stdin);
    freopen("2.out","w",stdout);
    int C,a[100][100],x[100],y[100];
    cin>>C;
    for (int T=1;T<=C;++T)
    {
        int n,m;
        scanf("%d%d",&n,&m);
        for (int i=0;i<n;++i)
          for (int j=0;j<m;++j)
            scanf("%d",&a[i][j]);
        memset(x,0,sizeof(x));
        memset(y,0,sizeof(y));
        for (int i=0;i<n;++i)
          for (int j=0;j<m;++j)
            {
              x[i]>?=a[i][j];
              y[j]>?=a[i][j];
            }
        bool flag=1;
        for (int i=0;i<n;++i)
         if (flag)
          for (int j=0;j<m;++j)
            if (a[i][j]!=x[i]&&a[i][j]!=y[j]) {flag=0;break;}
        if (flag)
          printf("Case #%d: YES\n",T);
        else printf("Case #%d: NO\n",T);
    }
    return 0;
}
