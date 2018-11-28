#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <string>
#include <cstring>
using namespace std;

#define REP(i,n) for(int i=0;i<(n);++i)
#define FOR(i,a,b) for(int i=(a);i<=(b);++i)
#define RFOR(i,a,b) for(int i=(a);i>=(b);--i)
#define FOREACH(it,c) for(typeof((c).begin())it=(c).begin();it!=(c).end();++it)
#define CLR(x) memset((x),0,sizeof((x)))
#define MP make_pair
#define MPI make_pair<int, int>
#define PB push_back
typedef long long LL;
typedef vector<int> VI;
typedef vector<string> VS;
typedef pair<int, int> PI;

bool isok(vector<int> q, vector<int>& mm) {
    bool up = true;
    int sz = q.size();
    FOR(i,1,sz-1) {
        if (up) {
            if (mm[q[i]] < mm[q[i - 1]]) up = false;
        } else {
            if (mm[q[i]] > mm[q[i - 1]]) return false;
        }
    }

    return true;
}

void run() {
    int N;
    cin >> N;
    vector<int> mm(N);
    vector<int> q;
    REP(i,N) {
        cin >> mm[i];
        q.push_back(i);
    }

    int res = -1;
    
    do {
        if (!isok(q, mm)) continue;
        VI tmp = q;
        VI qq;
        REP(i,N) qq.push_back(i);
        int sum = 0;
        REP(i,N) {
            int now = tmp[0];
            int idx = -1;
            REP(j,qq.size()) {
                if (qq[j] == now) {
                    idx = j;
                    break;
                }
            }
            sum += idx;
            tmp.erase(tmp.begin(), tmp.begin() + 1);
            qq.erase(qq.begin() + idx, qq.begin() + idx + 1);
        }
        
        if (res == -1) res = sum;
        else res = min(res, sum);
    } while (next_permutation(q.begin(), q.end()));

    cout << res << endl;
}

int main() {
    int nk;
    cin >> nk;
    FOR(c,1,nk) {
        cout << "Case #" << c << ": ";
        run();
    }
    return 0;
}
