#include <vector>
#include <cstdio>

using namespace std;

typedef vector<int> vi;
typedef vector<vector<int> > vvi;

vvi g(10, vi(10, 0));
int n,m;

int validate()
{
  int i,j,k;
  bool r,c;
  for(i=0;i<n;i++){
    for(j=0;j<m;j++){
      if(g[i][j]==2)continue;
      c=r=true;
      for(k=0;k<m;k++)if(g[i][k]!=1){r=false; break;}
      for(k=0;k<n;k++)if(g[k][j]!=1){c=false;break;}
      if(!c and !r) return false;
    }
  }
  return true;
}

int main()
{
  int i,j,k,t,c=1;

  scanf("%d", &t);

  while(t--){
    scanf("%d %d", &n, &m);

    for(i=0;i<n;i++)for(j=0;j<m;j++)scanf("%d", &g[i][j]);
    if(validate())printf("Case #%d: YES\n", c++);
    else printf("Case #%d: NO\n", c++);

  }

  return 0;
}
