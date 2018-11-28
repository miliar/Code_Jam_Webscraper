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
    for(int tc=1;tc<=T;tc++)
    {
        double naomi[1001],ken[1001];
        int n,war=0,dwar=0;
        fin>>n;
        for(int i=0;i<n;i++)
            fin>>naomi[i];
        for(int i=0;i<n;i++)
            fin>>ken[i];
        sort(naomi,naomi+n);
        sort(ken,ken+n);
        int indy1=0,indy2=0;
        while(indy1<n)
        {
            if(naomi[indy1]>ken[indy2])
            {
                dwar++;
                indy1++;
                indy2++;
            }
            else indy1++;
        }
        indy1=indy2=0;
        while(indy1<n)
        {
            if(naomi[indy2]<ken[indy1])
            {
                war++;
                indy1++;
                indy2++;
            }
            else indy1++;
        }
        fout<<"Case #"<<tc<<": "<<dwar<<" "<<n-war<<"\n";
    }
    return 0;
}
