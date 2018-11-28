#include <assert.h>
#include <algorithm>
#include <bitset>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <ctime>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <utility>
#include <vector>

using namespace std;

typedef unsigned int UINT;
typedef long long unsigned int ULL;
typedef long long int LL;

const int MAXN = 10;
const int MOD = 1000000007;

vector<map<int,int> > pos(MAXN);

map<int,int> Merge(map<int,int> a, map<int,int> b)
{
    map<int,int> res;
    for (map<int,int>::iterator it = a.begin(); it != a.end(); it++) {
        for (map<int,int>::iterator jt = b.begin(); jt != b.end(); jt++) {
            int teat = max(it->second, jt->second);
            int tsp = it->first + jt->first;
            if (teat + tsp >= MAXN) continue;
            if (res.find(tsp) == res.end()) {
                res[tsp] = teat;
            } else {
                res[tsp] = min(res[tsp], teat);
            }
        }
    }
    return res;
}

map<int,int> DivideMerge(const vector<int>& plate, int N, int begin, int end)
{
    if (begin == end) {
        return pos[plate[begin]];
    }

    int mid = begin + (end - begin)/2;
    map<int,int> a = DivideMerge(plate, N, begin, mid);
    map<int,int> b = DivideMerge(plate, N, mid+1, end);
    map<int,int> res = Merge(a, b);
    return res;
}

int solve(const vector<int> &plate, int N)
{
    map<int,int> m = DivideMerge(plate, N, 0, N-1);
    int best = MAXN;
    for (map<int,int>::iterator it = m.begin(); it != m.end(); it++) {
        best = min(best, it->first + it->second);
    }
    return best;
}

int main ()
{
    int TT;
    scanf("%d", &TT);
    for (int i = 1; i < MAXN; i++) {
        for (int j = 2, k = i - j; j <= k; j++, k--) {
            map<int,int> res = Merge(pos[j], pos[k]);
            for (map<int,int>::iterator it = res.begin(); it != res.end(); it++) {
                if (pos[i].find(it->first + 1) == pos[i].end()) {
                    pos[i][it->first + 1] = it->second;
                } else {
                    pos[i][it->first + 1] = min(pos[i][it->first + 1], it->second);
                }
            }
        }
        pos[i][0] = i;
        //for (map<int,int>::iterator it = pos[i].begin(); it != pos[i].end(); it++) {
            //printf("%d: %d,%d\n", i, it->first, it->second);
        //}
    }

    for (int tt = 1; tt <= TT; tt++) {
        int N;
        scanf("%d", &N);
        vector<int> plate;
        for (int i = 0; i < N; i++) {
            int a;
            scanf("%d", &a);
            plate.push_back(a);
        }
        int best = solve(plate, N);
        printf("Case #%d: %d\n", tt, best);
    }
    return 0;
}
