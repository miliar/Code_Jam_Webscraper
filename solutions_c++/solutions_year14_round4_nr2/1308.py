#include <algorithm>
#include <cassert>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <cstring>
#include <iostream>
#include <sstream>
#include <string>
#include <utility>
#include <vector>
#include <cassert>
#include <ctime>
#include <queue>
#include <map>
#include <set>
#include <climits>
using namespace std;

typedef vector<int> VI;
typedef vector<string> VS;
typedef long long LL;
typedef pair<int, int> PII;

#define REP(i,n) for(int _n=n, i=0;i<_n;++i)
#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;++i)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define FOREACH(it,c) for(auto it=(c).begin();it!=(c).end();++it)
#define FILLCHAR(a, x) memset(a, x, sizeof(a))
#define SZ(x) ((int) (x).size())
#define ALL(x) (x).begin(), (x).end()

int T;
int N;
const int MAXN = 1024;
int A[MAXN];
int org[MAXN];
int oorg[MAXN];

bool isValid() {
    bool first = true;

    for (int i = 1; i < N; i++) {
        if (first) {
            if (A[i] < A[i - 1]) {
                first = false;
            }
        } else {
            if (A[i] > A[i - 1]) return false;
        }
    }

    return true;
}

int run() {
    scanf("%d", &N);
    REP(i,N) scanf("%d", &A[i]);
    REP(i,N) org[i] = A[i];
    map<int, int> v2i;
    sort(A, A + N);

    int ret = INT_MAX;
    do {
        if (!isValid()) continue;
        REP(i,N) {
            oorg[i] = org[i];
        }
        int cnt = 0;
        REP(i,N) {
            if (A[i] != oorg[i]) {
                int j;
                for (j = i + 1; j < N; j++) {
                    if (oorg[j] == A[i]) break;
                }

                while (j != i) {
                    swap(oorg[j], oorg[j - 1]);
                    cnt++;
                    j--;
                 }
            }
        }

        ret = min(ret, cnt);
    } while (next_permutation(A, A + N));

    return ret;
}
int main() {
    int T;
    scanf("%d", &T);

    REP(t,T) {
        printf("Case #%d: %d\n", t + 1, run());
    }
}



