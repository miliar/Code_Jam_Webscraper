// tested by Hightail: https://github.com/dj3500/hightail
#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <cmath>
#include <algorithm>
#include <sstream>
#include <stack>
#include <cstring>
#include <iomanip>
#include <ctime>
#include <cassert>
using namespace std;
#define pb push_back
#define INF 1001001001
#define FOR(i,n) for(int (i)=0;(i)<(n);++(i))
#define FORI(i,n) for(int (i)=1;(i)<=(n);++(i))
#define mp make_pair
#define pii pair<int,int>
#define ll long long
#define vi vector<int>
#define SZ(x) ((int)((x).size()))
#define fi first
#define se second
#define wez(n) int (n); scanf("%d",&(n));
#define wez2(n,m) int (n),(m); scanf("%d %d",&(n),&(m));
#define wez3(n,m,k) int (n),(m),(k); scanf("%d %d %d",&(n),&(m),&(k));
inline void pisz(int n) { printf("%d\n",n); }
template<typename T,typename TT> ostream& operator<<(ostream &s,pair<T,TT> t) {return s<<"("<<t.first<<","<<t.second<<")";}
template<typename T> ostream& operator<<(ostream &s,vector<T> t){FOR(i,SZ(t))s<<t[i]<<" ";return s; }
#define DBG(vari) cout<<"["<<__LINE__<<"] "<<#vari<<" = "<<(vari)<<endl;
#define ALL(t) t.begin(),t.end()
#define FOREACH(i,t) for (__typeof(t.begin()) i=t.begin(); i!=t.end(); i++)
#define TESTS wez(testow)while(testow--)
#define REP(i,a,b) for(int (i)=(a);(i)<=(b);++i)
#define REPD(i,a,b) for(int (i)=(a); (i)>=(b);--i)
#define REMAX(a,b) (a)=max((a),(b));
#define REMIN(a,b) (a)=min((a),(b));
#define IOS ios_base::sync_with_stdio(0);

const int N = 111;
char s[N][N];

int main () {
    wez(te)
    FORI(testno,te) {
        printf("Case #%d: ", testno);
        wez2(n,m)
        FOR(i,n) scanf("%s", s[i]);
        int res = 0;
        bool fail = 0;

        FOR(i,n) FOR(j,m) {
            if (s[i][j] != '.') {
                bool someone = 0;
                FOR(i1,i) if (s[i1][j] != '.') someone = 1;
                FOR(j1,j) if (s[i][j1] != '.') someone = 1;
                REP(i1,i+1,n-1) if (s[i1][j] != '.') someone = 1;
                REP(j1,j+1,m-1) if (s[i][j1] != '.') someone = 1;
                if (!someone) fail = 1;
            }
            if (s[i][j] == '^') {
                bool someone = 0;
                FOR(i1,i) if (s[i1][j] != '.') someone = 1;
                if (!someone) ++res;
            }
            if (s[i][j] == 'v') {
                bool someone = 0;
                REP(i1,i+1,n-1) if (s[i1][j] != '.') someone = 1;
                if (!someone) ++res;
            }
            if (s[i][j] == '<') {
                bool someone = 0;
                FOR(j1,j) if (s[i][j1] != '.') someone = 1;
                if (!someone) ++res;
            }
            if (s[i][j] == '>') {
                bool someone = 0;
                REP(j1,j+1,m-1) if (s[i][j1] != '.') someone = 1;
                if (!someone) ++res;
            }
        }
        if (fail) printf("IMPOSSIBLE\n");
        else pisz(res);
    }
}
