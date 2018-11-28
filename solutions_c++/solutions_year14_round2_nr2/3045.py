#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<iostream>
#include<vector>
#include<cassert>
#include<sstream>
#include<map>
#include<set>
#include<stack>
#include<queue>
#include<algorithm>
#include<fstream>
using namespace std;
#define lld long long
#define llu long long unsigned
#define F first
#define S second
#define mod 1000000007
#define INF 1000000000
#define sd(n) scanf("%d",&n)
#define sl(n) scanf("%lld",&n)
#define su(n) scanf("%llu",&n)
#define pdn(n) printf("%d\n",n)
#define pln(n) printf("%lld\n",n)
#define pun(n) printf("%llu\n",n)
#define pd(n) printf("%d",n)
#define pl(n) printf("%lld",n)
#define pu(n) printf("%llu",n)
#define pn printf("\n")
#define ps printf(" ")
#define gc getchar_unlocked
#define fill(a,x) memset(a,x,sizeof(a))
#define PB push_back
#define MP make_pair
#define FOR(i,a,b) for(i=a;i<b;i++)
#define REP(i,a) FOR(i,0,a)
#define sz(a) int((a).size())
#define all(c) (c).begin(), (c).end()
#define tr(c,i) for(typeof(c.begin()) it=c.begin();it!=c.end();it++)
typedef vector<int> VI;
typedef vector< VI > VVI;
typedef pair<int,int> PII;
/*inline int ri()
{
  int ret=0;
  char c=gc();
  while(c<'0'||c>'9') c=gc();
  while(c>='0'&&c<='9')
  {
    ret=10*ret+c-48;
    c=gc();
  }
  return ret;
}
inline long long rll()
{
  long long ret=0;
  char c=gc();
  while(c<'0'||c>'9') c=gc();
  while(c>='0'&&c<='9')
  {
    ret=10*ret+c-48;
    c=gc();
  }
  return ret;
}*/
int main()
{
    std::ios::sync_with_stdio(false);
    ifstream fin("in");
    ofstream fout("out");
    int T;
    fin>>T;
    for(int z=1;z<=T;z++)
    {
        int a,b,k,ans=0;
        fin>>a>>b>>k;
        for(int i=0;i<a;i++)
            for(int j=0;j<b;j++)
                if((i&j)<k)
                    ans++;
        fout<<"Case #"<<z<<": "<<ans<<"\n";
    }
    return 0;
}
