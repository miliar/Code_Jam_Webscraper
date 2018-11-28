// @author peter50216
// #includes {{{
#include <bits/stdc++.h>
using namespace std;
// }}}
// #defines {{{
#define FOR(i,c) for(__typeof((c).begin()) i=(c).begin();i!=(c).end();i++)
#define SZ(x) ((int)(x).size())
#define ALL(x) (x).begin(),(x).end()
#define REP(i,n) for(int i=0;i<(n);i++)
#define REP1(i,a,b) for(int i=(a);i<=(b);i++)
#define REPL(i,x) for(int i=0;x[i];i++)
#define PER(i,n) for(int i=(n)-1;i>=0;i--)
#define PER1(i,a,b) for(int i=(a);i>=(b);i--)
#define RI(x) scanf("%d",&x)
#define DRI(x) int x;RI(x)
#define RII(x,y) scanf("%d%d",&x,&y)
#define DRII(x,y) int x,y;RII(x,y)
#define RIII(x,y,z) scanf("%d%d%d",&x,&y,&z)
#define DRIII(x,y,z) int x,y,z;RIII(x,y,z)
#define RS(x) scanf("%s",x)
#define PI(x) printf("%d\n",x)
#define PIS(x) printf("%d ",x)
#define CASET int ___T,cas=1;scanf("%d ",&___T);while(___T--)
#define CASEN0(n) int cas=1;while(scanf("%d",&n)!=EOF&&n)
#define CASEN(n) int cas=1;while(scanf("%d",&n)!=EOF)
#define MP make_pair
#define PB push_back
#define MS0(x) memset(x,0,sizeof(x))
#define MS1(x) memset(x,-1,sizeof(x))
#define SEP(x) ((x)?'\n':' ')
#define F first
#define S second
#ifdef ONLINE_JUDGE
#define FILEIO(x) freopen(#x ".in","r",stdin);freopen(#x ".out","w",stdout);
#define FILEIOS freopen("input.txt","r",stdin);freopen("output.txt","w",stdout);
#else
#define FILEIO(x) ;
#define FILEIOS ;
#endif
typedef pair<int,int> PII;
typedef long long LL;
typedef unsigned long long ULL;
// }}}

LL a[1010000];
const LL INFLL=10000000000000000LL;
inline LL f(LL a,LL b,LL c){if(c<0)return INFLL;return max(a,max(b,c));}
int main(){
  CASET{
    DRIII(n,p,q);
    DRII(r,s);
    LL sum=0;
    REP(i,n){
      a[i]=(i*(LL)p+q)%r+s;
      sum+=a[i];
    }
    int i1=0,i2=n-1;
    LL s1=0,s2=0;
    while(i1<n){
      s1+=a[i1];
      if(s1*3>sum)break;
      i1++;
    }
    while(i2>=0){
      s2+=a[i2];
      if(s2*3>sum)break;
      i2--;
    }
    LL ss1=s1-a[i1];
    LL ss2=s2-a[i2];
    LL ans=min(min(f(s1,s2,sum-s1-s2),f(s1,ss2,sum-s1-ss2)),
        min(f(ss1,s2,sum-ss1-s2),f(ss1,ss2,sum-ss1-ss2)));
    LL ls=sum-ss2;
    LL lss=0;
    for(int i=0;i<=i2;i++){
      lss+=a[i];
      ans=min(ans,max(lss,ls-lss));
    }
    LL rs=sum-ss1;
    LL rss=0;
    for(int i=i1;i<n;i++){
      rss+=a[i];
      ans=min(ans,max(rss,rs-rss));
    }
    printf("Case #%d: %.12f\n",cas++,(double)(sum-ans)/(double)sum);
  }
}
// vim: fdm=marker:commentstring=\ \"\ %s:nowrap:autoread

