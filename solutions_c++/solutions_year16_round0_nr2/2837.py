// vudduu - codejam 2016 qualification round
// Problem B
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

string A;

int getFirstDiff() {
    char first = A[0];
    FOR(i, 1, A.S) {
        if(A[i] != first)
            return i;
    }
    return -1;
}

void solve() {
    cin >> A;
    int total = 0;
    int it = getFirstDiff();
    while(it != -1) {
        F(i, it) A[i] = A[it];
        total++;
        it = getFirstDiff();
    }
    if(A[0] == '-') total++;
    printf("%d\n", total);
}

int main(){
	//freopen("in.txt", "r", stdin);
	// freopen("B-small-attempt0.in", "r", stdin);
	freopen("B-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T;
    scanf("%d", &T);
    for(int cas=1; cas<=T ;cas++) {
        printf("Case #%d: ", cas);
        solve();
    }
}
