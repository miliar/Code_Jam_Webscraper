// vudduu - codejam 2016 qualification round
// Problem A
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

LL INF = 1LL<<55;
bool digs[10];
int totalD;

void markFromNum(LL x) {
    while(x > 0LL) {
        LL y = x % 10LL;
        if(!digs[y]) {
            totalD++;
            digs[y] = 1;
        }
        x /= 10LL;
    }
}

bool isValid() {
    return totalD == 10;
}

void solve() {
    LL SN, N;
    totalD = 0;
    memset(digs, 0, sizeof(digs));
    cin >> N;
    SN = N;
    bool flag = false;
    F(i, 1000000) {
        if(SN > INF) break;
        markFromNum(SN);
        if(isValid()) {
            flag = true;
            cout << SN << endl;
            break;
        }
        SN += N;
    }
    if(!flag) printf("INSOMNIA\n");
}

int main(){
	// freopen("in.txt", "r", stdin);
	// freopen("A-small-attempt1.in", "r", stdin);
	freopen("A-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T;
    scanf("%d", &T);
    for(int cas=1; cas<=T ;cas++) {
        printf("Case #%d: ", cas);
        solve();
    }
}
