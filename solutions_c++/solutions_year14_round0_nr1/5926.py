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
#include <iostream> 
#include <iomanip> 
#include <cstdio> 
#include <cmath> 
#include <cstdlib> 
#include <cctype> 
#include <string> 
#include <cstring> 
#include <cstdio> 
#include <cmath> 
#include <cstdlib> 
#include <ctime> 
#include <string.h>

using namespace std; 

#define ALL(X)       (X).begin(),(X).end()
#define SIZE(X)      ((int)(X).size())
#define FORI(x,a,b)  for(x=(a);x<=(b);x++)
#define FORD(x,a,b)  for(x=(a);x>=(b);x--)
#define min(a,b)     ((a)<(b)?(a):(b))
#define max(a,b)     ((a)<(b)?(b):(a))
#define MEM(X,with)  memset((X),(with),sizeof(X))
#define Contains(X,item)    ((X).find(item)!=(X).end())
#define Contains_n(X,item)	(find((X).begin(),(X).end(),(item))!=(X).end())
#define rep(i,m,n) for((i)=m;(i)<(int)(n);(i)++)
#define PQ priority_queue
#define IT iterator
//#define N 1000005

//bool prime[N];
const int inf =(1<<30)-1;
const long long linf = (1ll<<62)-1;
const int dirx[]={-1,0,0,1,-1,-1,1,1}, diry[]={0,-1,1,0,-1,1,-1,1};
const double ERR = 1e-11, PI=(2*acos(0.0));


template<class T> bool cmpmin(T a, T b){return a<b;}
template<class T> bool cmpmax(T a, T b){return a>b;}
template<class T> inline T ABS(T a) {return ((a<0)?(-a):(a));}
template<class T> T GCD(T a,T b) {return ((!b)?(a):GCD(b,a%b));}
template<class T> T fastPow(T Base,T Power) {T Result=1; while(Power>0){if(Power&((T)1))Result*=Base; Power>>=1; Base*=Base;} return Result;}
template<class T> T fastModPow(T Base,T Power,T Mod) {T Result=1;while(Power>0){if(Power&((T)1))Result=(Result*Base)%Mod; Power>>=1; Base=(Base*Base)%Mod;} return (Result%Mod);}
inline int compDouble(double x,double y) {double d=x-y; if(d-ERR>0.0) return 1; else if(d+ERR<0.0) return -1; else return 0;}
inline void file(){freopen("A-small-attempt0.in","r",stdin);freopen("rle-size.txt","w",stdout);}
//void prim(){prime[0]=1;prime[1]=1;int i;long long j;for(i=2;i<N;i++){if(prime[i]==0){for(j=i,j=j*i;j<N;j+=i){prime[j]=1;}}}}

typedef long long ll;
typedef unsigned long long ull;
typedef stringstream   SS;
typedef vector<string> VS;
typedef vector<double> VD;
typedef vector<ll>     VL;
typedef vector<int>    VI;
int lowbit(int t){ return t&(t^(t-1));}

#define N 1000005
bool prime[N];
int yin[N],num[N];
void prim(){prime[0]=1;prime[1]=1;int i;long long j;for(i=2;i<N;i++){if(prime[i]==0){for(j=i,j=j*i;j<N;j+=i){if(prime[j]==0)yin[j]=i;prime[j]=1;}}}}
bool si[N];


int reta[5][5], retb[5][5];
int main() {
	file();
	int T, cas, i, j, n, m;
	scanf("%d", &T);
	for (cas = 1; cas <= T; cas++) {
		scanf("%d", &n);
		for (i = 0; i < 4; i++) {
			for (j = 0; j < 4; j++) {
				scanf("%d", &reta[i][j]);
			}
		}
		scanf("%d", &m);
		for (i = 0; i < 4; i++) {
			for (j = 0; j < 4; j++) {
				scanf("%d", &retb[i][j]);
			}
		}
		int ans, num = 0;
		for (i = 0; i < 4; i++) {
			for (j = 0; j < 4; j++) {
				if(reta[n-1][i] == retb[m-1][j]){
					ans = reta[n-1][i];
					num++;
				}
			}
		}
		if (num == 1) {
			printf("Case #%d: %d\n", cas, ans);
		} else if (num > 1) {
			printf("Case #%d: Bad magician!\n", cas);
		} else {
			printf("Case #%d: Volunteer cheated!\n", cas);
		}
	}
	return 0;
}