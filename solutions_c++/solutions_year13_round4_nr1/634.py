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


const int mods=1000002013;
long long pri(int b,int e,int n){
	long long res=e-b;
	return ((n*2-res-1)*res/2)%mods;
}

long long enter[2100];
long long people[2100];
int index;

struct sts{
	long long peo;
	int flag;//0 in 1 out;
	long long st;
};
bool cmp( const sts & lhs, const sts & rhs )
{
	if(lhs.st==rhs.st)
		return lhs.flag>rhs.flag;
   return lhs.st < rhs.st;
}
sts info[2200];
int main(void)
{
	long long ansb,ansa;
    int cc,tt;
	int n,m,i,j;
    scanf("%d",&tt);
    FOR1(cc,tt){
		scanf("%d%d",&n,&m);
		ansb=ansa=0;
		index=0;
		for(int j=0;j<m;j++){
			int o,e,p;
			scanf("%d%d%d",&o,&e,&p);
			info[j*2].st=o;
			info[j*2].flag=1;
			info[j*2+1].st=e;
			info[j*2+1].flag=0;
			info[j*2].peo=info[j*2+1].peo=p;
			ansb+=(p*pri(o,e,n))%mods;
			ansb%=mods;
		}
		
		sort(info,info+2*m,cmp);

		for(int j=0;j<2*m;j++){
			if(info[j].flag){
				enter[index]=info[j].st;
				people[index]=info[j].peo;
				index++;
			}else{
				long long res=info[j].peo;
				while(res>0){
					if(res>=people[index-1]){
						index--;
						res-=people[index];
						ansa+=(people[index]*pri(enter[index],info[j].st,n))%mods;
						ansa%=mods;
					}else{
						ansa+=(res*pri(enter[index-1],info[j].st,n))%mods;
						ansa%=mods;
						people[index-1]-=res;
						res=0;
					}
				}
			}
		}



        printf("Case #%d: %d\n",cc,(ansb+mods-ansa)%mods);
    }
	return 0;
}



