// vudduu - codejam 2016 qualification round
// Problem D
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
typedef long long   LL;

LL K; // initial size
LL C; // C times
LL S; // help

void solve() {
    cin >> K >> C >> S;
    if(S < K) {
        printf("IMPOSSIBLE\n");
        return;
    }
    F(i, S) {
        if(i) printf(" ");
        printf("%d", i+1);
    }
    printf("\n");
}

int main(){
	//freopen("in.txt", "r", stdin);
	freopen("D-small-attempt0.in", "r", stdin);
	//freopen("A-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T;
    scanf("%d", &T);
    for(int cas=1; cas<=T ;cas++) {
        printf("Case #%d: ", cas);
        solve();
    }
}
