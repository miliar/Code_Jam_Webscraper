#include<bits/stdc++.h>

using namespace std;

long long int a[1000000];
int main()
{
freopen("niki.in","r",stdin);
freopen("niki.out","w",stdout);

int t;
cin>>t;
for(int kk=1;kk<=t;kk++)
{

 long long int n,i,j,k,ans1=0,ans2=0,ma=0;
 cin>>n;

 for(i=0;i<n;i++)
  cin>>a[i];

 for(i=1;i<n;i++)
 {
  if(a[i]<a[i-1])
  {
   ans1+=(a[i-1]-a[i]);
   }
 }

 for(i=0;i<n-1;i++)
 {
  k=a[i]-a[i+1];
  if(k>ma)
  ma=k;
 }

for(i=0;i<n-1;i++)
{
ans2+=min(a[i],ma);
}

printf("Case #%d: %lld %lld\n", kk,ans1,ans2);
}
return 0;
}
