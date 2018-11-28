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

int T,N;
double a[1001],b[1001];
int main()
{
	freopen("D-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	//outfile.open("output.txt");
	cin>>T;
	int num=0;
	while(T--)
	{
		cin>>N;
		for(int i=0;i<N;i++)
			cin>>a[i];
		for(int i=0;i<N;i++)
			cin>>b[i];
		sort(a,a+N);
		sort(b,b+N);
		int pos1=0,pos2=0,score1=0,score2=0;
		while(pos1<N&&pos2<N)
		{
			if(a[pos1]>b[pos2])
			{
				pos1++;
				pos2++;
				score1++;
			}
			else
				pos1++;
		}
		pos1=pos2=0;
		while(pos1<N&&pos2<N)
		{
			if(a[pos1]<b[pos2])
			{
				pos1++;
				pos2++;
				score2++;
			}
			else
				pos2++;
		}
		score2=N-score2;
		cout<<"Case #"<<++num<<": ";
		cout<<score1<<" "<<score2<<endl;
	}
	return 0;
}
