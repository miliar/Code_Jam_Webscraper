# include <iostream>
# include <fstream>
# include <sstream>
# include <algorithm>
# include <cstdio>
# include <cmath>
# include <numeric>
# include <cstdlib>
# include <cstring>
# include <vector>
# include <list>
# include <set>
# include <map>
# include <stack>
# include <queue>
# include <cctype>
# include <climits>
# include <complex>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> pii;
typedef vector<int> vi;
#define rep(i,a,b) for(int i=a;i<b;i++)
#define pb push_back
#define mp make_pair
#define inf 1000000000
#define mod 1000000007
#define mst(a,b) memset(a,b,sizeof(a))
#define pi (double)(3.141592653589793)

long long int m[1010];
int main()
{
      freopen("in.txt", "r", stdin);
  freopen("out.txt", "w", stdout);
  long long int i,j,k,t,n,xx=0,yy=0,maxi=0;
  cin>>t;
  for(i=1;i<=t;i++)
  {
      xx=0,yy=0,maxi=0;
    //  scanf("%lld",&n);
    cin>>n;
      for(j=0;j<n;j++)
      {
        //scanf("%lld",&m[j]);
          cin>>m[j];
          if(j>0)
           {

               if(m[j]<m[j-1])
               {
                   maxi=max(maxi,m[j-1]-m[j]);
                   xx+=(m[j-1]-m[j]);

               }
           }
      }

      for(j=1;j<n;j++)
      {
          if(maxi>=m[j-1])
            yy+=(m[j-1]);
          else
            yy+=maxi;
      }

      printf("Case #%lld: %lld %lld\n",i,xx,yy);


  }

    return 0;
}
