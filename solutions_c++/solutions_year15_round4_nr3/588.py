#include<bits/stdc++.h>
#define rep(i,s,t) for (i=(s); i<=(t); ++i)
#define dep(i,t,s) for (i=(t); i>=(s); --i)
#define sz(x) ll((x).size())
#define p(i) (1LL<<((i)-1))
#define w(x,i) ((x)&p(i))
#define fi first
#define se second
#define dll "%lld"

using namespace std;

typedef int ll;
typedef unsigned long long ull;
typedef pair<ll,ll> PII;

template<class T> inline T pr(T x) { return --x; }
template<class T> inline T nx(T x) { return ++x; }
template<class T> inline T sqr(T x) { return x*x; }

template<class T>
inline void get(T &n) {
	char c = getchar();
	while (c!='-' && (c<'0' || c>'9')) c = getchar();
	n = 0; T s = 1; if (c=='-') s = -1,c = getchar();
	while (c>='0' && c<='9') n*=10,n+=c-'0',c=getchar();
	n *= s;
}

ll T,Test;
const ll maxn = 210,maxm = 40010;
char str[1000010];
ll n,bel[maxm],sent[maxn][20],len[maxn],tmp[maxm],cnt;
string s,word;
unordered_map<string,ll> id;

int main() {
    ll i,j,k,t,tt,le,x,y,z; char c;
    scanf("%d",&Test);
    rep(T,1,Test) {
        id.clear();
        memset(tmp,0,sizeof(tmp));
        scanf("%d",&n); gets(str);
        cnt = 0;
        rep(k,1,n) {
            gets(str); s = string(str)+" ";
            le = s.length();
            tt = 0; j = 0;
            rep(i,0,le-1) if (s[i]==' ') {
                word = s.substr(j,i-j); j = i+1;
                ll &t = id[word];
                if (t==0) t = ++cnt;
                if (k==1) tmp[t] |= 1;
                else if (k==2) tmp[t] |= 2;
                else sent[k-2][++tt] = t;
            }
            if (k>2) len[k-2] = tt;
        }
        ll ans = cnt;
        for (x=0; x<(1<<(n-2)); ++x) {
            rep(i,1,cnt) bel[i] = tmp[i];
            rep(i,1,n-2)
                rep(j,1,len[i])
                    bel[sent[i][j]] |= 1<<((x>>(i-1))&1);
            t = 0;
            rep(i,1,cnt) if (bel[i]==3) ++t;
            ans = min(ans,t);
        }
        printf("Case #%d: %d\n",T,ans);
    }

    return 0;
}
