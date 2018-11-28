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

char s[1001];
long long sum[1001];
int main()
{
     freopen("in.txt", "r", stdin);
  freopen("out.txt", "w", stdout);
  long long int t,i,j,k,r,c,w,xx;

  cin>>t;

  rep(i,1,t+1)
  {
      xx=0;
    cin>>r>>c>>w;
   // if(c%w==0)
        xx=c/w;
     //   else
         //   xx=c/w+1;
         if(c%w==0)
        xx+=w-1;
        else
            xx+=w;
       // xx--;


      cout<<"Case #"<<i<<": "<<xx<<endl;
  }

    return 0;
}
