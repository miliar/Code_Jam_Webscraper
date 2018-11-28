#include <stdio.h>
#include <set>
#include <algorithm>
#include <cstring>

const int MAXN=1000;
int uN,vN;  //u,v数目
int g[MAXN][MAXN];//编号是0~n-1的 
int linker[MAXN];
bool used[MAXN];
bool dfs(int u)
{
  int v;
  for(v=0;v<vN;v++)
    if(g[u][v]&&!used[v])
    {
      used[v]=true;
      if(linker[v]==-1||dfs(linker[v]))
      {
        linker[v]=u;
        return true;
      }    
    }  
  return false;  
}    
int hungary()
{
  int res=0;
  int u;
  memset(linker,-1,sizeof(linker));
  for(u=0;u<uN;u++)
  {
    memset(used,0,sizeof(used));
    if(dfs(u))  res++;
  } 
  return res;   
}     

int main() {
  int T;scanf("%d",&T);
  for (int cas = 1;cas <= T;cas++) {
    int n;scanf("%d",&n);
    double a[1000],b[1000];
    for (int i = 0;i < n;i++)
      scanf("%lf",&a[i]);
    for (int i = 0;i < n;i++) 
      scanf("%lf",&b[i]);
    for (int i = 0;i < n;i++)
      for (int j = 0;j < n;j++)
        g[i][j] = a[i] > b[j];
    uN = vN = n;
    std::set<double> st;
    int res = 0;
    for (int i = 0;i < n;i++) {
      st.insert(b[i]);
    }
    for (int i = 0;i < n;i++) {
      std::set<double>::iterator it = st.lower_bound(a[i]);
      if (it == st.end()) {
        res += 1;
        st.erase(st.begin());
      } else {
        st.erase(it);
      }
    }
    printf("Case #%d: %d %d\n",cas,hungary(),res);
    
  }
  return 0;
}
