/*"The Woods are lovely dark and deep,
But i have promises to keep,
Miles to go before i sleep and Miles to go before i Sleep"
*/
#include<bits/stdc++.h>
#define pb(n) push_back(n)
unsigned long long mod=1000000007;
using namespace std;
#define GI ({long int t;scanf("%ld",&t);t;})
#define all(x) x.begin(),x.end() //sort(all(x))
#define sz(h1) h1.size()
int main()
{
  int T;
cin>>T;
int nn=1;
while(T--)
{
int a,b,k,ans=0;
cin>>a>>b>>k;
for(int i=0;i<a;i++)
for(int j=0;j<b;j++)
if((i&j)<k)
ans++;
  printf("Case #%d: ", nn);
  cout<<ans<<endl;
  nn++;
  }
  return 0;
}
