// Problem A. Standing Ovation
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

int Smax;
string s;

int solve() {
    int total = s[0]-'0';
    int res = 0;
    for(int i=1; i<=Smax ;i++) {
        int aux = s[i]-'0';
        if(total < i) {
            res += (i-total);
            total = i;
        }
        total += aux;
    }
    return res;
}

int main(){
	//freopen("a.in.txt", "r", stdin);
	//freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-large.in", "r", stdin);
	freopen("a.out.txt", "w", stdout);
	int T;
    scanf("%d", &T);
    F(cas, T) {
        cin >> Smax >> s;
        printf("Case #%d: %d\n", cas+1, solve());
    }
}
