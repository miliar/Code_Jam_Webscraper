//program C

#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
#include<cmath>
#include<vector>
#include<set>
#include<queue>
#include<bitset>
#include<ctime>

using namespace std;

int get()
{
  char c;
  while(c=getchar(),(c<'0'||c>'9')&&(c!='-'));
  bool flag=(c=='-');
  if(flag)
    c=getchar();
  int x=0;
  while(c>='0'&&c<='9')
    {
      x=x*10+c-48;
      c=getchar();
    }
  return flag?-x:x;
}

void output(int x)
{
  if(x<0)
    {
      putchar('-');
      x=-x;
    }
  int len=0,data[10];
  while(x)
    {
      data[len++]=x%10;
      x/=10;
    }
  if(!len)
    data[len++]=0;
  while(len--)
    putchar(data[len]+48);
  putchar('\n');
}

struct edge
{
  int data,weight,next;
};

const int maxv=100000;
const int maxe=700000;
const int inf=1000000000;

int counter;
string data[10000];
vector<string> sen[200];
vector<int> list[200];
int g[maxv];
edge e[maxe];

void add(int x,int y,int w)
{
  //cout<<x<<' '<<y<<' '<<w<<endl;
  e[counter*2]=(edge){y,w,g[x]};
  g[x]=counter*2;
  e[counter*2+1]=(edge){x,0,g[y]};
  g[y]=counter*2+1;
  counter++;
}

int SAP(int s,int t,int n)
{
  static int dist[maxv],cnt[maxv],start[maxv],pre[maxv];
  memset(dist,0,sizeof(dist));
  memset(cnt,0,sizeof(cnt));
  cnt[0]=n;
  for(int i=0;i<n;i++)
    start[i]=g[i];
  int ans=0,flow=inf,v=s;
  while(dist[s]<n)
    {
      int p=start[v];
      while(p!=-1)
	{
	  if(e[p].weight&&dist[v]==dist[e[p].data]+1)
	    break;
	  p=e[p].next;
	}
      if(p!=-1)
	{
	  start[v]=p;
	  v=e[p].data;
	  pre[v]=p;
	  flow=min(flow,e[p].weight);
	  if(v==t)
	    {
	      ans+=flow;
	      while(v!=s)
		{
		  e[pre[v]].weight-=flow;
		  e[pre[v]^1].weight+=flow;
		  v=e[pre[v]^1].data;
		}
	      flow=inf;
	    }
	}
      else
	{
	  int p=g[v],mind=n;
	  while(p!=-1)
	    {
	      if(e[p].weight&&dist[e[p].data]+1<mind)
		{
		  mind=dist[e[p].data]+1;
		  start[v]=p;
		}
	      p=e[p].next;
	    }
	  if(!--cnt[dist[v]])
	    break;
	  cnt[dist[v]=mind]++;
	  if(v!=s)
	    v=e[pre[v]^1].data;
	}
    }
  return ans;
}

int main()
{
  int totaltest=get();
  for(int test=1;test<=totaltest;test++)
    {
      int n=get(),total=0;
      for(int i=0;i<n;i++)
	{
	  char c;
	  while(c=getchar(),c<'a'||c>'z');
	  sen[i].clear();
	  while(true)
	    {
	      string s="";
	      while(c>='a'&&c<='z')
		{
		  s+=c;
		  c=getchar();
		}
	      sen[i].push_back(s);
	      data[total++]=s;
	      if(c=='\n')
		break;
	      while((c<'a'||c>'z')&&c!=-1)
		c=getchar();
	    }
	}
      sort(data,data+total);
      int m=unique(data,data+total)-data;
      for(int i=0;i<n;i++)
	{
	  list[i].clear();
	  for(int j=0;j<sen[i].size();j++)
	    list[i].push_back(lower_bound(data,data+m,sen[i][j])-data);
	}
      int s=0,t=1;
      counter=0;
      memset(g,-1,sizeof(g));
      for(int i=2;i<n;i++)
	{
	  add(s,i,100000);
	  add(i,t,100000);
	}
      for(int i=0;i<m;i++)
	add(n+i,n+m+i,1);
      for(int i=0;i<n;i++)
	for(int j=0;j<list[i].size();j++)
	  {
	    add(i,n+list[i][j],inf);
	    add(n+m+list[i][j],i,inf);
	  }
      printf("Case #%d: %d\n",test,SAP(s,t,n+m*2)-(n-2)*100000);
    }
  return 0;
}
