#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
#include <climits>
#include <cfloat>
#include <ctime>
#include <map>
#include <utility>
#include <set>
#include <memory>
#include <functional>
#include <sstream>
#include <complex>
#include <stack>
#include <queue>

using namespace std;

#define rep(i,b,e) for(int i=b;i<e;++i)
#define mp make_pair
#define pb push_back
#define all(c) (c).begin(),(c).end()

typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> pii;

static const ll Zp = 1000000009;
static const double EPS = 1e-9;

int T;
int X,Y;

struct ST {
    ST(int x_, int y_) : x(x_), y(y_), s(0), move("") {}
    ST(const ST& o) : x(o.x), y(o.y), s(o.s), move(o.move) {}
    int x;
    int y;
    int s;
    string move;
};

string solve(){
    deque<ST> Q;
    set<pair<int,int> > US;
    ST st(0,0);
    Q.pb(st);
    US.insert(mp(0,0));
    while (!Q.empty()) {
        ST p = Q.front(); Q.pop_front();
        if (p.x == X && p.y == Y) return p.move;
        {
            ST np(p);
            ++np.s;
            np.y += np.s; np.move+="N";
            if (US.find(mp(np.x, np.y)) == US.end() )
            Q.push_back(np);
            US.insert(mp(np.x,np.y));
        }
        {
            ST np(p);
            ++np.s;
            np.y -= np.s; np.move+="S";
            if (US.find(mp(np.x, np.y) )== US.end() )
            Q.push_back(np);
            US.insert(mp(np.x,np.y));
        }
        {
            ST np(p);
            ++np.s;
            np.x -= np.s; np.move+="W";
            if (US.find(mp(np.x, np.y)) == US.end() )
            Q.push_back(np);
            US.insert(mp(np.x,np.y));
        }
        {
            ST np(p);
            ++np.s;
            np.x += np.s; np.move+="E";
            if (US.find(mp(np.x, np.y)) == US.end() )
            Q.push_back(np);
            US.insert(mp(np.x,np.y));
        }
    }
    return "";
}

int main(int argc, char *argv[]) {
    cin>>T;
    for(int t=1;t<=T;++t) {
        cin>>X>>Y;
        cout<<"Case #"<<t<<": "<<solve()<<endl;
    }
    return 0;
}
