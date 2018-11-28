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

    freopen("B-large.in","r",stdin);
    freopen("cookie.out","w",stdout);

    int ntest;
    cin >> ntest;

    FOR(test,1,ntest){
        double c,f,x;
        cin >> c >> f >> x;
        double t = 0.0;
        double gen = 2.0;
        while(c / gen + x /(gen+f) <x/gen){
        t+= c/gen;
        gen += f;
        //cout << "% "<< gen << endl;
        }
        t+= x/gen;
        printf("Case #%d: %.7lf\n",test,t);
    }


    return 0;
}
