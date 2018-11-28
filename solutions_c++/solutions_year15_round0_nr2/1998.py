// Problem B. Infinite House of Pancakes
// Para mi esposa Susana, en una semana me caso ^_^
#include <iostream>
#include <sstream>
#include <utility>
#include <cstdlib>
#include <cstdio>
#include <cctype>
#include <cmath>
#include <functional>
#include <algorithm>
#include <numeric>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <map>
#include <set>
#include <stdio.h>
#include <string.h>
using namespace std;

#define FOR(i,a,b)  for(int i=(a),_##i=(b);i<_##i;++i)
#define F(i,a)      FOR(i,0,a)
#define ALL(x)      x.begin(),x.end()
#define PB          push_back
#define MP          make_pair
#define S           size()
typedef long long   LL;

int D;
vector<int> P;
int memo1[1000];

int getQuantity(int m) {
    int&res = memo1[m];
    if(res == -1) {
        res = 0;
        for(int i=D-1; i>=0 && P[i] ;i--) {
            if(P[i] > m) {
                int aux = (P[i] / m);
                if(P[i] % m) aux++;
                res += aux-1;
            }
        }
    }
    return res;
}

void solve(int ca) {
    int res;
    memset(memo1, -1, sizeof(memo1));
    cin >> D;
    P.resize(D);
    F(i, D) cin >> P[i];
    sort(ALL(P));
    res = P[D-1];
    FOR(i, 1, P[D-1]) {
        int aux = getQuantity(i);
        res = min(res, aux+i);
    }
    printf("Case #%d: %d\n", ca, res);
}

int main(){
	// freopen("a.in.txt", "r", stdin);
	// freopen("B-small-attempt1.in", "r", stdin);
	freopen("B-large.in", "r", stdin);
	freopen("a.out.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	F(i, T){ solve(i+1); }
}

