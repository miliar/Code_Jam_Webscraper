#include <bits/stdc++.h>
#define pb push_back
#define sqr(x) (x)*(x)
#define sz(a) int(a.size())
#define reset(a,b) memset(a,b,sizeof(a))
#define oo 1000000007

using namespace std;

typedef pair<int,int> pii;
typedef pair<int,pii> iii;
typedef long long ll;


string dp[13][3];
int layer,P,R,S;

string get(int layer, char x){
    if(layer==0){
        string res="";
        res+=x;
        return res;
    }
    int id;
    if(x=='P') id=0;
    else if(x=='R') id=1;
    else id=2;

    if(dp[layer][id]!="") return dp[layer][id];
    string s1,s2;
    if(x=='P'){
        s1 = get(layer-1,'P');
        s2 = get(layer-1,'R');
    }else if(x=='R'){
        s1 = get(layer-1,'R');
        s2 = get(layer-1,'S');
    }else{
        s1 = get(layer-1,'S');
        s2 = get(layer-1,'P');
    }
    if(s1>s2) swap(s1,s2);
    string res=s1+s2;
    dp[layer][id]=res;
    return res;
}

bool check(int layer, int P, int R, int S, char x){
    string s=get(layer,x);
    for(int i=0; i<sz(s); ++i){
        if(s[i]=='P') --P;
        else if(s[i]=='R') --R;
        else --S;
    }
    return P==0 && R==0 && S==0;
}

int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int T;
    scanf("%d",&T);
    for(int tt=1; tt<=T; ++tt){
        scanf("%d%d%d%d",&layer,&R,&P,&S);
        printf("Case #%d: ",tt);
        string res="Z";
        if(check(layer,P,R,S,'P')) res=min(res,get(layer,'P'));
        if(check(layer,P,R,S,'S')) res=min(res,get(layer,'S'));
        if(check(layer,P,R,S,'R')) res=min(res,get(layer,'R'));
        if(res=="Z")
            puts("IMPOSSIBLE");
        else printf("%s\n",res.c_str());
    }
}

