// vudduu - codejam 2016 Round 1A
// Problem C
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

int N;
vector<pair<int,int> > v;
bool allGood;

void solve() {
    cin >> N;
    v.resize(N);
    int x;
    F(i, N) {
        cin >> x;
        v[i] = MP(i+1, x);
    }
    sort(ALL(v));
    int maxi = 0;
    do {
        vector<pair<int, int> > aux = v;
        int b = 0;
        while(b != aux.S) {
            b = aux.S;
            F(i, aux.S) {
                int j0 = (i+1 >= aux.S)? 0 : i+1;
                int j1 = (i-1 < 0)? aux.S-1 : i-1;
                bool t = false;
                if(aux[i].second == aux[j0].first)
                    t = true;
                if(aux[i].second == aux[j1].first)
                    t = true;
                if(!t) {
                    aux.erase(aux.begin()+i);
                    break;
                }
            }
        }
        maxi = max(maxi, int(aux.S));
    } while(next_permutation(ALL(v)));
    cout << maxi << endl;
}

int main() {
	//freopen("in.txt", "r", stdin);
	freopen("C-small-attempt0.in", "r", stdin);
	// freopen("C-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T;
    scanf("%d", &T);
    for(int cas=1; cas<=T ;cas++) {
        printf("Case #%d: ", cas);
        solve();
    }
}
