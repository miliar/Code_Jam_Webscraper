// Author: Swarnaprakash
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <queue>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cctype>
#include <cassert>

using namespace std;

const int M = 105;
const int INF = 0x3f3f3f3f;
const bool debug=true;

#define SET(x,v)	memset(x,v,sizeof(x))
#define ALL(x) 		(x).begin() , (x).end()
#define SZ(x)		((int)((x).size()))
#define DB(x) 		if(debug) cout << #x << " : " << x <<endl;

typedef long long LL;
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<VI> VVI;
typedef pair<int,int> PII;
typedef pair<int,PII> PIII;

bool is_updown(vector<int> &v) {
    for(int ind = 0;ind < SZ(v); ++ind) {
        bool is_updown = true;
        for(int i=0;i<ind && i < (SZ(v) -1) && is_updown;++i) if(v[i] > v[i+1]) is_updown = false;
        for(int i=ind;i < (SZ(v) -1) && is_updown;++i) if(v[i] < v[i+1]) is_updown = false;

        if(is_updown) return true;
    }
    return false;
}

int moves(vector<int> &source, vector<int> &dest) {
    map<int,int> real_index;
    for(int i=0;i<SZ(dest);++i) real_index[dest[i]] = i;

    int inversions = 0;
    for(int i=0;i<SZ(source);++i) {
        for(int j=i+1;j<SZ(source);++j) {
            if(real_index[source[i]] > real_index[source[j]]) ++inversions;
        }
    }
    return inversions;
}

void print(vector<int> &v) {
    for(int i=0;i<SZ(v);++i) printf("%d ", v[i]);
    puts("");
}

int main() {
    int tc;
    scanf("%d",&tc);
    for(int t=1;t<=tc;++t) {
        int n;
        scanf("%d",&n);
        vector<int> v(n);
        for(int i=0;i<n;++i) scanf("%d", &v[i]);
        vector<int> v_copy = v;
        int ans = INF;
        sort(ALL(v));
        do {
            if(is_updown(v)) {
                int m = moves(v_copy, v);
                ans = min(ans, moves(v_copy, v));
//                printf("%d - ",m);
//              print(v);
            }
        } while(next_permutation(ALL(v)));

        printf("Case #%d: %d\n",t,ans);
    }
    return 0;
}

