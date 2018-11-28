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

int count_dw(const vector<double> &naomi,
             const vector<double> &ken)
{
    int score = 0;
    int diceit = 0;
    for(int i = 0; i < naomi.size(); i++) {
        if(naomi[i] > ken[i-diceit]) {
            score++;
        } else {
            diceit++;
        }
    }
    
    return score;
}

int count_w(const vector<double> &naomi,
          const vector<double> &ken)
{
    vector<bool> kflags(ken.size(), true);
    
    for(int i = 0; i < naomi.size(); ++i) {
        vector<double>::const_iterator it = lower_bound(ken.begin(), ken.end(), naomi[i]);
        size_t j = distance(ken.begin(), it);
        while(it != ken.end()) {
            if(kflags[j]) {
                kflags[j] = false;
                break;
            }
            j++;
            it++;
        }
    }
    
    return count(kflags.begin(), kflags.end(), true);
}



pair<int, int> solve(vector<double> &naomi,
                     vector<double> &ken)
{
    pair<int, int> points;
    
    sort(naomi.begin(), naomi.end());
    sort(ken.begin(), ken.end());
    
    points.first = count_dw(naomi, ken);
    points.second = count_w(naomi, ken);
    
    return points;
}


int main()
{
    int T;
    cin >> T;
    for(int t = 0; t < T; ++t) {
        int n;
        cin >> n;
        vector<double> naomi, ken;
        for(int i = 0; i < n; ++i) {
            double tmp;
            cin >> tmp;
            naomi.push_back(tmp);
        }
        for(int i = 0; i < n; ++i) {
            double tmp;
            cin >> tmp;
            ken.push_back(tmp);
        }
        pair<int, int> ret = solve(naomi, ken);
        cout << "Case #" << (t+1) << ": " << ret.first << " " << ret.second << endl;
    }
    
    return 0;
}

