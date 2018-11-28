#include <ctime>
#include <iostream>
#include <fstream>
#include <cstring>
#include <algorithm>
#include <queue>
#include <cmath>
#include <map>
#include <set>
#include <bitset>
#include <stack>
#include <deque>
#include <assert.h>

using namespace std;
#define BUG1 puts("BUG11\n")
#define BUG2 puts("BUG22\n")
#define rep(i,a,b) for(int (i)=(a);(i)<=(b);(i)++)
#define rp(i,a) for(int i=0;i<a;i++)
#define FD(i,a,b) for(int i=a;i>=b;i--)
#define STOP  system("pause")
#define PP printf(" ")
#define mem(x,y) memset(x,y,sizeof(x))
#define LN printf("\n");
#define du freopen("in.txt","r",stdin)
#define chu freopen("out.txt","w",stdout)
#define EPS 1e-8

#define FI first
#define SE second
#define PB push_back
#define MP make_pair


typedef long long LL;
inline int dblcmp(double x) { return fabs(x)<EPS?0:x>0?1:-1; }
inline bool insize(int c,int l,int r){if (c>=l&&c<=r) return true; return false;}
template<class T> inline void checkmin(T &a,T b)	{if(a == -1 || a > b)a = b;}
template<class T> inline void checkmax(T &a,T b)	{if(a < b)	a = b;}
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef pair<int ,int> II;

int dx[] = {0,1,0,-1};//up Right down Left
int dy[] = {1,0,-1,0};
template<class T> inline void sf(T& x)
{
    char c;
    int mul = 1;
    while((c = getchar()) != EOF)
    {
        if(c == '-')mul = -1;
        if(c >= '0' && c <= '9')
        {
            x = c-'0';
            break;
        }
    }
    if(c == EOF){x = EOF;return;}
    while(c = getchar())
    {
        if(c >= '0' && c <= '9')
        {
            x = (x<<1)+(x<<3)+(c-'0');
        }
        else break;
    }
    x *= mul;
}

const int N= 50005;       // 点数
const int E=200555;   //边数
const int INF= 0x3f3f3f3f;
const long long  LINF= 0x3F3F3F3F3F3F3F3FLL;


int ch[103][103];
int n, m;

bool calc(int x, int y){
    bool res = 1;
    rep(j,0,m-1)
        if (ch[x][j] > ch[x][y]){
            res = 0;
            break;
        }
    if (res)
        return 1;
    res = 1;
    rep(i,0,n-1)
        if (ch[i][y] > ch[x][y]){
            res = 0;
            break;
        }
    if (res)
        return 1;
    return 0;
}
int main(){
    du;chu;
    int t;
    sf(t);
    for (int cas = 1; cas <= t; cas++){
        sf(n); sf(m);
        rep(i,0,n-1) rep(j,0,m-1)
                sf(ch[i][j]);

        bool res = 1;
        rep(i,0,n-1){
            if (!res)   break;
            rep(j,0,m-1){
                if (!calc(i, j)){
                    res = false;
                    break;
                }
            }
        }
        if (res){
            printf("Case #%d: YES\n", cas);
        }
        else{
            printf("Case #%d: NO\n", cas);
        }
    }
	return 0;
}

