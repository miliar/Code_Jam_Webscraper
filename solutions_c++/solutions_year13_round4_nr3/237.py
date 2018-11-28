#include<iostream>
#include<fstream>
#include<cstdio>
#include<vector>
#include<cstring>
#include<queue>
using namespace std;
int l0,l1,t,z,x,n,v;
priority_queue<int> pq;
vector<int> adj[10000];
int e[10000],i[10000],a[10000];
int scan[10000];
int main()
{
  freopen("clarge.in","r",stdin);
  freopen("clarge.out","w",stdout);
  cin>>t;
  for(z=1;z<=t;z++)
  {
    cin>>n;
    memset(e,0,sizeof(e));
    for(l0=1;l0<=n;l0++)
      adj[l0].clear();
    //forward
    for(l0=1;l0<=n;l0++)
    {
      cin>>i[l0];
      for(l1=l0-1;l1>=1;l1--)
        if(i[l1]==i[l0]-1)
        {
          adj[l0].push_back(l1);
          e[l1]++;
          break;
        }
    }
    memset(scan,0,sizeof(scan));
    for(l0=1;l0<=n;l0++)
    {
      if(scan[i[l0]]>0)
      {
        adj[scan[i[l0]]].push_back(l0);
        e[l0]++;
      }
      scan[i[l0]]=l0;
    }
    //reverse
    for(l0=n;l0>=1;l0--)
      cin>>i[l0];
    for(l0=1;l0<=n;l0++)
    {
      for(l1=l0-1;l1>=1;l1--)
        if(i[l1]==i[l0]-1)
        {
          adj[n-l0+1].push_back(n-l1+1);
          e[n-l1+1]++;
          break;
        }
    }
    memset(scan,0,sizeof(scan));
    for(l0=1;l0<=n;l0++)
    {
      if(scan[i[l0]]>0)
      {
        adj[n-scan[i[l0]]+1].push_back(n-l0+1);
        e[n-l0+1]++;
      }
      scan[i[l0]]=l0;
    }
    for(l0=1;l0<=n;l0++)
      if(e[l0]==0)
        pq.push(l0);
    v=n;
    while(!pq.empty())
    {
      x=pq.top();
      pq.pop();
      a[x]=v;
      v--;
      for(l0=0;l0<adj[x].size();l0++)
      {
        e[adj[x][l0]]--;
        if(e[adj[x][l0]]==0)
          pq.push(adj[x][l0]);
      }
    }
    printf("Case #%d: %d",z,a[1]);
    for(l0=2;l0<=n;l0++)
        printf(" %d",a[l0]);
    printf("\n");
  }
  return 0;
}
