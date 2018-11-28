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

ll n, m;
string s;



void work() {
    cin>>s;
    n = s.length();
 //   reverse(s.begin(),s.begin()+1);
  //  cout<<s<<endl;

    int r = n-1;
    int ans = 0;
    while(r >= 0) {
        while(r>=0 && s[r] == '+') r--;
        if (r < 0) break;
        int i;
        for(i = 0;i <= r;i ++) {
            if(s[i] == '+') break;
        }
        if (i >= r) {
            cout<<ans + 1<<endl;return;
        }
//+-
        if (i == 0) {
            for(i = 0;i <= r;i ++) {
                if (s[i] == '-') break;
            }
            reverse(s.begin(),s.begin()+i);
            for(int j = 0;j < i;j ++) {
                if(s[j] == '+') s[j] = '-';
                else s[j] = '+';
            }
        }
        else {
            reverse(s.begin(),s.begin() + r + 1);
            for(int j = 0;j <= r;j ++) {
                if(s[j] == '+') s[j] = '-';
                else s[j] = '+';
            }
        }
//        cout<<s<<endl;
//
//        if(ans > 100) break;
        ans ++;
    }

    cout<<ans<<endl;

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
        work();
    }



    return 0;
}



