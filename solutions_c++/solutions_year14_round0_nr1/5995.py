    using namespace std;
#include <cmath>
#include <cstdio>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <string>
#include <cstring>
#include <vector>
#include <iostream>
#include <sstream>
#include <algorithm>

#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;i++)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;i--)

#define SET(a,x) memset((a),(x),sizeof(a))
#define COPY(a,b) memcpy((a),(b),sizeof(a))
// set = 0
#define PB push_back
#define TR(c,it) for(typeof(c.begin()) it=c.begin();it!=c.end();it++)

#define EXIST(c,x) (c.find(x)!=c.end())

typedef long long LL;
typedef pair<int,int>II;
typedef pair<int,II>III;

#define ST first
#define ND second

typedef vector<int>VI;
typedef vector<VI>VVI;
typedef vector<II>VII;
typedef vector<VII>VVII;

int main(){

    freopen("A-small-attempt0.in","r",stdin);
    freopen("magician.out","w",stdout);

    int ntest;
    cin >> ntest;
    FOR(test,1,ntest){
        int ans1,ans2;
        int f1[4][4],f2[4][4];

        cin >> ans1; FOR(i,0,3) FOR(j,0,3) cin >> f1[i][j];
        cin >> ans2; FOR(i,0,3) FOR(j,0,3) cin >> f2[i][j];
        int res = 0,t;
        FOR(i,0,3) FOR(j,0,3) if(f1[ans1-1][i] == f2[ans2-1][j]) {res++; t= f1[ans1-1][i];}
        cout <<"Case #"<<test<<": ";
        if(res > 1) cout << "Bad magician!\n"; else {
            if(res == 1) cout << t << endl; else cout << "Volunteer cheated!\n";
        }
    }

    return 0;
}
