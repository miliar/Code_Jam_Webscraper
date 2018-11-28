/**
 * Author : Parachvte (ryannx6@gmail.com)
 * Date   : 05/01/2016
 */

#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <utility>
#include <cstring>
#include <string>
#include <vector>
#include <map>

using namespace std;

#define range(i, a, b) for (int i = (a), _end_ = (b); i <= _end_; ++i)
#define rep(i, n) for (int i = (0), _end_ = (n); i < _end_; ++i)
#define pb push_back
#define mp make_pair
#define INF 1000000000
#define MOD 1000000007
#define EPS 1e-6

typedef long long LL;
typedef pair<int, int> PII;
typedef vector<int> VI;
typedef vector<PII> VII;

#define INF 1000000000
#define MOD 1000000007
#define EPS 1e-6

string C,J,CC,JJ,CCC,JJJ;
int len;
LL ans,pow;

LL get_max(LL a,LL pow){
    return a + pow - 1;
}
LL get_min(LL a,LL pow){
    return a;
}

bool check(LL a,LL b,LL pow){
    return get_min(a,pow)-get_max(b,pow)<ans || get_min(b,pow)-get_max(a,pow)<ans;
}

void dfs(int dep,LL a,LL b,LL pow){
    if (dep==len){
        LL now=max(a,b)-min(a,b);
        if (now<ans){
            ans=now;
            CCC=CC;
            JJJ=JJ;
        }
        return;
    }
    LL aa=a,bb=b;
    if (C[dep]!='?') aa+=pow*(C[dep]-'0');
    if (J[dep]!='?') bb+=pow*(J[dep]-'0');
    if (C[dep]!='?'){
        if (J[dep]!='?')
            dfs(dep+1,aa,bb,pow/10);
        else {
            for (int i=0;i<=9;i++){
                bb=b+pow*i;
                JJ[dep]='0'+i;
                if (!check(aa,bb,pow)) continue;
                dfs(dep+1,aa,bb,pow/10);
            }
        }
    }else{
        if (J[dep]!='?'){
            for (int i=0;i<=9;i++){
                aa=a+pow*i;
                CC[dep]='0'+i;
                if (!check(aa,bb,pow)) continue;
                dfs(dep+1,aa,bb,pow/10);
            }
        }else{
            for (int i=0;i<=9;i++){
                for (int j=0;j<=9;j++){
                    aa=a+pow*i;
                    bb=b+pow*j;
                    CC[dep]='0'+i;
                    JJ[dep]='0'+j;
                    if (!check(aa,bb,pow)) continue;
                    dfs(dep+1,aa,bb,pow/10);
                }
            }
        }
    }
}

void solve(){
    cin>>C>>J;
    CC=C;
    JJ=J;
    len=(int)C.length();

    ans = 1000000000000000000L;
    pow = 1;
    for (int i=0;i<len-1;i++) pow*=10;
    dfs(0,0,0,pow);
//    cout<<ans<<endl;
    cout<<CCC<<" "<<JJJ<<endl;
}

int main() {
#ifdef DEBUG
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    std::ios_base::sync_with_stdio(false);

    int T;
    cin >> T;
    for (int i=1;i<=T;i++){
        printf("Case #%d: ",i);
        solve();
    }

    return 0;
}
