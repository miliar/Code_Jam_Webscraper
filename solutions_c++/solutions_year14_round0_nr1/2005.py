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


int T,a,row,flag[17],num;
int main()
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("output.txt","w",stdout);
	//outfile.open("output.txt");
	cin>>T;
	num=0;
	while(T--)
	{
		memset(flag,0,sizeof(flag));
		for(int cnt=1;cnt<=2;cnt++)
		{
			cin>>row;
			for(int i=1;i<=4;i++)
				for(int j=1;j<=4;j++)
				{
					cin>>a;
					if(i==row)
						flag[a]++;
				}
		}
		int cnt=0,res;
		for(int i=1;i<=16;i++)
			if(flag[i]>1)
			{
				cnt++;
				res=i;
		    }
		cout<<"Case #"<<++num<<": ";
		if(cnt==1)
			cout<<res<<endl;
		else if(cnt>1)
			cout<<"Bad magician!"<<endl;
		else
			cout<<"Volunteer cheated!"<<endl;
	}
	return 0;
}
