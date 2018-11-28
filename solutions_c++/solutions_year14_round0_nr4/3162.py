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

int T,N;
double balls[2][1000];
double memin;
int howmany;
int cheatres, res;
int main() {
    ios::sync_with_stdio(0);
    cin>>T;
    cout << fixed << setprecision(7);
    FOR(IT,1,T) {
        cin>>N;   
        cheatres=0;
        res=0;
        FOR(IN,0,N-1) {
            cin>>balls[0][IN];
        }
        FOR(IN,0,N-1) {
            cin>>balls[1][IN];
        }
        sort(balls[0], balls[0] + N);
        sort(balls[1], balls[1] + N);

        //memin = balls[1][0];
        int ii = 0;
        int opp = 0;
        while(ii<N) {
            if(balls[1][opp] < balls[0][ii]) {
            cheatres++;
            ++opp;
            }
            ++ii;
        }
        ii = 0;
        opp = 0;
        while(ii<N) {
            if(balls[0][opp] < balls[1][ii]) {
            res++;
            ++opp;
            }
            ++ii;
        }
                cout<<"Case #"<<IT<<": "<<cheatres<<" "<<N-res<<endl;
    }
    return 0;
}


