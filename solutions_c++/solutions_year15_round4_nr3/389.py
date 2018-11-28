#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <queue>
#include <deque>
#include <set>
#include <map>
#include <stack>
#include <utility>
#include <fstream>
#include <functional>
#include <ctime>
#include <cstdlib>
#include <string>
#include <cstring>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;

#define mp make_pair
#define pb push_back
#define fi first
#define se second
#define pii pair<int,int>
#define pdd pair<double,double>
#define pll pair<ll,ll>
#define forn(i,a,b) for( int i = (a); i < (b); i++ )
#define rep(i,n) forn(i,0,n)
#define repe(i,n) for( i = 0; i < (n); i++ )

const int MXN = 25;
const int MXS = 20*10;
const int inf = 2e9;
const int mod = 1000000007;
const int MXW = 3000;
const double eps = 1e-9;


string sent [MXN];

int eng [MXW];
int frn [MXW];

void setv( int *a, int val, vector<int> &snt){
    int sz = snt.size();
    rep(i,sz){
        a[snt[i]]+=val;
    }
}

char tmp [100100];

bool isset( int msk, int i ){
    return msk & (1<<i);
}


map<string, int> nn;

vector<int> snt [MXN];

int WORD;

void transfor( char *tmp, vector<int>& a ){
    a.clear();
    int sz = strlen(tmp);
    string cur = "";
    rep(i,sz){
        if(tmp[i]==' '){
            if(nn[cur]==0){
                nn[cur] = WORD++;
            }
            a.pb(nn[cur]);
            cur = "";
        }
        else cur+=tmp[i];
    }
    if(!cur.empty()){
        if(nn[cur]==0){
            nn[cur] = WORD++;
        }
        a.pb(nn[cur]);
    }
}

int solve(){
    rep(i,MXW) eng[i] = frn[i] = 0;
    nn.clear();
    WORD = 1;
    int n;
    scanf("%d", &n);
    gets(tmp);
    gets(tmp);
    transfor(tmp,snt[0]);
    setv(eng,1,snt[0]);

    gets(tmp);
    transfor(tmp,snt[0]);
    setv(frn,1,snt[0]);
    n-=2;
    rep(i,n){
        gets(tmp);
        transfor(tmp,snt[i]);
    }
    int res = 1e9;
    rep(i, (1<<n)){
        rep(j,n){
            if( isset(i,j) )
                setv(eng,1,snt[j]);
            else setv(frn,1,snt[j]);
        }
        int cur = 0;
        rep(j,WORD){
            if(frn[j] && eng[j]) cur++;
        }
        res = min(res,cur);
        rep(j,n){
            if( isset(i,j) )
                setv(eng,-1,snt[j]);
            else setv(frn,-1,snt[j]);
        }
    }
    return res;
}

int main()
{
    freopen("input.txt", "r", stdin);
    ofstream out;
    out.open("output.txt");
    int t;
    scanf("%d", &t);
    rep(i,t){
        cout<<i<<endl;
        out<<"Case #"<<i+1<<": "<<solve()<<endl;
    }
    out.close();
    return 0;
}
