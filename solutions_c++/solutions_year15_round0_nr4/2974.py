#include <map>
#include <climits>
#include <set>
#include <cmath>
#include <ctime>
#include <queue>
#include <stack>
#include <cstdio>
#include <vector>
#include <cstdlib>
#include <cstring>
#include <iomanip>
#include <numeric>
#include <sstream>
#include <utility>
#include <iostream>
#include <algorithm>
#include <functional>

using namespace std;

#define EACH(i,c) for(__typeof((c).begin()) i = (c).begin();i!=(c).end();i++)
#define DBG(e) cout<<(#e)<<" : "<<e<<endl
#define FOR(i,s,e) for(int i=(s);i<(e);i++)
#define CLEAR(v,i) memset(v,i,sizeof v)
#define ALL(x) x.begin(),x.end()
#define pb  push_back
#define pr pair<int,int>
#define SZ(x) int((x).size())


int main() {
    int tests;
    cin>>tests;
    string gab="GABRIEL";
    string rich="RICHARD";
    FOR(tt,1,tests+1) {
        string ret;
        int x,r,c;
        cin>>x>>r>>c;
        if(x==1) ret=gab;
        if(x==2) {
            if(r%2 && c%2) ret=rich;
            else ret=gab;
        }
        if(x==3) {
            if(r==1 || c==1) ret=rich;
            else if(r%2==0 && c%2==0) ret=rich;
            else if(r==3 || c==3) ret=gab;
            else ret=rich;
        }
        if(x==4) {
            if((r==3 && c==4) || (r==4 && c==3) || (r==4 && c==4)) ret=gab;
            else ret=rich;
        }
        cout<<"Case #"<<tt<<": "<<ret<<"\n";
    }
    return 0;
}
