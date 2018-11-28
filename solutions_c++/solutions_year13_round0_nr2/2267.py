#include<cstdio>
#include<algorithm>
using namespace std;
int tab[105][105];
int kol[105],wier[105];

int solve()
{
  int n,m;
  scanf("%d%d",&n,&m);
  for(int i=0;i<n;i++)
    for(int j=0;j<m;j++)scanf("%d",&tab[i][j]);
  for(int i=0;i<n;i++)
  {
    wier[i]=0;
    for(int j=0;j<m;j++)wier[i]=max(wier[i],tab[i][j]);
  }
  
  for(int i=0;i<m;i++)
  {
    kol[i]=0;
    for(int j=0;j<n;j++)kol[i]=max(kol[i],tab[j][i]);
  }
  //for(int i=0;i<n;i++)printf("%d ",wier[i]);printf("\n");
  //for(int i=0;i<m;i++)printf("%d ",kol[i]);printf("\n");
  for(int i=0;i<n;i++)
    for(int j=0;j<m;j++)if(tab[i][j]!=min(wier[i],kol[j]))return 1;
  return 0;
}
int main()
{
    int t;
    scanf("%d",&t);
    for(int i=0;i<t;i++)
    {
        int k=solve();
        switch(k)
        {
            case 0:
            printf("Case #%d: YES\n",i+1);break;
            case 1:
            printf("Case #%d: NO\n",i+1);break;
        }
    }
    return 0;
}
