#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <time.h>
#include <cctype>
#include <functional>
#include <deque>
#include <iomanip>
#include <bitset>
#include <assert.h>
#include <numeric>
#include <sstream>
#include <utility>

#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define all(a) (a).begin(),(a).end()
#define FOR(i,a,b) for (int i=(a);i<(b);i++)
#define FORD(i,a,b) for (int i=(a); i>=(b); i--)
#define REP(i,b) FOR(i,0,b)
#define ll long long
#define sf scanf
#define pf printf
using namespace std;
const int maxint = -1u>>1;
const double pi = 3.14159265358979323;
const double eps = 1e-8;
typedef pair<int,int> pii;
typedef vector<int> vi;
typedef vector<int>::iterator vit;

double c, f, x;
int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int T, ca = 0;
    cin >>T;
    while (T--) {
        cin >>c >>f >>x;
        double ans = x / 2.0;
        double sum = 0, speed = 2.0;
        
        for (int i = 1; i <= ((int)(x+5)); i++) {
            sum += c / speed;
            speed += f;
            if (sum + x / speed > ans) break;
            ans = min(ans, sum + x / speed);
        }
        printf("Case #%d: %.7f\n", ++ca, ans);
    }
    return 0;
}

