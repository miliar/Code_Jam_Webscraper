#include<cstdio>
#include<iostream>
#include<fstream>
#include<queue>
#include<cstring>
#include<vector>
using namespace std;
struct node
{
  string s;
  bool operator<(const node &n)const
  {
    return s>n.s;
  }
};
priority_queue<node> pq;
string l[201],s,z;
int k,n,x,l0,l1,l2,y,t;
bool v[3000000];
int start[201],cur[201];
vector<int> a[201];
int type[201];
int mask;
int main()
{
  freopen("dsmall0.in","r",stdin);
  freopen("t0.out","w",stdout);
  scanf("%d",&t);
  for(l0=1;l0<=t;l0++)
  {
    memset(v,0,sizeof(v));
    memset(start,0,sizeof(start));
    scanf("%d%d",&k,&n);
    for(l1=1;l1<=k;l1++)
    {
      scanf("%d",&x);
      start[x]++;
    }
    for(l1=1;l1<=n;l1++)
    {
      scanf("%d%d",&type[l1],&x);
      a[l1].clear();
      l[l1]="!";
      while(x--)
      {
        scanf("%d",&y);
        a[l1].push_back(y);
      }
    }
    while(!pq.empty())
      pq.pop();
    pq.push((node){""});
    v[0]=1;
    while(!pq.empty())
    {
      s=pq.top().s;
      pq.pop();
      mask=0;
      memcpy(cur,start,sizeof(start));
      for(l1=0;l1<s.size();l1++)
      {
        x=(int)(s[l1]);
        mask+=(1<<(x-1));
        cur[type[x]]--;
        for(l2=0;l2<a[x].size();l2++)
          cur[a[x][l2]]++;
      }
      if(l[s.size()]=="!")
      {
        l[s.size()]=s;
        if(s.size()==n)
          break;
      }
      for(l1=1;l1<=n;l1++)
        if(((1<<(l1-1))&mask)==0&&cur[type[l1]]>0&&!v[mask+(1<<(l1-1))])
        {
          v[mask+(1<<(l1-1))]=1;
          z=" ";
          z[0]=l1;
          pq.push((node){s+z});
        }
    }
    cout<<"Case #"<<l0<<": ";
    if(l[n]=="!")
      cout<<"IMPOSSIBLE";
    else
      for(l1=0;l1<n;l1++)
      {
        cout<<((int)l[n][l1]);
        if(l1<n-1)
          cout<<" ";
      }
    cout<<endl;
  }
  fclose(stdin);
  fclose(stdout);
  return 0;
}
