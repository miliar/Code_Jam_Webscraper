#pragma comment(linker, "/STACK:33554432")

#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <iostream>
#include <cmath>
#include <string>
#include <sstream>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <ctime>
#include <memory.h>

using namespace std;

#define REP(i,n) for(int i=0;i<n;++i)
#define ABS(n) ((n)<0 ? -(n) : (n))
#define SQR(a) (a)*(a)
#define MIN(a,b) (a<b?a:b)
#define MAX(a,b) (a>b?a:b)
#define MP make_pair
#define PB push_back
#define FILL(a) memset(a,0,sizeof(a));
#define COPY(a,b) memcpy(a,b,sizeof (b));
#define SI(a) (int)((a).size())
#define ALL(a) (a).begin(),(a).end()
#define y1 yyyyy1
#define prev prevvvvv
#define LL long long
const double PI = 2*acos(0.0);
const double EPS = 1e-8;
const int INF = (1<<30)-1;
const int P = 1000000007;

int m, n, tc;
int a[10000];
bool used[10000];

int fun() {
    int res = 0;
    memset (used, false, sizeof(bool)*n);
    for (int i = n-1; i >= 0; --i) if (!used[i]) {
        used[i] = true;
        int j = upper_bound(a, a+n, m-a[i]) - a;
        if (j > i) j = i-1;
        while (j >= 0 && (used[j] || a[i]+a[j] > m)) --j;
        if (j >= 0) used[j] = true;
        res += 1;
    }
    return res;
}

int main(){
	freopen ("input.txt", "r", stdin);
	freopen ("output.txt", "w", stdout);
    cin >> tc;
    REP(ic,tc) {
        cin >> n >> m;
        REP(i,n) cin >> a[i];
        sort(a, a+n);
        cout << "Case #" << ic+1 << ": " << fun() << endl;
    }



	return 0;
};