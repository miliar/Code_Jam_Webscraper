#include <iostream>
#include <stdio.h>
#include <string.h>
#include <set>
#include <vector>
using namespace std;
struct node
{
  char st,ed;
  int c;
}w[10];
int n,p[10],ans,cnt;
vector<int> v;
inline int isvalid()
{
  int a=w[v[0]].c,i;
  for (i=1;i<n;i++)
    if (w[v[i]].st==w[v[i-1]].ed) a+=w[v[i]].c-1;
    else a+=w[v[i]].c;
  return a==cnt;
}
void dfs(int d)
{
  if (d==n) {if (isvalid()) ans++;return;}
  for (int i=0;i<n;i++)
  {
    if (!p[i])
    {
      p[i]=1;v.push_back(i);
      dfs(d+1);
      p[i]=0;v.pop_back();
    }
  }
}
int main()
{
  freopen("B-small-attempt3.in","r",stdin);
  freopen("B-small-attempt3.out","w",stdout);
  int t,k,i,j;
  string s;
  cin>>t;
  for (k=1;k<=t;k++)
  {
    cin>>n;
    set<char> cs;
    for (i=0;i<n;i++)
    {
      cin>>s;
      w[i].st=s[0];
      w[i].ed=s[s.size()-1];
      w[i].c=0;
      for (j=0;j<s.size();j++)
        {
          cs.insert(s[j]);
          if (!j) w[i].c++;
          else if (s[j]!=s[j-1]) w[i].c++;
        }
    }
    cnt=cs.size();
    memset(p,0,sizeof(p));
    v.clear();
    ans=0;
    dfs(0);
    cout<<"Case #"<<k<<": "<<ans<<endl;
  }
  return 0;
}
