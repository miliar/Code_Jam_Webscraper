/*lcf*/


#include<stdio.h>
#include<string.h>
#include<ctype.h>
#include<stdlib.h>
#include<cmath>


#define FO(i,s,e,p) for(int i=(s);i<int(e);i+=p)
#define FOD(i,s,e,p) for(int i=(s);i>int(e);i-=p)


#define FOR(i,s,e) FO(i,s,e,1)
#define FORE(i,s,e) FOR(i,s,e+1)
#define FORD(i,s,e) FOD(i,s,e,1)
#define FORDE(i,s,e) FORD(i,s,e-1)

#define ALL(i,s) for(__typeof((s).begin()) i=(s).begin();i!=(s).end();i++)

#define MEM(tab,fill) memset(tab,fill,sizeof(tab))

#include<iostream>
#include<set>
#include<vector>
#include<string>
#include<sstream>
#include<stack>
#include<queue>
#include<algorithm>
#include<utility>
#include<bitset>
#include<map>
#include<cassert>
#define pb push_back
#define ll long long
using namespace std;

#define EPS 0.0000001
#define MOD 1000000007
#define mp make_pair
#define fi first
#define se second
#define inf (1<<29)
const int SZ=100100;
const int LG=18;

vector<int> g[SZ];
int up[SZ][LG];
int sz[SZ];
int in[SZ],out[SZ];

bool isup(int a,int b){
    return in[a]<=in[b] && out[a]>=out[b];
}
int cl=1;
void dfs(int on,int p=1)
{
    in[on]=cl++;
    up[on][0]=p;
    FOR(i,1,LG) up[on][i]=up[up[on][i-1]][i-1];

    sz[on]=1;
    ALL(i,g[on]) if(*i!=p) dfs(*i,on),sz[on]+=sz[*i];
    out[on]=cl++;
}
void pre(){
    dfs(1);
}

struct stt{
    vector<int> IN;
    stt(int szz){IN.resize(szz+4,0);}
    int get(int idx){
        int ret=0;
        for(;idx;idx^=(idx&-idx)) ret+=IN[idx];
        return ret;
    }
    void upd(int idx,int v){
        for(;idx<IN.size();idx+=(idx&-idx)) IN[idx]+=v;
    }
    void upd(int a,int b,bool x){
        upd(a,1);upd(b+1,-1);
    }

};
stt *al[SZ];

int ID[SZ];
int sppar[SZ];

int trbul(int on,int pp,bool ki){
     if(ki==0) cl=1;

     if(ki==1) sppar[on]=sppar[pp];
     else sppar[on]=on;

     ID[on]=cl++;
     int sul=1;

     int mx=0;

     ALL(i,g[on]) if(*i!=pp) mx=max(mx,sz[*i]);
     ALL(i,g[on]) if(*i!=pp)
        if(sz[*i]==mx && 2*mx>=sz[on]) sul+=trbul(*i,on,1);
     ALL(i,g[on])if(*i!=pp)
        if(!(sz[*i]==mx && 2*mx>=sz[on])) trbul(*i,on,1);

    if(!ki) al[on]=new stt(sul);
    return sul;
}

void buld(){
    trbul(1,-1,0);
}
int lcs(int a,int b){
    FORDE(i,LG-1,0) if(!isup(up[b][i],a)) b=up[b][i];
    if(!isup(b,a)) b=up[b][0];
    return b;
}

void UPD(int super,int on){
    while(!isup(sppar[on],super)){
        al[ID[sppar[on]]]->upd(ID[sppar[on]]+1,ID[on]);
        on=up[sppar[on]][0];
    }
    if(on!=super)
     al[ID[sppar[on]]]->upd( ID[super]+1,ID[on] );
}



int main(){

    freopen("C:\\a","r",stdin);
    int n,q;cin>>n>>q;
    FOR(i,1,n){
        int a,b;cin>>a>>b;
        g[a].pb(b);g[b].pb(a);
    }
    pre();
    buld();

    while(q--){
        char c;
        while(isspace(c=getchar()));
        int a,b;cin>>a>>b;
        if(c=='P'){
            int lc=lcs(a,b);
            if(isup(b,a)) swap(b,a);
            if(lc==a || lc==b) UPD(a,b);
            else UPD(lc,a),UPD(lc,b);
        }else{
            if(up[a][0]==b) swap(a,b);
            cout<<al[sppar[b]]->get(ID[b])<<endl;
        }
    }


   return 0;
}
