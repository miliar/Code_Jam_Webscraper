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


int main()
{
 ios_base::sync_with_stdio(0);

 fi;fo;

 int test,row,x;

 cin>>test;

 for(int t=1;t<=test;t++)
 {
        vector<int> a,b;

        cin>>row;

        for(int i=1;i<=4;i++)
             for(int j=1;j<=4;j++)
        {
                cin>>x;

                if(i==row)
                     a.pb(x);
        }

        cin>>row;

        for(int i=1;i<=4;i++)
             for(int j=1;j<=4;j++)
        {
                cin>>x;

                if(i==row)
                     b.pb(x);
        }

        int cn=0,ans=-1;

        for(int i=0;i<4;i++)
        {
              bool mila=false;

              for(int j=0;j<4;j++)
                  if( a[i]==b[j])
                    mila=true;

              if(mila)
              {
                  cn++;
                  ans=a[i];
              }
        }

        if(cn==1)
             cout<<"Case #"<<t<<": "<<ans<<endl;
        else if( cn > 1)
               cout<<"Case #"<<t<<": "<<"Bad magician!"<<endl;
        else
               cout<<"Case #"<<t<<": "<<"Volunteer cheated!"<<endl;



 }

 return 0;

}
