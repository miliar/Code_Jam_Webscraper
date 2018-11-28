#include <bits/stdc++.h>

using namespace std;

#define mp make_pair
#define pb push_back
#define rep(i,n) for( int i = 0; i < (n); i++ )
#define fi first
#define se second

const int MXN = 10010;

pair<char,int> mul( pair<char,int> a, pair<char,int> b ){
    pair<char,int> res;
    if(a.fi=='1' && b.fi=='1') res = mp('1',0);
    if(a.fi=='i' && b.fi=='i') res = mp('1',1);
    if(a.fi=='j' && b.fi=='j') res = mp('1',1);
    if(a.fi=='k' && b.fi=='k') res = mp('1',1);

    if(a.fi=='i' && b.fi=='1') res = mp('i',0);
    if(a.fi=='j' && b.fi=='i') res = mp('k',1);
    if(a.fi=='k' && b.fi=='j') res = mp('i',1);
    if(a.fi=='1' && b.fi=='k') res = mp('k',0);

    if(a.fi=='j' && b.fi=='1') res = mp('j',0);
    if(a.fi=='k' && b.fi=='i') res = mp('j',0);
    if(a.fi=='1' && b.fi=='j') res = mp('j',0);
    if(a.fi=='i' && b.fi=='k') res = mp('j',1);

    if(a.fi=='k' && b.fi=='1') res = mp('k',0);
    if(a.fi=='1' && b.fi=='i') res = mp('i',0);
    if(a.fi=='i' && b.fi=='j') res = mp('k',0);
    if(a.fi=='j' && b.fi=='k') res = mp('i',0);

    res.se ^= a.se;
    res.se ^= b.se;

    return res;
}

char s [MXN];

string solve(){
    int l,x;
    scanf("%d%d%s", &l, &x, s);
    rep(i,l*x) if(i>=l) s[i] = s[i-l];

    int t = 0;
    pair<char,int> cur = mp('1',0);
    rep(i,l*x){
        cur = mul(cur, mp(s[i],0));
        if(t==0){
            if(cur.fi=='i' && cur.se==0){
                cur = mp('1',0);
                t++;
            }
        }
        else if(t==1){
            if(cur.fi=='j' && cur.se==0){
                cur = mp('1',0);
                t++;
            }
        }
    }
    if(t==2 && cur.fi=='k' && cur.se==0) return string("YES");
    else return string("NO");
}

int main()
{
    freopen("in.txt", "r", stdin);    freopen("out.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    rep(i,t) printf("Case #%d: %s\n", i+1, solve().c_str());

    return 0;
}
