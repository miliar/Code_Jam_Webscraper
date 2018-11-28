#include <cmath>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <map>
#include <vector>
#include <string>
using namespace std;
map<string,int> eng,fra;
vector <string> a[50];
int ans=1000000,tmp;
string s;
int n;
void dfs(int x)
{
  if (tmp>ans) return ;
  if (x>n) {ans=min(ans,tmp);return ;}
  if (x!=2){
  for (int i=0;i<a[x].size();i++)
  {
    if (eng[a[x][i]]==0&&fra[a[x][i]]) tmp++;
    eng[a[x][i]]++;
  }
  dfs(x+1);
  for (int i=0;i<a[x].size();i++)
  {
    if (eng[a[x][i]]==1&&fra[a[x][i]]) tmp--;
    eng[a[x][i]]--;
  }
  }
  if (x!=1){
  for (int i=0;i<a[x].size();i++)
  {
    if (fra[a[x][i]]==0&&eng[a[x][i]]) tmp++;
    fra[a[x][i]]++;
  }
  dfs(x+1);
  for (int i=0;i<a[x].size();i++)
  {
    if (fra[a[x][i]]==1&&eng[a[x][i]]) tmp--;
    fra[a[x][i]]--;
  }
  }
}
int main()
{
  freopen("in.txt","r",stdin);
  freopen("out.txt","w",stdout);
  int T,ca=0,m;
  scanf("%d",&T);
  while(T--)
  {
    eng.clear();
    fra.clear();
    scanf("%d",&n);
    for (int i=1;i<=n;i++)
      {
        a[i].clear();
        while(1){
          cin>>s;
          a[i].push_back(s);
          char c=getchar();
          if (c=='\n') break;
        }
      }
    tmp=0;ans=1000000;
    dfs(1);
    printf("Case #%d: %d\n",++ca,ans );
  }
}