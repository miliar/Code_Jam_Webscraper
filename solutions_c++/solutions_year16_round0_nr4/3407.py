/** ========================================**
 ** Bismillahi-Rahamanirahim.
 ** @Author: A Asif Khan Chowdhury
/** ========================================**/

#include <bits/stdc++.h>

using namespace std;

#define Set(N, j) (N|(1<<j))
#define reset(N, j) (N&~(1<<j))
#define Check(N, j) (bool)(N&(1<<j))
#define toggle(N, j) (N^(1<<j))
#define turnOff(N, j) (N & ~(1<<j))
#define CLEAR(A, x) ( memset(A,x,sizeof(A)) )
#define pii pair <int, int>
#define pb push_back
#define open freopen("D:/a.txt", "r", stdin);
#define write freopen("D:/b.txt","w", stdout);
#define inf (1ll<<28)
#define ll long long
#define mod 1000000007
#define gc getchar
#define ls(n) (n<<1)
#define rs(n) ls(n)|1
#define MID(a,b) ((a+b)>>1)
#define fs first
#define sc second
#define mx 100010

template<class T>inline bool read(T &x) {
    int c=getchar();
    int sgn=1;
    while(~c&&c<'0'||c>'9') {
        if(c=='-')sgn=-1;
        c=getchar();
    }
    for(x=0; ~c&&'0'<=c&&c<='9'; c=getchar())x=x*10+c-'0';
    x*=sgn;
    return ~c;
}
//int X[]= {-1, -1, -1, 0, 1, 1, 1, 0};   //x 8 direction
//int Y[]= {-1, 0, +1, 1, 1, 0, -1, -1};  //y 8 direction
int X[]= {-1, 0, 1, 0};   //x 4 direction
int Y[]= { 0, 1, 0, -1};  //y 4 direction

ll k,c,s;
ll Pow(ll a, ll b){
    ll ret=1;
    for(int i=1;i<=b;i++)ret*=a;
    return ret;
}

//vector<ll>op;

int main() {
#ifdef LOCAL
    freopen("a.in", "r", stdin);
    freopen("b.out","w",stdout);
#endif // LOCAL

    int test;
    read(test);
    for(int C=1; C<=test; C++) {
        printf("Case #%d:", C);
//        op.clear();
        read(k);read(c);read(s);
//        ll gap = Pow(k,c);
        for(ll i=1;i<=s;i++){
//            op.push_back(1ll+gap*i);
            printf(" %lld",i);
        }
        puts("");
//        for()
    }

    return 0;
}
