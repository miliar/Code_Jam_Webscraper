#include<bits/stdc++.h>
#define X first
#define Y second

using namespace std;

typedef pair<int,int> pii;

const int maxn=1e6;
vector<int>G[60];
vector<pii>vec;
int n,t[2],ans,dp[maxn],javab[maxn];
bool dp1[maxn],mark[60];

void dfs(int v,int ind)
{
  t[ind]++;
  mark[v]=true;
  for(int i=0;i<G[v].size();i++)
    {
      int u=G[v][i];
      if(!mark[u])
	dfs(u,1-ind);
    }
}

int main()
{
  int qw;
  cin>>qw;
  for(int q=1;q<=qw;q++)
    {
      cin>>n;
      ans=0;vec.clear();
      for(int i=0;i<50;i++)
	G[i].clear(),mark[i]=false;
      for(int i=0;i<n;i++)
	for(int j=0;j<n;j++)
	  {
	    char c;
	    cin>>c;
	    if(c=='1')
	      ans--,G[i].push_back(j+n),G[j+n].push_back(i);
	  }
      for(int i=0;i<2*n;i++)
	if(!mark[i])
	  {
	    t[0]=t[1]=0;
	    dfs(i,i/n);
	    if(t[0]==t[1])
	      ans+=t[0]*t[1];
	    else
	      vec.push_back(pii(t[0],t[1]));
	  }
      memset(dp1,false,sizeof dp1);
      memset(dp,63,sizeof dp);
      memset(javab,0,sizeof javab);
      n=vec.size();
      //  cout<<ans<<" "<<n<<endl;
      for(int i=0;i<(1<<n);i++)
	{
	  int sum=0,sum1=0;
	  for(int j=0;j<n;j++)
	    if(i&(1<<j))
	      sum+=vec[j].X-vec[j].Y,sum1+=vec[j].X;
	  if(sum==0) dp1[i]=true,javab[i]=sum1*sum1;
	}
      dp[0]=0;
      for(int i=1;i<(1<<n);i++)
	if(dp1[i])
	  for(int mask=i;mask>0;mask=(mask-1)&i)
	    if(dp1[mask])
	      dp[i]=min(dp[i],dp[i-mask]+javab[mask]);
      cout<<"Case #"<<q<<": "<<ans+dp[(1<<n)-1]<<endl;
    }
}
