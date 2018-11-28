#include <iostream>
#include <sstream>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
#include <queue>

#include <cstring>
#include <cmath>
#include <cctype>
#include <cstdlib>
#include <cstdio>

using namespace std;
typedef long long LL;

int isPal(LL n)
{
   ostringstream oss;
   oss<<n;
   string s = oss.str();
   for(int i = 0; i < (s.size()/2); i++) {
      if(s[i]!=s[s.size()-i-1]) return 0;
   }
   return 1;
}
int main()
{
   freopen("C-small-attempt0.in","r",stdin);
   freopen("C-small-out.txt","w",stdout);

   int T;
   cin>>T;
   for(int tc = 1; tc <= T; tc++) {
      LL a,b;
      cin>>a>>b;
      LL ret = 0;
      for(LL i = 1; i*i<=b; i++) {
         if(!isPal(i)) {
            continue;
         }
         if(i*i<a) continue;
         if(isPal(i)&&isPal(i*i)) {
            ret++;
         }
      }
      cout<<"Case #"<<tc<<": "<<ret<<endl;

   }
   return 0;
}
