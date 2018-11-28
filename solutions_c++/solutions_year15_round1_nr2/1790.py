//#include <iostream>
//#include <vector>
//#include <list>
//#include <map>
//#include <set>
//#include <deque>
//#include <queue>
//#include <stack>
//#include <bitset>
//#include <algorithm>
//#include <functional>
//#include <numeric>
//#include <utility>
//#include <sstream>
//#include <iomanip>
//#include <cstdio>
//#include <cstdlib>
//#include <cctype>
//#include <string>
//#include <cstring>
//#include <cmath>
//#include <ctime>
//#include <cassert>
//using namespace std;
//
//const double PI = acos(-1.0);
//const double EPS = 1e-11;
//const int INF = 0x7fffffff;
//const int MOD=(int)1e9+7;
//const int dx[4]={-1,0,1,0};
//const int dy[4]={0,1,0,-1};
//
//typedef long long LL;
//typedef pair<int,int> PII;
//typedef pair<LL,LL> PLL;
//
//template<class T> inline T gcd(T a,T b)
//{if(a<0)return gcd(-a,b);if(b<0)return gcd(a,-b);return (b==0)?a:gcd(b,a%b);}
//template<class T> inline T lcm(T a,T b)
//{if(a<0)return lcm(-a,b);if(b<0)return lcm(a,-b);return a*(b/gcd(a,b));}
//template<class T> inline T euclide(T a,T b,T &x,T &y)
//{if(a<0){T d=euclide(-a,b,x,y);x=-x;return d;}
//if(b<0){T d=euclide(a,-b,x,y);y=-y;return d;}
//if(b==0){x=1;y=0;return a;}else{T d=euclide(b,a%b,x,y);T t=x;x=y;y=t-(a/b)*y;return d;}}
//
//int n;
//int B,Time[1111];
//
//LL solve(LL time){
//	if(time==0)
//		return B;
//	LL ans=0;
//	for(int i=0;i<B;i++)
//		ans+=(time-1)/Time[i]+1;
//	return ans;
//}
//
//int main()
//{
//	freopen("B-small-attempt0.in","r",stdin);
//	//freopen("out.txt","w",stdout);
//	int T;
//	scanf("%d",&T);
//	int nCase=1;
//	while(T--){
//		scanf("%d%d",&B,&n);
//		for(int i=0;i<B;i++)
//			scanf("%d",Time+i);
//		LL l=0,r=100000000000000ll,mid,num;
//		while(l<r){
//			mid=(l+r)/2;
//			num=solve(mid);
//			if(num>=n)
//				r=mid;
//			else
//				l=mid+1;
//		}
//		num=solve(l);
//		vector<pair<int,int>> table;
//		for(int i=0;i<B;i++)
//			if((l-1)%Time[i]==0){
//				table.push_back(make_pair(Time[i],-i));
//			}
//		sort(table.begin(),table.end());
//		int ans= -table[num-n].second + 1;
//		printf("Case #%d: %d\n",nCase++,ans);
//	}
//	return 0;
//}


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
#include <cassert>
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
int B,Time[1111];

int main()
{
	freopen("B-small-attempt1.in","r",stdin);
	freopen("out.txt","w",stdout);
	int T;
	scanf("%d",&T);
	int nCase=1;
	while(T--){
		scanf("%d%d",&B,&n);
		for(int i=0;i<B;i++)
			scanf("%d",Time+i);
		int beishu=Time[0];
		for(int i=1;i<B;i++)
			beishu=lcm(Time[i],beishu);
		int sum=0;
		for(int i=0;i<B;i++)
			sum+=beishu/Time[i];
		n%=sum;
		vector<int> t(B,0);
		int ans;
		if(n==0){
			int mn=0x7fffffff;
			for(int i=B-1;i>=0;i--)
				if(Time[i]<mn){
					mn=Time[i];
					ans=i+1;
				}
		}
		for(int i=0;i<n;i++){
			int ind,mn=0x7fffffff;
			for(int j=0;j<B;j++){
				if(t[j]<mn){
					mn=t[j];
					ind=j;
				}
			}
			t[ind]+=Time[ind];
			if(i==n-1)
				ans=ind+1;
		}
		printf("Case #%d: %d\n",nCase++,ans);
	}
	return 0;
}


