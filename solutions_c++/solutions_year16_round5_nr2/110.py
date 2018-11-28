#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <stack>
#include <queue>
using namespace std;

#define rep(i,n) for (int i=1;i<=(n);++i)
#define rep2(i,x,y) for (int i=(x);i<=(y);++i)
#define pb push_back
#define mp make_pair
typedef long long LL;
typedef vector<int> VI;
typedef pair<int,int> PII;
typedef vector<PII> VII;

int a[200];
string b[200];
char s[200][200];
int mynext[200][200],cur[200];
int p[200];
int n,m;
int f[1000000][3];
const int inf =100000000;
stack<char> st;
vector<int> g[200];
bool exist[200];
bool gone[200];
int sz[200],cnt[200];
void dfs(int t){
    gone[t]=false;
    sz[t]=1;
    for (int x:g[t]){
        if (gone[x]){
            dfs(x);
            sz[t]+=sz[x];
        }
    }
}
string str;
void MAIN(){
    cin >> n;
    rep(i,n) g[i].clear();
    rep(i,n) cin >> a[i];
    cin >> str;
    rep(i,n) g[a[i]].pb(i);
    rep(i,n) gone[i]=true;
    rep(i,n)
        if (a[i]==0)
            dfs(i);
    cin >> m;
    rep(i,m) cin >> b[i];
    rep(i,m) rep(j,b[i].length()) s[i][j]=b[i][j-1];
    rep(i,m){
        mynext[i][1]=0; int j=0;
        rep2(k,2,b[i].length()){
            while (j>0 && s[i][k]!=s[i][j+1]) j=mynext[i][j];
            if (s[i][k]==s[i][j+1]) j++;
            mynext[i][k]=j;
        }
    }
    rep(i,m) cnt[i]=0;
    const int RNDTIME = 100000;
    rep(round,RNDTIME){
        vector<int> clist;
        rep(i,n)
            if (a[i]==0){
                clist.pb(i);
            }
        rep(i,m) exist[i]=false;
        rep(i,m) cur[i]=0;
        rep(i,n){
            int rnd=rand()%(n-i+1)+1;
            int t;
            for(auto lnk=clist.begin();lnk!=clist.end();++lnk){
                rnd-=sz[*lnk];
                if (rnd<=0){
                    t=*lnk;
                    clist.erase(lnk);
                    break;
                }
            }
            //cout << str[t-1] << endl;
            rep(j,m){
                while (cur[j]>0 && s[j][cur[j]+1]!=str[t-1]) cur[j]=mynext[j][cur[j]];
                if (s[j][cur[j]+1]==str[t-1]) ++cur[j];
                if (cur[j]==b[j].length()){
                    exist[j]=true;
                    cur[j]=0;
                }
            }
            for (auto j:g[t])
                clist.pb(j);
        }
        rep(i,m) if (exist[i]){
                cnt[i]++;
            }
    }
    rep(i,m) cout << cnt[i]*1.0/RNDTIME << " "; cout << endl;
}

int main() {
    freopen("d:\\oi\\gcjr3\\B-small-attempt0.in","r",stdin);
    freopen("d:\\oi\\gcjr3\\B-small-attempt0.out","w",stdout);
    int tt;
    cin >> tt;
    rep(i,tt)
    {
        printf("Case #%d: ",i);
        MAIN();
    }
    return 0;
}