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
  long long int t,i,j,k;

  cin>>t;

  rep(i,1,t+1)
  {
      cin>>j;

      scanf("%s",s);
      memset(sum,0,sizeof(sum));
      sum[0]=s[0]-48;
      long long int xx=0;
      for(k=1;k<=j;k++)
      {
          if(k<=sum[k-1])
            sum[k]=sum[k-1]+(s[k]-48);
          else
          {
              xx+=(k-sum[k-1]);
              sum[k]=k+(s[k]-48);
          }

      }
      cout<<"Case #"<<i<<": "<<xx<<endl;
  }

    return 0;
}
