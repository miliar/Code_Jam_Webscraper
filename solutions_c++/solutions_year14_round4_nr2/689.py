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

int tc, n;
int a[1000];

int fun() {
    int i = 0;
    int j = n-1;
    int res = 0;
    while (i < j) {
        int ps = i;
        for (int k = i+1; k <= j; ++k) if (a[k] < a[ps]) ps = k;
        if (abs(ps-i) < abs(ps-j)) {
            for (int k = ps-1; k >= i; --k) {
                res += 1;
                swap(a[k], a[k+1]);
            }
            i += 1;
        } else {
            for (int k = ps; k < j; ++k) {
                swap(a[k], a[k+1]);
                res += 1;
            }
            j -= 1;
        }
    }
    return res;
}

int main(){
	freopen ("input.txt", "r", stdin);
	freopen ("output.txt", "w", stdout);

    cin >> tc;
    REP(ic,tc) {
        cin >> n;
        REP(i,n) cin >> a[i];
        cout << "Case #" << ic+1 << ": " << fun() << endl;
    }

	return 0;
};