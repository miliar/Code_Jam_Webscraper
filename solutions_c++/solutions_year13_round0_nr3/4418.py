#include <iostream>
#include <fstream>
#include <sstream>
#include <utility>
#include <vector>
#include <list>
#include <string>
#include <stack>
#include <queue>
#include <deque>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <numeric>
#include <bitset>
#include <complex>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <climits>
using namespace std;

#define lp for(;;)
#define repf(i,a,b) for (int i=(a);i<(b);++i)
#define rep(i,n) repf(i,0,n)
#define ft(i,a,b) for (int i=(a);i<=(b);++i)
#define fdt(i,a,b) for (int i=(a);i>=b;--i)
#define feach(e,s) for (typeof((s).begin()) e=(s).begin();e!=(s).end();++e)
#define fsubset(subset,set) for (int subset=set&(set-1);subset;subset=(subset-1)&set)
#define forin(i,charset) for (cstr i=charset;*i;i++)
#define whl while
#define rtn return
#define fl(x,y) memset((x),sizeof(x),char(y))
#define clr(x) fl(x,char(0))
#define pb push_back
#define mp make_pair
#define x first
#define y second
#define sz(x) (int((x).size()))
#define all(x) (x).begin(),(x).end()
#define srt(x) sort(all(x))
#define uniq(x) srt(x),(x).erase(unique(all(x)),x.end());
#define pr pair
#define que queue
#define prq priority_queue
#define itr iterator
#define sf scanf
#define pf printf
#define pdb(prcs,x) printf("%."#prcs"f",(abs(x)<1e-##prcs)?0.0:x)
#define input(in) freopen(in,"r",stdin)
#define output(out) freopen(out,"w",stdout)

typedef long long int LL;
typedef pr<int,int> pii;
typedef pr<LL,LL> pll;
typedef pr<double,double> pdd;
typedef pr<string,int> psi;
typedef map<int,int> mii;
typedef map<string,int> msi;
typedef map<char,int> mci;
typedef set<int> si;
typedef set<string> ss;
typedef que<int> qi;
typedef prq<int> pqi;
typedef vector<int> veci;
typedef vector<bool> vecb;
typedef vector<string> vecs;
typedef vector<double> vecdb;

const int oo=(~0u)>>1;
const LL lloo=(~0ull)>>1;
const double dboo=1e+20;
const double eps=1e-8;
const double pi=acos(-1.0);
const int MOD=1000000007;
char stemp[100];
bool hwcheck(LL num)
{
	 int p=1;
	 int len=0;
	 while(num)
	 {
		  stemp[p++]=num%10;
		  num/=10;
		  len++;
	 }
	 for (int i = 1,j=len; i <j; ++i,--j)
	 {
		  if(stemp[i]!=stemp[j])
			   return 0;
	 }
	 return 1;
}
int T;
LL l,r;
int main(int argc, char *argv[])
{
	 sf("%d",&T);
	 ft(tt,1,T)
	 {
		  int cnt=0;
		  cin>>l>>r;
		  LL low=1;
		  while(low*low<l)
			   low++;
		  low--;
		  LL up=1;
		  while(up*up<r)
			   up++;
		  for (LL i = low; i <= up; ++i)
		  {
			   if(i*i<l||i*i>r)
					continue;
			   if(hwcheck(i)&&hwcheck(i*i))
					cnt++;
		  }
		  pf("Case #%d: %d\n",tt,cnt);
	 }
	 return 0;
}
