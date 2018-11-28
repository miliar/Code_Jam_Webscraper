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
#define rep(i,a,b)  for(int (i)=(a);(i)<=(b);(i)++)
#define rp(i,n) for(int i=0;i<n;i++)
#define repp(i,a,b,c) for(int i=a;(c>0)?(i<=b):(i>=b);i+=c)
#define isf(x) int x;sf(x);
#define STOP  system("pause")
#define PP printf(" ")
#define mem(x,y) memset(x,y,sizeof(x))
#define LN printf("\n");
#define du freopen("in.txt","r",stdin)
#define chu freopen("out.txt","w",stdout)
#define EPS 1e-8

//--------------

//--------
#define FI first
#define SE second
#define PB push_back
#define MP(a,b) make_pair(a,b)
#define VIS vector<string>
#define SZ(x) int(x.size())
#define feach(i,x) for(__typeof(x.begin()) i=x.begin();i!=x.end();++i)
#define ALL(x) x.begin(),x.end()
template<class T> inline void CLR(T &A) {A.clear();}
#define DO(n) while(n--)
#define DO_C(n) int n____=n;while(n____--)
//----------
typedef long long LL;
inline bool insize(int c,int l,int r){if (c>=l&&c<=r) return true; return false;}
template<class T> inline void checkmin(T &a,T b){if(a == -1 || a > b)a = b;}
template<class T> inline void checkmax(T &a,T b){if(a < b)    a = b;}
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef pair<int ,int> II;
typedef queue<int> QI;

int dx[] = {0,1,0,-1, 1, 1, -1, -1};//up Right down Left
int dy[] = {1,0,-1,0, 1, -1, 1, -1};
int sig(double x){return fabs(x-0)<EPS?0:x>0?1:-1;}
template<class T> inline void sf(T& x){
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
    while((c = getchar()))
    {
        if(c >= '0' && c <= '9')
        {
            x = (x<<1)+(x<<3)+(c-'0');
        }
        else break;
    }
    x *= mul;
}
template<class T0, class T1> inline void sf(T0& x, T1& y) {sf(x);sf(y);}
template<class T0, class T1, class T2> inline void sf(T0& x, T1& y, T2& z) {sf(x);sf(y);sf(z);}
// mem 127, 0x7f => 2139062143 => 0x7F7F7F7F
// mem  63, 0x3f => 1061109567 => 0x3f3f3f3f
// mem 255, 0xff => -1
const int N=1005;       // 点数
const int E=200055;   //边数
const int INF= 0x3f3f3f3f;
const long long  LINF= 0x3F3F3F3F3F3F3F3FLL;


int a[N], b[N], n;

void init(){
    sf(n);
    rp(i,n){
        double x; 
        cin>> x;
        a[i] = x*100000;
    }
    rp(i,n){
        double x;
        cin>> x;
        b[i] = x*100000;
    }

    sort(a,a+n);
    sort(b,b+n);
}

int sol1(){
    int ans = 0;
    int la =0 , lb =0 , ra = n-1, rb = n-1;
    rp(i,n){
        // printf("%d-th\n", i);
        if (a[la]>b[lb]){
            // printf("A %d  B %d\n", a[la], b[lb]);
            la++;
            lb++;
            ans++;

        } else {
            // printf("A %d  B %d\n", a[la], b[rb]);
            la++;
            rb--;
        }

    }

    return ans;
}

// War Game
int sol2(){
    // puts("A[] :");
    // rp(i,n){
    //     printf("%d ", a[i]);
    // }
    // puts("");
    // puts("B[] :");
    // rp(i,n){
    //     printf("%d ", b[i]);
    // }
    // puts("");

    set<int> sa, sb;
    sa.clear(); sb.clear();
    rp(i,n) sb.insert(b[i]);
    int ans = 0;

    rp(i,n){
        int val = a[i];
        set<int>::iterator it = sb.upper_bound(val);
        // printf("%d -th A val: %d ", i+1, val);

        if (it == sb.end()){
            // printf(" B val: %d  Win\n", *(sb.begin()));
            sb.erase(sb.begin());
            ans++;
        } else {
            // printf("B val: %d   Lose\n", *(it));
            sb.erase(it);
        }

        // puts("");

    }

    return ans;
}

int main(){
    // du;
    // chu;
    // freopen("D-large.in","r",stdin);
    isf(t);
    rep(ica, 1, t){
        init();
        printf("Case #%d: %d %d\n", ica, sol1(), sol2());
    }


}