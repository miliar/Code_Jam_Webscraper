#include<algorithm>
#include<cassert>
#include<complex>
#include<map>
#include<iomanip>
#include<sstream>
#include<queue>
#include<set>
#include<string>
#include<cstdio>
#include<vector>
#include<iostream>
#include<cstring>
#define FOR(i, a, b) for(int i =(a); i <=(b); ++i)
#define FORD(i, a, b) for(int i = (a); i >= (b); --i)
#define fup FOR
#define fdo FORD
#define REP(i, n) for(int i = 0;i <(n); ++i)
#define VAR(v, i) __typeof(i) v=(i)
#define FORE(i, c) for(VAR(i, (c).begin()); i != (c).end(); ++i)
#define ALL(x) (x).begin(), (x).end()
#define SZ(x) ((int)(x).size())
#define siz SZ
#define CLR(x) memset((x), 0, sizeof(x))
#define PB push_back
#define MP make_pair
//#define X first
#define Y second 
#define FI X
#define SE Y
#define SQR(a) ((a)*(a))
#define DEBUG 1
#define debug(x) {if (DEBUG)cerr <<#x <<" = " <<x <<endl; }
#define debugv(x) {if (DEBUG) {cerr <<#x <<" = "; FORE(it, (x)) cerr <<*it <<", "; cout <<endl; }}
#define SETALL(x,l,v) for(int i=0;i<l;++i){x[i]=v;}
using namespace std;
typedef long long LL;
typedef long double LD;
typedef pair<int, int>P;
typedef vector<int>VI;
const int INF=1E9+7;

int T;
double C,F,X;
double timeres;
double prod;
double cookies;
int res;
double tillend() {
    return (X-cookies)/prod;
}
void addfarm() {
    if(cookies>=C) {
        cookies-=C;
        prod+=F;
    }
    else {
        timeres = timeres + (C-cookies)/prod;
        cookies=0;
        prod+=F;
    }
}
double onetillend() {
    if(cookies>=C) {
        return (X+C-cookies)/(prod+F);
    }
    else {
        double ww = (C-cookies)/prod;
        return ww + X/(prod+F);
    }
}
void waitTillEnd() {
    timeres += tillend();//difference/prod;
}
double wd,fd;
int main() {
    ios::sync_with_stdio(0);
    cin>>T;
    cout << fixed << setprecision(7);
    FOR(IT,1,T) {
        cin>>C>>F>>X;   
        timeres=0;
        prod=2;

        while(true) {
            wd = tillend();
            fd = onetillend();
            if(wd<fd) {
                waitTillEnd();
                break;
            }
            addfarm();
        }


        cout<<"Case #"<<IT<<": "<<timeres<<endl;
    }
    return 0;
}


