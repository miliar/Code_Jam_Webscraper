/*
http://codingaquarium.wordpress.com/
Shaikh shiam Rahman
Khunla University of Engineering and Technology(KUET)

*/

#include <bits/stdc++.h>
using namespace std;

/*** typedef ***/

#define MEMSET_INF 127
#define MEMSET_HALF_INF 63
#define stream istringstream
#define rep(i,n) for(__typeof(n) i=0; i<(n); i++)
#define repl(i,n) for(__typeof(n) i=1; i<=(n); i++)
#define FOR(i,a,b) for(__typeof(b) i=(a); i<=(b); i++)
#define INF (1<<30)
#define PI acos(-1.0)
#define pb push_back
#define ppb pop_back
#define all(x) x.begin(),x.end()
#define mem(x,y) memset(x,y,sizeof(x))
#define memsp(x) mem(x,MEMSET_INF)
#define memdp(x) mem(x,-1)
#define memca(x) mem(x,0)
#define eps 1e-9
#define ii pair<int,int>
#define pmp make_pair
#define ft first
#define sd second
#define vi vector<int>
#define vii vector<ii>
#define si set<int>
#define msi map<string , int >
#define mis map<int , string >
typedef long long i64;
typedef unsigned long long ui64;

/** function **/

#define SDi(x) sf("%d",&x)
#define SDl(x) sf("%lld",&x)
#define SDs(x) sf("%s",x)
#define SD2(x,y) sf("%d%d",&x,&y)
#define SD3(x,y,z) sf("%d%d%d",&x,&y,&z)
#define pf printf
#define sf scanf
#define pfcas(x) pf("Case %d: ",x)

#define READ(f) freopen(f, "r", stdin)
#define WRITE(f) freopen(f, "w", stdout)
#define MAX 20010

int main (int argc, char **argv) {
#ifndef ONLINE_JUDGE
    READ("input.txt");
    WRITE("out.txt");
//    cout<<"hello world!"<<endl;
#endif
    int tc,cas=0,ans1,ans2,a[5][5],b[5][5];
    SDi(tc);
    while(tc--){
        pf("Case #%d: ",++cas);
        SDi(ans1);
        rep(i,4) rep(j,4) SDi(a[i][j]);
        SDi(ans2);
        rep(i,4) rep(j,4) SDi(b[i][j]);
        int cnt=0,ans;
        rep(i,4) rep(j,4){
            if(a[ans1-1][i]==b[ans2-1][j]){
                cnt++;
                ans = a[ans1-1][i];
            }
        }
        if(cnt==0) puts("Volunteer cheated!");
        else if(cnt==1) pf("%d\n",ans);
        else puts("Bad magician!");
    }
    return 0;
}
