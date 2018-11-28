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
#include<iomanip>
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
    FILE *file;
    file=fopen("out","w");
    std::ios::sync_with_stdio(false);
    ifstream fin("in");
    ofstream fout("out");
    fout.precision(7);
    int T;
    fin>>T;
    for(int tc=1;tc<=T;tc++)
    {
        double C,F,X,rate=2,time=0,temp1,temp2,temp3;
        fin>>C>>F>>X;
        while(1)
        {
            temp1=X/rate;
            temp2=rate+F;
            temp3=(C/rate)+(X/temp2);
            if(temp3<temp1)
                time+=C/rate;
            else
            {
                time+=X/rate;
                break;
            }
            rate+=F;
        }
        fprintf(file,"Case #%d: %.7f\n",tc,time);    
    }
    fclose(file);
    return 0;
}
