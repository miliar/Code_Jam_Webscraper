#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>


using namespace std;

typedef long long LL;
typedef pair<int, int> PII;

#define lld long long int 
#define EOL '\0'
#define PEL cout<<endl;
#define N 100002
#define rep(n) for(int i =0;(i)<(int)(n);(i)++)
#define repij(n,m) for(int i =0;(i)<(int)(n);(i)++) for(int j =0;(j)<(int)(m);(j)++)

#define SSTR( x ) dynamic_cast< std::ostringstream & >( \
                  std::ostringstream() << std::dec << x ).str()

#define For(iterable) for(__typeof__((iterable).begin()) it = (iterable).begin(); it != (iterable).end(); ++it)

#define PB push_back
#define ST first
#define ND second

int p[1002];
int hold[1002][1002];

void read(int d) { 
    rep(d) cin>>p[i];
    for(int i=0;i<1002;i++) 
        for(int j=0;j<1002;j++)
            hold[i][j]=0;
}

void write(int d) { 
    cout<<d<<endl;
    rep(d) cout<<p[i]<<" "; PEL;
}

int calc(int c,int d) { 
    if(c<=d) return 0;
    if(hold[c][d]) return hold[c][d];
    int curr=99999999;
    for(int i=1;i<=d;i++) {
        curr = min( curr, calc(c-i,d-i));
    }
    for(int i=1;i<=c/2;i++) {
        curr = min( curr, 1+ calc(i,d)+calc(c-i,d));
    }
    hold[c][d]= curr;
    return curr;
}

int solve(int d) { 
    int gm = 10002,lm;
    for(int i=1;i<=1000;i++) {
        lm = i; 
        for(int di=0;di<d;di++) { 
            lm += calc(p[di],i);
        }
        gm = min(gm,lm);
    }
    return gm;
}

int main() 
{
    ios::sync_with_stdio(false);
#ifndef ONLINE_JUDGE
	freopen("test.in", "r",stdin);
	freopen("test.out", "w",stdout);
#endif
    int t,d;cin>>t;
    rep(t) {
        cin>>d;read(d);
        //write(d);
        cout<<"Case #"<<i+1<<": "<<solve(d)<<endl;
    }
    return 0;
}

