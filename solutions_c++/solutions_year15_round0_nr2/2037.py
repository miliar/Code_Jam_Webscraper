#include <algorithm>
#include <assert.h>
#include <climits> 
#include <cmath>
#include <cstdio>
#include <fstream>
#include <iostream>
#include <map>
#include <memory.h>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <vector>
#include <unordered_map>
#include <unordered_set>

using namespace std;

#define pb push_back
#define FOR(i,a,b) for (int _n(b), i(a); i < _n; i++) 
#define REP(i,n) FOR(i,0,n)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define CL(a,v) memset((a),(v),sizeof(a))
#define mp make_pair
#define X first
#define Y second 
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c)) 

typedef long long ll;
typedef pair<int,int> pii;
typedef vector<int> VI;



int main(int argc, char const *argv[]) {

    #ifndef ONLINE_JUDGE
    freopen("input.txt","r", stdin);
    freopen("output_blARGE.txt","w",stdout);
    #endif

    int T; cin>>T;

    REP(t,T) {
        int n; cin>>n;
        std::vector<int> v(n); 
        REP(i,n) cin>>v[i];
        int mm = v[0];
        REP(i,n) {
            mm = max(mm, v[i]);
        }
        int res = mm;
        FOR(i,1,mm+1) {
            int divs = 0;
            REP(j,n) {
                divs += (v[j] + i -1)/i - 1;
            }
            res = min(res, divs + i);
        }
        cout<<"Case #"<<t+1<<": "<<res<<endl;
    }

    return 0;
}