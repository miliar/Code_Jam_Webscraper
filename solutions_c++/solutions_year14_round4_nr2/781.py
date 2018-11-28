#include <iostream>
#include <iomanip>
#include <fstream>
#include <sstream>
#include <cassert>

#include <algorithm>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <cmath>
#include <numeric>
#include <bitset>

#include <cstdio>
#include <cstring>

using namespace std;

#define rep(i, n) for (int i = 0, _n = (int)(n); i < _n; i++)
#define fer(i, x, n) for (int i = (int)(x), _n = (int)(n); i < _n; i++)
#define rof(i, n, x) for (int i = (int)(n), _x = (int)(x); i-- > _x; )
#define fch(i, x) for (__typeof(x.begin()) i = x.begin(); i != x.end(); i++)
#define sz(x) (int((x).size()))
#define pb push_back
#define mkp make_pair
#define all(X) (X).begin(),(X).end()

#define X first
#define Y second

template<class T> inline void smin(T &a, T b){if(b<a)a=b;}
template<class T> inline void smax(T &a, T b){if(a<b)a=b;}

typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;
typedef pair<ll,ll> pll;
typedef vector<pii> vii;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<vii> vvii;


typedef vector<char> VC;
typedef vector<string> VS;
typedef vector<ll> VL;
typedef vector<double> VD;
typedef set<int> SI;
typedef set<string> SS;
typedef map<int, int> MII;
typedef map<string, int> MSI;

template<class T> inline void RST(T &A){memset(A, 0, sizeof(A));}
template<class T> inline void FLC(T &A, int x){memset(A, x, sizeof(A));}
template<class T> inline void CLR(T &A){A.clear();}

/** Constant List .. **/ //{
const int dx4[] = {-1, 0, 1, 0};
const int dy4[] = {0, 1, 0, -1};
const int dx8[] = {-1, 0, 1, 0 , -1 , -1 , 1 , 1};
const int dy8[] = {0, 1, 0, -1 , -1 , 1 , -1 , 1};
const int mod = 1000000007;
//}

template<class T> inline T min(T a, T b, T c){return min(min(a, b), c);}
template<class T> inline T max(T a, T b, T c){return max(max(a, b), c);}
template<class T> inline T min(T a, T b, T c, T d){return min(min(a, b), min(c, d));}
template<class T> inline T max(T a, T b, T c, T d){return max(max(a, b), max(c, d));}
template<class T> inline T sqr(T a){return a*a;}
template<class T> inline T cub(T a){return a*a*a;}

////////////////////////////////////////////////////////////////////////////////
const int N = 1009;
int mxh;
int T,n,a[N],b[N];

void swap(int &a,int &b){int c=a;a=b;b=c;}
int work(int h,int mxh){
	memcpy(a,b,N);
	int i,j;
	int ret = 0;
	if(h>mxh) for(i=mxh;i<h;i++) swap(a[i],a[i+1]),ret++;
	else if(h<mxh) for(i=mxh;i>h;i--) swap(a[i],a[i-1]),ret++;
	//printf("ret:%d\n", ret);
	for(i=0;i<h-1;i++)
		for(j=0;j<h-1;j++)
			if(a[j]>=a[j+1]) swap(a[j],a[j+1]),ret++;
	for(i=h+1;i<n;i++)
		for(j=h+1;j<n-1;j++)
			if(a[j]<=a[j+1]) swap(a[j],a[j+1]),ret++;
	return ret;
}

int main()
{
	freopen("in.txt","r",stdin);
	freopen("b.txt","w",stdout)
	ios_base::sync_with_stdio(0);
	scanf("%d",&T);
	fer(tt,1,T+1){
		printf("Case #%d: ",tt);
		scanf("%d",&n);
		int tmp = -1,mxh=0;
		rep(i,n){
			scanf("%d",b+i);
			if(b[i]>tmp) tmp=b[i],mxh=i;
		}
		//rep(i,n) printf("%d ", b[i]);
		//printf("mx=%d\n", mxh);
		int ans = 10000000;
		rep(i,n) smin(ans,work(i,mxh));
		printf("%d\n", ans);
	}
	
}