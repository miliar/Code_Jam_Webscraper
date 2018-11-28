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
int main()
{
 int t,i,j,n,k;
 cin>>t;
 for(k=1;k<=t;++k)
 {

  cin>>n;
  int a[n+1];
  for(i=0;i<=n;++i)
  scanf("%1d",&a[i]);
  int sum=0;
  int ans=0;
  for(i=0;i<=n;++i)
  {
   if(a[i]==0)
   continue;
   if(sum<i)
   {
    ans+=(i-sum);
    sum=i;
   }
   sum+=a[i];
  }
  cout<<"Case #"<<k<<":"<<" ";
  cout<<ans<<endl;
 }
}
