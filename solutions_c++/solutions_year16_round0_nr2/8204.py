#include <bits/stdc++.h>
using namespace std;
#define dprint(v) cerr << #v"=" << v << endl //;)
#define forr(i,a,b) for(int i=(a); i<(b); i++)
#define forn(i,n) forr(i,0,n)
#define dforn(i,n) for(int i=n-1; i>=0; i--)
#define forall(it,v) for(auto it=v.begin();it!=v.end();++it)
#define sz(c) ((int)c.size())
#define zero(v) memset(v, 0, sizeof(v))
#define pb push_back
#define fst first
#define snd second
typedef long long ll;
typedef pair<int,int> ii;

const int MAXN=12;
int n;
string s;
int vis[1<<MAXN];

int asd[MAXN];

void print(){
    forn(i, n) cout << (asd[i]?'+':'-');
}
int greedy(int bms, int n){
    forn(j, n) asd[j]=(bms>>j)&1;
    int step=0;
    while(n){
        while(n && asd[n-1]==1) n--;
        if(!n) break;
        int b=-1;
        int kb=0;
        print();
        forn(i, n){
            int k=0;
            while(i+k<n && asd[i+k]==1) k++;
            dprint(i);
            dprint(k);
            if(kb<k) kb=k, b=i;
        }
        if(b==-1) return step+1;
        int i=b+kb;
        for(int j=0; j<i/2; j++){
            swap(asd[j], asd[i-1-j]);
            asd[j]^=1;
            asd[i-1-j]^=1;
        }
        if(i&1) asd[i/2]^=1;
        step++;
        while(n && asd[n-1]==1) n--;
        if(!n) break;
        i=n;
        for(int j=0; j<i/2; j++){
            swap(asd[j], asd[i-1-j]);
            asd[j]^=1;
            asd[i-1-j]^=1;
        }
        if(i&1) asd[i/2]^=1;
        step++;
        
    }
    return step;
}

int solve(int bms, int n){
    queue<int> qu;
    qu.push(bms);
    memset(vis, -1, sizeof(vis));
    vis[bms]=0;
    while(sz(qu)){
        int bm=qu.front(); qu.pop();
        if(bm==(1<<n)-1) break;
        forr(i, 1, n+1){
            forn(j, n) asd[j]=(bm>>j)&1;
            for(int j=0; j<i/2; j++){
                swap(asd[j], asd[i-1-j]);
                asd[j]^=1;
                asd[i-1-j]^=1;
            }
            if(i&1) asd[i/2]^=1;
            int bm2=0;
            forn(i, n) bm2|=asd[i]<<i;
            if(vis[bm2]==-1){
                vis[bm2]=1+vis[bm];
                qu.push(bm2);
            }
        }
    }
    return vis[(1<<n)-1];
}


int main() {
    //~ freopen("input.in", "r", stdin);
    freopen("B-small-attempt0.in", "r", stdin);
    //~ freopen("B-large.in", "r", stdin);
    freopen("asd.out", "w", stdout);
    ios::sync_with_stdio(0);
    int TC; cin >> TC;
    for(int TT=1; TT<=TC; TT++){
        cout << "Case #" << TT << ": ";
        cin >> s;
        n=sz(s);
        int bms=0;
        forn(i, n) bms|=(s[i]=='+')<<i;
        //~ cout << solve(bms, n);
        cout << solve(bms, n);
        
        cout << endl;
    }
    return 0;
}
