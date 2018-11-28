#include <bits/stdc++.h>
using namespace std;
#define pb push_back
#define mp make_pair
#define bg begin()
#define en end()
#define Y second
#define X first
typedef long long ll;

#define fi freopen("input.txt","r",stdin)
#define fo freopen("output.txt","w",stdout)

const double pi     =   acos(-1.0);
const double eps    =   1e-8;

#define print(a) cout<<(#a)<<" = "<<a<<"\n";
#define fill(a,val) memset(a ,val, sizeof(a) );
#define sz(s) ((int)(s.size()))

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

#define maxn 1005

int N ;
int in[maxn];//cake size
int sum[maxn];//sum[i] stores the days taken todivide all cake into <=i size

bool solve( int day)
{
    for(int  sp=0;sp<=day-1;sp++)
    {
        int ms =day - sp;

        if( sum[ms]<=sp)
          return true;
    }
    return false;
}

void process(int test)
{
    scanf("%d",&N);

    int max_cake = 0;

    for(int i=1;i<=N;i++)
     {
         scanf("%d",&in[i]);
         max_cake = max( max_cake , in[i]);
     }

    //populate sum
    for(int ms=1;ms<=max_cake;ms++)
    {
        sum[ms]=0;

        for(int i=1;i<=N;i++)
        {
            int  pc =( in[i] + ms -1 )/ms;
            sum[ms]+=pc-1;
        }
    }

    //start binary seacr
    int ans = max_cake;

    int lo = 1, hi = max_cake;

    while( lo <= hi)
    {
        int mid = (lo+hi)/2;

        if( solve(mid))
        {
            hi = mid -1;
            ans=mid;
        }
        else
        {
            lo = mid +1;
        }
    }

    printf("Case #%d: %d\n",test,ans);


}

int main()
{
  int test;

  scanf("%d",&test);


  for(int i=1;i<=test;i++)
  {
      process(i);
  }

  return 0;
}

