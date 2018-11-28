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

void add (const vector<int> &v, vector<bool> &s) {
    FOREACH(it,v) s[*it] = 1;
}

int main () {
    wez(te)
    FORI(testno,te) {
        printf("Case #%d: ", testno);
        wez(n)
        string s[20];
        getline(cin, s[0]);
        FOR(i,n) getline(cin, s[i]);
        vector<string> v[20];
        map<string,int> id;
        int q = 1;
        FOR(i,n) {
            stringstream ss(s[i]);
            string t;
            while (ss >> t) {
                v[i].pb(t);
                id[t] = q++;
            }
        }
        vi vv[20];
        FOR(i,n) {
            FOREACH(it,v[i]) {
                vv[i].pb(id[*it]);
            }
        }
        int best = 1111;
        FOR(mask,1<<(n-2)) {
            vector<bool> eng(q,0), fra(q,0);
            add(vv[0], eng);
            add(vv[1], fra);
            FOR(i,n-2) add(vv[i+2], (!!((1<<i) & mask)) ? eng : fra);
            int res = 0;
            FOR(a,q) if (eng[a] && fra[a]) ++res;
            REMIN(best, res);
        }
        pisz(best);
    }
}
