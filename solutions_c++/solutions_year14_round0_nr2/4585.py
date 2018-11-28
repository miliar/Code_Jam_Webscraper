#include <algorithm>
#include <iomanip>
#include <iostream>
#include <sstream>
#include <cstring>
#include <cstdlib>
#include <climits>
#include <fstream>
#include <cctype>
#include <cstdio>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <cmath>
#include <ctime>
#include <map>
#include <set>
using namespace std;

#define pb push_back
#define mp make_pair
#define sz size()
#define bg begin()
#define en end()
#define Y second
#define X first
typedef long long ll;

#define fi freopen("input.txt","r",stdin)
#define fo freopen("output.txt","w",stdout)

const double pi     =   acos(-1.0);
const double eps    =   1e-8;

#define print(a) cout<<(#a)<<" = "<<a<<"  ";
#define println(a) cout<<(#a)<<" = "<<a<<"\n";
#define fill(a,val) memset(a ,val, sizeof(a) );

vector <string> parse(string s, string c)
{
  int len = c.length(), p = -len, np;
  vector <string> ans;

  do
    {
      np = s.find(c, p+len);
      ans.push_back(s.substr(p+len, np - p - len));
      p = np;
    }
  while (p != string::npos);

  return ans;
}


/*Solution code starts here */

double c,f,x;

double val( int s)
{
      double ans=0,cr=2.000000;

      for(int i=1;i<=s;i++)
      {
            ans+=(c/cr);
            cr+=f;
      }
      return ans;
}

#define maxn (1e8)

int main()
{
 ios_base::sync_with_stdio(0);

   fi;fo;

  int test;

  cin>>test;

 for(int t=1;t<=test;t++)
 {
       cin>>c>>f>>x;



        double ans=x/2.0;

        int s=1;

        while( (s*2<maxn) && (val(s) <=ans ) )
             { s=s*2;
//             cout<<s<<"  "<<val(s)<<endl;
             }

         if((s*2<maxn))
           s=s*2;

          double pc=0;
          double pr=2;

        for(int i=1;i<=s;i++)
        {
            double cc,cr;

            cc=pc+(c/pr);
            cr=pr+f;

            double ts=cc+(x/cr);
             ans=min( ans , ts);

             pc=cc; pr=cr;

        }

      printf("Case #%d: %0.9lf\n",t,ans);

 }



 return 0;

}

