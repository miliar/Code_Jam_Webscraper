#include <bits/stdc++.h>
using namespace std;
int main()
{
   int t,c,s,i,j,k;
   freopen("D-small-attempt0.txt","rt",stdin);
   freopen("output.txt","wt",stdout);
   cin>>t;
   for(j=0;j<t;j++)
   {
      cin>>k>>c>>s;
      cout<<"Case #"<<j+1<<": ";
      for(i=1;i<=s;i++)
      {
          cout<<i<<" ";
      }
      cout<<endl;
   }
   return 0;
}
