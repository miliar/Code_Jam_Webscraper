#include <iostream>
#include <fstream>

using namespace std;

int main()
{
   freopen("B-large.in","r",stdin);
   freopen("B-large.out","w",stdout);
   cin.tie(0);
   ios_base::sync_with_stdio(0);
   int T;
   cin>>T;
   for(int t = 1; t <= T; ++t)
   {
      int ans = 0;
      string s;
      cin>>s;
      char x = s[0];
      for(int i = 0; i < s.size(); ++i)
         if(s[i] != x)
         {
            x = (x == '+' ? '-' : '+');
            ++ans;
         }
      cout<<"Case #"<<t<<": "<<ans + (x == '-')<<"\n";
   }
}
