
//This template is CopyRight By WenX(R), Southeast University, China
//wenxiao1992@gmail.com
//This is for GCJ 2010 Round 3
//2010-6-12
#pragma comment(linker, "/STACK:64000000")
#define _CRT_SECURE_NO_WARNINGS
#pragma warning (disable: 4996)

//SYS
#include <iostream>
#include <string>/////////
#include <cstring>////////This two
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <complex>
#include <cassert>
//ALG
#include <list>
#include <vector>
#include <stack>
#include <map>
#include <set>
#include <bitset>
#include <queue>
#include <algorithm>
///Unknown
#include <cstddef>///?
#include <cassert>///?
#include <sstream>///?
#include <functional>///?
#include <numeric>///?
#include <utility>///?
#include <climits>///?
#include <numeric>///?

using namespace std;

#define fori(n)	 for(i=0;i<n;i++)
#define forj(n)  for(j=0;j<n;j++)
#define fork(n)  for(k=0;k<n;k++)
#define fori1(n) for(i=1;i<=n;i++)
#define forj1(n) for(j=1;j<=n;j++)
#define fork1(n) for(k=1;k<=n;k++)
#define FOR(i,n) for(i=0;i<n;i++)
#define FOR1(i,n) for(i=1;i<=n;i++)

typedef vector<int>    vi;
typedef vector<string> vs;

#define pub(x) push_back(x)
#define puf(x) push_front(x)
#define pob(x) pop_back(x)
#define pof(x) pop_front(x)

const double pi=acos(-1.0);
const double eps=1e-9;
const long dx[]={1,0,-1,0};
const long dy[]={0,1,0,-1};
#define zero(f){f>0?(f<eps):(f>-eps)}//ONLY for float and double

template<class T> inline void checkmin(T &a,T b){if(b<a) a=b;}//NOTES:checkmin(
template<class T> inline void checkmax(T &a,T b){if(b>a) a=b;}//NOTES:checkmax(
template<class T> inline int countbit(T n)
{return (n==0)?0:(1+countbit(n&(n-1)));}//NOTES:countbit(
template<class T> inline T gcd(T a,T b)//NOTES:gcd(
{if(a<0)return gcd(-a,b);if(b<0)return gcd(a,-b);return (b==0)?a:gcd(b,a%b);}
template<class T> inline T lcm(T a,T b)//NOTES:lcm(
{if(a<0)return lcm(-a,b);if(b<0)return lcm(a,-b);return a*(b/gcd(a,b));}
template<class T> inline bool isPrimeNumber(T n)//NOTES:isPrimeNumber(
  {if(n<=1)return false;for (T i=2;i*i<=n;i++) if (n%i==0) return false;return true;}


int anss[11];
int gans(int n,int p){//p = 1 if w, 0 if l
	int ans=0;
	if(p==0)
		return 0;
	if(p<(1<<(n-1)))
		p=(1<<(n-1));
	if(p&(1<<(n-1)))
		anss[n]=1;
	gans(n-1,(p&((1<<(n-1))-1)));
}

int main(void)
{
    int cc,tt;
	int aa,ab;
    scanf("%d",&tt);
    FOR1(cc,tt){
		int n,p;
		aa=ab=0;
		scanf("%d%d",&n,&p);
		memset(anss,0,sizeof(anss));
		gans(n,(1<<n)-p);
		for(int i=0;i<=n;i++)
			if(anss[i]){
				aa=aa*2+1;
			}

		aa=(1<<n)-1-aa;
		int t=(1<<n)-p,i;
		for(i=n-1;i>=0;i--)
			if(t&(1<<i))
				break;
		if(i==-1)
			ab=(1<<n)-1;
		else if(i==n-1)
			ab=0;
		else
			ab=(1<<(n-i))-2;
        printf("Case #%d: %d %d\n",cc,ab,aa);
    }
	return 0;
}
