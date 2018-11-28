#include <functional>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <sstream>
#include <iomanip>
#include <numeric>
#include <cstring>
#include <cassert>
#include <cstdio>
#include <string>
#include <vector>
#include <bitset>
#include <queue>
#include <stack>
#include <cmath>
#include <ctime>
#include <list>
#include <set>
#include <map>

using namespace std;

#define DO(n) for ( int ____n ## __line__ = n; ____n ## __line__ -- ; )

#define ALL(A) A.begin(), A.end()
#define BSC(A, x) (lower_bound(ALL(A), x) - A.begin())
#define CTN(T, x) (T.find(x) != T.end())
#define SZ(A) int(A.size())
#define PB push_back
#define MP(A, B) make_pair(A, B)
#define fi first
#define se second

typedef long long LL;


typedef vector<int> VI;
typedef map<int, int> MII;
typedef pair<int, int> PII;
typedef pair<LL, LL> PLL;



template<class T> inline void RST(T &A){memset(A, 0, sizeof(A));}
template<class T> inline void FLC(T &A, int x){memset(A, x, sizeof(A));}
template<class T> inline void CLR(T &A){A.clear();}

//}

/** Constant List .. **/ //{

const int dx4[] = {-1, 0, 1, 0};
const int dy4[] = {0, 1, 0, -1};

const int dx8[] = {-1, 0, 1, 0 , -1 , -1 , 1 , 1};
const int dy8[] = {0, 1, 0, -1 , -1 , 1 , -1 , 1};

const int dxhorse[] = {-2 , -2 , -1 , -1 , 1 , 1 , 2 , 2};
const int dyhorse[] = {1 ,  -1 , 2  , -2 , 2 ,-2 , 1 ,-1};

const int MOD = 1000000007;
//int MOD = 99990001;
const int INF = 0x3f3f3f3f /3;
const LL INFF = 1LL << 60;
const double EPS = 1e-9;
const double OO = 1e15;
const double PI = acos(-1.0); //M_PI;

//}

template<class T> inline void checkMin(T &a,const T b){if (b<a) a=b;}
template<class T> inline void checkMax(T &a,const T b){if (a<b) a=b;}
//}
template<class T> inline T low_bit(T x) {return x & -x;}
/*****************************************************************/
#define MAXN 200
#define inf 1000000000
typedef int elem_t;
const int N = 200;
int mp1[N][N] , mp2[N][N];
int n;
int G1[N] , G2[N] , pre[N];
void dijkstra(int n,elem_t mat[][MAXN],int s,elem_t* min,int* pre){
	int v[MAXN],i,j,k;
	for (i=0;i<n;i++)
		min[i]=INF,v[i]=0,pre[i]=-1;
	for (min[s]=0,j=0;j<n;j++){
		for (k=-1,i=0;i<n;i++)
			if (!v[i]&&(k==-1||min[i]<min[k]))
				k=i;
		for (v[k]=1,i=0;i<n;i++)
			if (!v[i]&&min[k]+mat[k][i]<min[i])
				min[i]=min[k]+mat[pre[i]=k][i];
	}
}
int m , p;
struct Edge{
    int s , t , l , r;
    void input(){
        scanf("%d%d%d%d" , &s , &t , &l , &r);
        s--;
        t--;
    }
}e[N];
int d[N] , TAT;
bool check(int TOT , int p){
    for (int i = 0 ; i < n;  ++i)
        for (int j = 0 ; j < n ; ++j)
            if (i == j) mp1[i][j] = mp2[i][j] = 0;
            else mp1[i][j] = mp2[i][j] = INF;
    for (int i = 0 ; i < m ; ++i){
        if (TOT & (1 << i)){
            checkMin(mp1[e[i].s][e[i].t] , e[i].l);
            checkMin(mp2[e[i].t][e[i].s] , e[i].l);
        }
        else{
            checkMin(mp1[e[i].s][e[i].t] , e[i].r);
            checkMin(mp2[e[i].t][e[i].s] , e[i].r);
        }
    }
    dijkstra(n , mp1 , 0 , G1 , pre);
    dijkstra(n , mp2 , 1 , G2 , pre);
    return G1[e[p].s] < INF && G2[e[p].t] < INF && G1[e[p].s] + G2[e[p].t] + e[p].l == G1[1];
}
int Case;
void solve(){
    scanf("%d%d%d" , &n , &m , &p);
    for(int i = 0 ; i < m ; ++i)
        e[i].input();
    for (int i = 0 ; i < p ; ++i){
        scanf("%d" ,&d[i]);
        d[i]--;
    }
    TAT = 1 << m;
    printf("Case #%d: " , ++Case);
    for (int i = 0 ;  i < p ; ++i){
         int now = 1 << d[i];
         bool f = false;
         for (int j = 0 ; j < TAT ; ++j)
         if (now & j){
            if (check(j , d[i])){
                f = true;
                break;
            }
         }
         if (!f){
            printf("%d\n" , d[i] + 1);
            return;
         }
    }
    puts("Looks Good To Me");
}

int main(){
    freopen("C-small-attempt0.in" , "r" , stdin);
    freopen("0.out" , "w" , stdout);
    Case = 0;
    int _;
    cin >> _;
    while(_--) solve();
}
