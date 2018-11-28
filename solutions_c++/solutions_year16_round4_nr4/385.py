#include <iostream>
#include <vector>
#include <cstring>
#include <cstdio>
#include <map>
#include <deque>
#include <set>
#include <algorithm>
#include <numeric>
#include <functional>
#include <unordered_map>
#include <thread>

using namespace std;

#define ll long long


int N;
string U[25];

bool good(const vector<int>& o, int p = 0, int used = 0) {
    if (p == N) return true;
    int id = o[p];
    bool any = false;
    for (int i=0;i<N;++i) {
        if (used & (1<<i)) continue;
        if (U[id][i] != '1') continue;
        
        any = true;
        if (!good(o, p+1, used | (1<<i))) {
            return false;
        }

    }
    return any;
}

bool good() {
    vector<int> o;
    for (int i=0;i<N;++i) {
        o.push_back(i);
    }
    do {
        if (!good(o)) {
            return false;
        }
    } while (next_permutation(o.begin(), o.end()));
    return true;
}

int teach(int p) {
    if (p == N) {
        if (good()) {
            return 0;
        } else {
            return 1<<30;
        }
    }
    int ans = 1<<30;
    
    for (int i=0;i<(1<<N);++i) {
        int cur = 0;
        string pu = U[p];
        for (int j=0;j<N;++j) {
            if ((i & (1<<j))) {
                cur++;
                U[p][j] = '1';
            }
        }
        ans = min(ans, teach(p+1) + cur);
        U[p] = pu;
    }

    return ans;
}

int main() {
    int T;
    cin>>T;
    for (int t=1;t<=T;++t) {

        cin>>N;

        for (int i=0;i<N;++i) {
            cin>>U[i];
        }


        int ans = teach(0);

        printf("Case #%d: %d\n", t, ans);
    }
}
