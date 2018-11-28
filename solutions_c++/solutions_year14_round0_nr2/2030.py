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

const double pi=acos(-1.0);
const double eps=1e-11;
typedef long long LL;
typedef pair<int,int> PII;
typedef pair<LL,LL> PLL;

template<class T> inline void Min(T &a,T b){if(b<a) a=b;}
template<class T> inline void Max(T &a,T b){if(b>a) a=b;}

template<class T> inline T gcd(T a,T b)
{if(a<0)return gcd(-a,b);if(b<0)return gcd(a,-b);return (b==0)?a:gcd(b,a%b);}
template<class T> inline T lcm(T a,T b)
{if(a<0)return lcm(-a,b);if(b<0)return lcm(a,-b);return a*(b/gcd(a,b));}
template<class T> inline T euclide(T a,T b,T &x,T &y)
{if(a<0){T d=euclide(-a,b,x,y);x=-x;return d;}
if(b<0){T d=euclide(a,-b,x,y);y=-y;return d;}
if(b==0){x=1;y=0;return a;}else{T d=euclide(b,a%b,x,y);T t=x;x=y;y=t-(a/b)*y;return d;}}

int T;
double ans,c,f,x;
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	//outfile.open("output.txt");
	cin>>T;
	int num=0;
	while(T--)
	{
		cin>>c>>f>>x;
		ans=x/2;
		int cnt=x/c;
		double per=2;
		double time=0;
		for(int i=1;i<=cnt;i++)
		{
			ans=ans<(time+c/per+x/(per+f))?ans:(time+c/per+x/(per+f));
			time+=c/per;
			per+=f;
		}
		cout<<"Case #"<<++num<<": ";
		cout<<fixed<<setprecision(7)<<ans<<endl;
	}
	return 0;
}
