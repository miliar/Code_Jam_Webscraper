#include <iostream>
using namespace std;

int map[105][105];
int a,b,i,j,k,t;

int main()
{
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    scanf("%d",&t);
    int t1 = 0;
    while (t--)
    {     
          scanf("%d %d",&a,&b);
          for (i = 0;i<a;i++)
              for (j = 0;j<b;j++)
              {
                  scanf("%d",&map[i][j]);
              }
          ++t1;
          bool ff=true;
          for (i=0;i<a;++i)
              for (j=0;j<b;++j)
              {
                  bool f=true;
                  for (k = 0;k<a;++k)
                      if (map[k][j]>map[i][j]) {f=false;break;}
                  if (f) continue;
                  f=true;
                  for (k = 0;k<b;++k)
                      if (map[i][k]>map[i][j]) {f=false;break;}
                  if (!f) {ff=false;break;}   
              }
          if (!ff) printf("Case #%d: NO\n",t1);
          else printf("Case #%d: YES\n",t1);
    }
    return 0;
}
