#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
const double pi = acos(-1.0);
const double eps = 1e-8;
//const ll INF=(_I64_MAX)/2;
//#pragma comment(linker, "/STACK:102400000,102400000")
const int inf = 0x3f3f3f3f;
#define maxx(a) memset(a, 0x3f, sizeof(a))
#define minn(a) memset(a, 0xC0, sizeof(a))
#define zero(a) memset(a, 0, sizeof(a))
#define FILL(a,b) memset(a, b, sizeof(a))
#define REP(i,a,b) for(i=a;i<b;i++)
#define rep(i,n) REP(i,0,n)
#define srep(i,n) for(i = 1;i <= n;i ++)
#define MP make_pair
#define fi first
#define se second
typedef pair <int, int> PII;
typedef pair <ll , ll > PX ;

const int N = 2000 + 11;

vector<int > G[N];

ll n, m, x;
int a[111];

void fk(ll b) {
    if(b==0)return;
    while(b) {
        if(!a[b%10]) {
            a[b%10] = 1;
            x++;
        }
        b /= 10;
    }
}

void work() {
    int i,j;
    zero(a);
    x=0;
    m = n;
    for(i=1;i<=1000010;i++) {
        fk(m);
        if(x == 10) {
            cout<<m<<endl;return;
        }
        m += n;
    }
    cout<<"INSOMNIA"<<endl;
}

int main() {
#ifdef LOCAL
    freopen( "in.txt", "r" , stdin);
 freopen ("out.txt","w",stdout );
#endif

    int T,cas=1;
    cin>>T;
    while(T--) {
        printf("Case #%d: ",cas++);
        cin>>n;
        work();
    }



    return 0;
}



