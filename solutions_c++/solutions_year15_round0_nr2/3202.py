#include<bits/stdc++.h>
#define s(n) scanf("%d",&n)
#define sl(n) scanf("%lld",&n)
#define p(n) printf("%d\n",n)
#define ll long long
#define pb push_back
#define mp make_pair
#define mod1 1000000007
#define NN 100000
#define LN 21
using namespace std;
pair<int,int>va[1002];
int fin[1002];
int calc(priority_queue<int>pq,int ste)
{
 int val=pq.top();
 if(val<=3)
 return val+ste;
 else
 {
  pq.pop();
  pq.push(val/2);
  pq.push(val-val/2);
  int v1=calc(pq,ste+1);
  pq.pop();
  pq.pop();
  pq.push(val/2-1);
  pq.push(val-val/2+1);
  v1=min(v1,calc(pq,ste+1));
  return min(val+ste,v1);
 }
}
void preprocess()
{
 int i,j;
 priority_queue<int>pq;
 fin[1]=1;
 fin[2]=2;
 fin[3]=3;
 for(i=4;i<=20;++i)
 {
  while(!pq.empty())
  pq.pop();
   va[i].first=1;
   va[i].second=i-1;
   pq.push(1);
   pq.push(i-1);
   int val=calc(pq,1);
   for(j=i/2-1;j<=i/2;++j)
   {
     while(!pq.empty())
     pq.pop();
    pq.push(j);
    pq.push(i-j);
    int vv=calc(pq,1);
    if(vv<=val)
    {
     va[i].first=j;
     va[i].second=i-j;
     val=vv;
    }
   }
   fin[i]=val;
 }
}
int main()
{
// preprocess();

 int t,i,j,n,k,ele,p;
 cin>>t;
 for(p=1;p<=t;++p)
 {
  cin>>n;
  int dp[n][1001];
  int a[n];
  int ans=100000000;
  for(i=0;i<n;++i)
  cin>>a[i];

  sort(a,a+n);
  for(i=0;i<n;++i)
  for(j=0;j<=a[i];++j)
  dp[i][j]=100000000;
  int sum=a[0]-1;
  for(j=1;j<=a[0];++j)
  {
   int pa=j-1;
   int maxm=a[0]/j;
   if(maxm*j<a[0])
   maxm++;
   dp[0][pa]=maxm+pa;
  }
  for(i=1;i<n;++i)
  {
   int ste=sum+a[i]-1;
   ste=min(ste,a[n-1]);
   for(j=0;j<=ste;++j)
   {
     for(k=0;k<=j;++k)
     {
     int pa=j-k;
     int maxm=a[i]/(pa+1);
     if(maxm*(pa+1)<a[i])
     maxm++;
     dp[i][j]=min(dp[i][j],j+max(maxm,dp[i-1][k]-k));
     }
   }

  }
  for(i=0;i<=a[n-1];++i)
  ans=min(ans,dp[n-1][i]);
  cout<<"Case #"<<p<<":"<<" ";
  cout<<ans<<endl;
 }
}
