#include <cmath>
#include <iostream>
#include <map>
#include <vector>
#include <set>
#include <string>
#include <algorithm>
#include <stack>
#include <queue>
#include <cstring>
#include <cstdio>
#include <string>
#include <functional>

#define all(cont) cont.begin(), cont.end()
#define rall(cont) cont.end(), cont.begin()
#define tr(cont, it) for (typeof(cont.begin()) it = cont.begin() ; it != cont.end() ; it++)
#define FOR(i, j, k, l) for(int i=(j) ; i<(k) ; i+=(l))
#define rep(i, j) FOR(i, 0, j, 1)
#define rrep(i, j) FOR(i, j, -1, -1)

#define INF 1000000000

using namespace std;

typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef vector<vi> vvi;
typedef long long ll;

ll A, B, K;
int T;

int main() {
    scanf("%d", &T);
    for (int t=1 ; t<=T ; t++) {
        scanf("%lld %lld %lld", &A, &B, &K);
        set<pair<int, int> > sol;
        for (int i=0 ; i<A ; i++) {
            for (int j=0 ; j<B ; j++) {
                if ((i&j) < K) {
                    sol.insert(ii(i, j));
                }
            }
        }

        printf("Case #%d: %d\n", t, (int)sol.size());
    }
}