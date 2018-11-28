#include    <bits/stdc++.h>

#define     M_PI            3.14159265358979323846
#define     mod             1000000007
#define     inf             1000000000000000000
#define     mp              make_pair
#define     pb              push_back
#define     F               first
#define     S               second
#define     ll              long long
#define     pii             pair<int,int>
#define     pli             pair<ll,int>
#define     pil             pair<int,ll>
#define     pll             pair<ll,ll>
#define     si(t)           scanf("%d",&t)
#define     sii(m,n)        scanf("%d %d",&m,&n);
#define     sl(t)           scanf("%lld",&t)
#define     rep(i,n)        for(int i=0;i<n;i++)
#define     REP(i,a,b)      for(int i=a;i<=b;i++)
#define     RREP(i,a,b)     for(int i=a;i>=b;i--)
#define     N               100005

using namespace std;

string ss;

pair<string ,int > fun2(pair<string ,int > a,pair<string ,int > b){
    int c;
    if(a.S == 1 && b.S == 2 || a.S == 2 && b.S == 1) c = 1;
    else if(a.S == 1 && b.S == 3 || a.S == 3 && b.S == 1) c = 3;
    else if(a.S == 2 && b.S == 3 || a.S == 3 && b.S == 2) c = 2;
    string pp;
    if(a.F < b.F) pp = a.F , pp.append(b.F);
    else pp = b.F , pp.append(a.F);
    return mp(pp,c);
}

void fun(map<pair<string ,int > , int > m){
    if(m.size() == 1){
        if((*m.begin()).S == 1){
            ss = (*m.begin()).F.F;
        }
        else ss = "IMPOSSIBLE";
        return;
    }
    int mx = -1;
    pair<string ,int > a,b,c;
    map<pair<string ,int > , int >::iterator it;
    for(it = m.begin() ; it != m.end() ; it++){
        if(it->S > mx){
            a = it->F;
            mx = it->S;
        }
    }
    int f=0;
    for(it = m.begin() ; it != m.end() ; it++){
        if(it->F !=  a){
            if(!f) b = it->F , f=1;
            else c = it->F , f=2;
        }
    }
    map<pair<string ,int > , int > temp;
    if(m.size() == 2){
        if(m[a] != m[b]){ss = "IMPOSSIBLE" ; return ;}
        else{
            temp[fun2(a,b)] = m[a];
        }
        fun(temp);
        return ;
    }
    else if(m[a] > m[b] + m[c]) {ss = "IMPOSSIBLE" ; return ;}
    
    while(m[a] != m[b] + m[c]){
        temp[fun2(b,c)]++;
        m[b]--;m[c]--;
    }
    temp[fun2(a,c)] = m[c];
    temp[fun2(a,b)] = m[b];
    fun(temp);
}

int main(){
    int t; si(t);
    REP(T,1,t){
        int n,p,r,s;
        sii(n,r); sii(p,s);
        map<pair<string ,int > , int > m;
        if(p != 0) m[mp("P" , 1)] = p;
        if(r != 0) m[mp("R" , 2)] = r;
        if(s != 0) m[mp("S" , 3)] = s;
        fun(m);
        printf("Case #%d: ",T);
        cout << ss;
        printf("\n");
    }
    return 0;   
}

