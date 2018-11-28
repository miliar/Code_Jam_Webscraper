#include<iostream>
#include<math.h>
#include<string.h>
using namespace std;
int main()
{
 freopen("lot.txt","r",stdin);
 freopen("lota.txt","w",stdout);
 int t;
 cin>>t;
 for(int q=1;q<=t;++q)
 {
  long long int a,b,k,ans=0;
  cin>>a>>b>>k;
  for(int i=0;i<a;++i)
  {
   for(int j=0;j<b;++j)
   {
    long long int q=i&j;
    if(q<k)
    ans++;        
   }        
  }
  printf("Case #%d: %d\n",q,ans);        
 }    
}
