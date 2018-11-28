#include <bits/stdc++.h>

#define rep(i,n) for(i=0;i<n;i++)
#define ll long long 
#define elif else if
#define pii pair<ll int,ll int>
#define mp make_pair
#define pb push_back
using namespace std;

int foo(vector<int>v,int val)
{
  int i,ans=0;
  for(i=0;i<v.size();i++)
  {
    
  }
}
int main()
{
  freopen("int","r",stdin);
  freopen("out","w",stdout);
	int T,t;
	cin>>T;
	for (t=1;t<=T;t++)
	{
    int i,j,k,n,l,r,mid=0,x=0,sum=0;
    cin>>n;
    vector<int>vv(n);
    rep(i,n)
    {
      cin>>vv[i];
     
    }

    int ans=99999999,tem;
  
    for(i=0;i<n-1;i++)
    {
      if(vv[i]>vv[i+1])
        x+= (vv[i]-vv[i+1]);
      
    }
    //cout<<mid<<" ";

    for(mid=0;mid<=10000;mid++)
    {
      vector<int>v(vv);
      sum=0;
      rep(i,n-1)
      {
        int eat;
        if(v[i]-mid >v[i+1])
          break;
        eat=min(v[i],mid);
        //eat= min(eat,max(v[i]-v[i+1],0));
         sum+=eat;
        }
        if(i<n-1)continue;
       // if(sum==85)cout<<mid<<"\n";
        //if(mid==0)cout<<sum<<"\n";
     ans=min(ans,sum);
       
    }
    printf("Case #%d: %d %d\n",t,x,ans);
	}
	return 0;
}