#include <map>
#include <set>
#include <list>
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
    FOR(tt,1,tests+1) {
        int len;
        string c;
        cin>>len>>c;
        int n =c.size();
        int sm=0;
        int ret=0;
        FOR(i,0,n) {
            int val = c[i]-'0';
            if(val!=0) {
            if(sm<i) ret+=i-sm,sm+=i-sm;
            sm+=val;
            }
        }
        cout<<"Case #"<<tt<<": "<<ret<<"\n";
    }
    return 0;
}
