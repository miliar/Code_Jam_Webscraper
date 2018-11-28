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

int first, second;
int tab[5][5];
int T;
int res;
int cards;
int restab[8];
int main() {
    ios::sync_with_stdio(0);
    cin>>T;
    FOR(IT,1,T) {
        cards = 0;
        res = 0;
        cin>>first;
        FOR(FI,1,4) {
            FOR(FII,1,4) {
                cin>>tab[FI][FII];
            }
        }

        FOR(FI,0,3) {
            restab[FI] = tab[first][FI+1];    
        }
        cin>>second;
        FOR(FI,1,4) {
            FOR(FII,1,4) {
                cin>>tab[FI][FII];
            }
        }
        FOR(FI,0,3) {
            restab[FI+4] = tab[second][FI+1];    
        }
        sort(restab,restab+8);
        FOR(FI,0,6) {
            if(restab[FI] == restab[FI+1]) {
                cards++;
                res = restab[FI];
            }
        } 
        if(cards == 0) {
            cout<<"Case #"<<IT<<": "<<"Volunteer cheated!"<<endl;
        }
        else if(cards ==1) {
            cout<<"Case #"<<IT<<": "<<res<<endl;

        }
        else cout<<"Case #"<<IT<<": "<<"Bad magician!"<<endl;
    }
    return 0;
}


