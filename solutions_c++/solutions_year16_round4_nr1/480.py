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

int r,p,s,n;
string c[3]={"R","P","S"};
int ans[3];
string dfs(int nn,int id) {
    if (nn == 1) {
        string zz;
        if (c[id] < c[(id+1)%3]) {
        ans[id]++;
        zz+=c[id];
        ans[(id+1)%3]++;
        zz += c[(id+1)%3];
        }
        else {
            ans[(id+1)%3]++;
            zz += c[(id+1)%3];
            ans[id]++;
            zz+=c[id];
        }
        return zz;
    }
    else{
        string a,b;
        if (c[id] < c[(id+1)%3]) {
            a=dfs(nn-1,id);
                    b=dfs(nn-1,(id+1)%3);
        }
        else{
            a=dfs(nn-1,(id+1)%3);
            b=dfs(nn-1,id);

        }
        if(a<b)return a+b;
        else return b+a;
    }
}


void work() {
    cin>>n>>r>>p>>s;
    zero(ans);
    string k;
    k=dfs(n,0);
    if (r == ans[0] && p == ans[1] && s == ans[2]) {
        cout<<k<<endl;return;
    }
    zero(ans);
    k=dfs(n,1);
    if (r == ans[0] && p == ans[1] && s == ans[2]) {
        cout<<k<<endl;return;
    }
    zero(ans);
    k=dfs(n,2);
    if (r == ans[0] && p == ans[1] && s == ans[2]) {
        cout<<k<<endl;return;
    }
    puts("IMPOSSIBLE");

}

int main() {
#ifdef LOCAL
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
#endif


    int T, cas = 1;
    cin >> T;
    while (T--) {
        printf("Case #%d: ", cas++);
        work();
    }

    return 0;
}



