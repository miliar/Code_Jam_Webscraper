#include <bits/stdc++.h>
using namespace std;

#define rep(i,n) for(int i=0;i<(n);++i)
#define lfo(i,a,b) for(int i=(a),_b=(b);i<=_b;++i)
#define rfo(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define lfoe(i,v) for(typeof((v).begin()) i = (v).begin(); i != (v).end(); ++i)
#define st first
#define sz(s) (int)(s.size())
#define nd second
#define pb push_back

template<class F, class T> T convert(F a, int p = -1) { stringstream ss; if (p >= 0) ss << fixed << setprecision(p); ss << a; T r; ss >> r; return r; }
template<class T> T gcd(T a, T b) { T r; while (b != 0) { r = a % b; a = b; b = r; } return a; }
template<class T> T lcm(T a, T b) { return a / gcd(a, b) * b; }
typedef long long ll;
typedef pair<int,int> II;
const int oo=int(1e9)+7;
const int dx[]={1,0,0,-1};
const int dy[]={0,-1,1,0};
const int N=int(1e6)+10;

struct nod{
    int n['z'-'a'+1];
    nod(){memset(n,0,sizeof n);}
};
struct trie{
    vector<nod> a;
    trie(){a.push_back(nod());}
    void rs(){a.clear();a.push_back(nod());}
    void add(const string &s){
        int r=0;
        rep(i,sz(s)){
            if (!a[r].n[ s[i]-'A' ]){
                a[r].n[ s[i]-'A' ]=sz(a);
                a.push_back(nod());
            }
            r=a[r].n[ s[i]-'A' ];
        }
    }
    int get(){
        return sz(a);
    }
};
int tc,n,m,ans,wor;
vector<string> v;
string s;
vector<int> ch;
vector<trie> vkl;

int main(){
    freopen("a.inp","r",stdin);
    freopen("a.out","w",stdout);
    ios::sync_with_stdio(false);
    //scanf("%d",&tc);
    vkl.resize(2);
    rep(i,2) vkl[i].rs();
    cin>>tc;
    lfo(tt,1,tc){
        cin>>m>>n;
        v.clear();
        rep(i,m){
            cin>>s;
            v.push_back(s);
        }
        vkl.resize(n);
        ans=0;wor=0;
        int pp=1;
        rep(i,m) pp*=n;
        for(int ms=0;ms<pp;++ms){
            ch.clear();
            int dp=ms;
            vector<int> dem(n,0);
            rep(i,m) {ch.push_back(dp%n);dp/=n;dem[ch.back()]++;}
            bool ok=false;
            rep(i,n) if (dem[i]==0) ok=true;
            if (ok) continue;
            for(int i=0;i<n;++i) vkl[i].rs();
            rep(i,m) vkl[ ch[i] ].add(v[i]);
            dp=0;
            rep(i,n) dp+=vkl[i].get();
            if (dp>wor) wor=dp,ans=1;
            else if (dp==wor) ans++;
        }
        //printf("Case #%d: \n",tt);
        cout<<"Case #"<<tt<<": "<<wor<<' '<<ans<<'\n';
    }
    return 0;
}
