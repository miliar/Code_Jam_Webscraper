#include <functional>
#include <algorithm>
#include <stdexcept>
#include <iomanip>
#include <cmath>
#include <string>
#include <cstdio>
#include <climits>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <numeric>
#include <iostream>
#include <sstream>
#include <cctype>
#include <ctime>
#include <float.h>
#include <bitset>
#include <set>
#include <utility>
#include <map>
#include <list>
#include <stack>
#include <queue>
#include <vector>

using namespace std;

#define LL long long

#define swap(a,b) {a^=b;b^a=;a^=b;}
#define For(i,a,b) for (int i(a),_b(b); i <= _b ; ++i)
#define Ford(i,a,b) for (int i(a),_b(b); i >= _b ; --i)
#define Rep(i,n) for (int i(0),_n(n); i < _n ; ++i)
#define Repd(i,n) for (int i((n)-1); i>=0 ; --i)
inline int min(int a,int b){return a<b?a:b;}
inline int max(int a,int b){return a>b?a:b;}

int A, N;
LL motes[1000001];

LL predict(LL cur, int i){
	if (i == N) return 0;
	LL ans = 0;
	while (cur <= motes[i]){
		cur += (cur-1);
		ans ++;
	}
	return min(ans + predict(cur+motes[i], i+1), N-i);
}

LL solve(){
	if (A == 1) return N; // delete N motes
	return predict(A,0);
}

int main(){
    freopen("A-large.in","r",stdin);freopen("A-large.out","w",stdout);
    int T;
    cin >> T;
    Rep(i, T){
        printf("Case #%d: ", i+1);
        cin >> A >> N;
        Rep(j, N) cin >> motes[j];
        sort(motes,motes+N);
        cout << solve() << endl;
    }
    return 0;
}