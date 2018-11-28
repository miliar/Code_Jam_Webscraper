#include<algorithm>
#include<cassert>
#include<complex>
#include<map>
#include<iomanip>
#include<sstream>
#include<queue>
#include<set>
#include<string>
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
#define X first
#define Y second 
#define FI X
#define SE Y
#define SQR(a) ((a)*(a))
#define DEBUG 1
#define debug(x) {if (DEBUG)cerr <<#x <<" = " <<x <<endl; }
#define debugv(x) {if (DEBUG) {cerr <<#x <<" = "; FORE(it, (x)) cerr <<*it <<", "; cout <<endl; }}
using namespace std;
typedef long long LL;
typedef long double LD;
typedef pair<int, int>P;
typedef vector<int>VI;
const int INF=1E9+7;
template<class C> void mini(C&a4, C b4){a4=min(a4, b4); }
template<class C> void maxi(C&a4, C b4){a4=max(a4, b4); }
#define MAXN 2007

int n,A[MAXN],B[MAXN],last[MAXN],deg[MAXN],ans[MAXN];
VI G[MAXN];

int main(){
	ios_base::sync_with_stdio(false);
    cout << setprecision(15) << fixed;
    int T;
    cin >> T;
    FOR(t,1,T) {
	    //in
        cin >> n;
        FOR(i,1,n) cin >> A[i];
        FOR(i,1,n) cin >> B[i];
        FOR(i,0,n) G[i].clear();
	    //sol
        FOR(i,1,n) FOR(j,i+1,n) {
            if(A[j] <= A[i]) G[j].PB(i);
            if(B[i] <= B[j]) G[i].PB(j);
        }
        CLR(last);
        FOR(i,1,n) {
            G[last[A[i]-1]].PB(i);
            last[A[i]] = i;
        }
        CLR(last);
        FORD(i,n,1) {
            G[last[B[i]-1]].PB(i);
            last[B[i]] = i;
        }
        CLR(deg); CLR(ans);
        FOR(i,1,n) FORE(j,G[i]) deg[*j]++;
        priority_queue<int> Q;
        FOR(i,1,n) if(!deg[i]) Q.push(-i);
        int val = 1;
        while(!Q.empty()) {
            int x = -Q.top(); Q.pop();
            ans[x] = val++;
            FORE(i,G[x]) if(--deg[*i] == 0) Q.push(-*i);
        }
	    //out
        cout << "Case #" << t << ": ";
        FOR(i,1,n) cout << ans[i] << " "; cout << endl;
    }
	return 0;
}

