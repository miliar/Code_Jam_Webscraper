#include <iostream>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iomanip>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cmath>
#include <ctime>
using namespace std;

const double PI = acos(-1.0);
const double EPS = 1e-11;
const int INF = 0x7fffffff;
const int MOD=(int)1e9+7;
const int dx[4]={-1,0,1,0};
const int dy[4]={0,1,0,-1};

typedef long long LL;
typedef pair<int,int> PII;
typedef pair<LL,LL> PLL;

template<class T> inline T gcd(T a,T b)
{if(a<0)return gcd(-a,b);if(b<0)return gcd(a,-b);return (b==0)?a:gcd(b,a%b);}
template<class T> inline T lcm(T a,T b)
{if(a<0)return lcm(-a,b);if(b<0)return lcm(a,-b);return a*(b/gcd(a,b));}
template<class T> inline T euclide(T a,T b,T &x,T &y)
{if(a<0){T d=euclide(-a,b,x,y);x=-x;return d;}
if(b<0){T d=euclide(a,-b,x,y);y=-y;return d;}
if(b==0){x=1;y=0;return a;}else{T d=euclide(b,a%b,x,y);T t=x;x=y;y=t-(a/b)*y;return d;}}


int n;
int p[1010];
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int T;
	scanf("%d",&T);
	int nCase=1;
	while(T--){
		scanf("%d",&n);
		for(int i=0;i<n;i++)
			scanf("%d",p+i);
		int ans=INF;
		for(int cur=1;cur<=1000;cur++){
			int tmp=cur;
			for(int i=0;i<n;i++)
				tmp+=(p[i]-1)/cur;
			ans=min(ans,tmp);
		}
		printf("Case #%d: %d\n",nCase++,ans);
	}
	return 0;
}
