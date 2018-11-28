#include <iostream>
#include <vector>
#include <list>
#include <stack>
#include <queue>
#include <deque>
#include <map>
#include <set>
#include <algorithm>
#include <functional>
#include <complex>

#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <climits>
#include <cfloat>
#include <ctime>
#include <iomanip>

using namespace std;

#define DBG(fmt, ...) fprintf(stderr, fmt, __VA_ARGS__);
#define DUMP(val) cerr << #val << " : " << (val) << endl

#define REP(a,b) for(a = 0; a < b; a++)
#define FOR(a,b,c) for(a = b; a < c; a++)
#define FOREACH(it, c) for (__typeof__((c).begin()) it=(c).begin(); it != (c).end(); ++it)

#define PUSH(e) push_back(e)
#define POP(e) pop_back(e)
#define MP(a,b) make_pair(a,b)
#define ALL(a) (a).begin(),(a).end()
#define RALL(a) (a).rbegin(),(a).rend()
#define SORT(a) sort((a).begin(),(b).end())
#define FILL(a,b) fill((a).begin(),(a).end(),b)

typedef pair<int,int> point;
#define F first
#define S second

typedef signed char int8_t;
typedef unsigned char uint8_t;
typedef signed short int16_t;
typedef unsigned short uint16_t;
typedef signed int int32_t;
typedef unsigned int uint32_t;

double solve(double c, double f, double x) {
    double cps = 2;
    double time = 0.0;
    double rem_time = x / cps;
    double upgrade_time = c/cps;
    double next_rem = upgrade_time + (x / (cps+f));
    
    while(rem_time > next_rem) {
        
        time += upgrade_time;
        cps += f;
        rem_time = x / cps;
        upgrade_time = c/cps;
        next_rem = upgrade_time + (x / (cps+f));
    }
    time += rem_time;
    
    return time;
}


int main()
{
    int T;
    double c,f,x;
    cin >> T;
    for(int t = 0; t < T; t++) {
        cin >> c >> f >> x;
        cout << "Case #" << (t+1) << ": " << fixed << setprecision(7) << solve(c, f, x) << endl;
    }
    
    return 0;
}

