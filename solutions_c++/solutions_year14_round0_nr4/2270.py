#include <cstring>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cassert>

using namespace std;
typedef long long int64;
typedef pair<int, int> PII;
const int MOD = 1000000007;
const double EPSILON = 1e-10;

#define FORU(i, a, b) for (int i = (a); i <= (b); ++i)
#define FORD(i, a, b) for (int i = (a); i >= (b); --i)
#define REPU(i, a, b) for (int i = (a); i < (b); ++i)
#define REPD(i, a, b) for (int i = (a); i > (b); --i)
#define SIZE(A) ((int) A.size())
#define PB(X) push_back(X)
#define MP(A, B) make_pair(A, B)

template<class T> inline T tmin(T a, T b) {return (a < b) ? a : b;}
template<class T> inline T tmax(T a, T b) {return (a > b) ? a : b;}
template<class T> inline T tabs(T a) {return (a > 0) ? a : -a;}
template<class T> T gcd(T a, T b) {if (b == 0) return a; return gcd(b, a % b);}

int n;
double a[1001], b[1001];

int cal_war()
{
	int ans = 0;
	int l = 0, h = n - 1;
	FORD(i, n-1, 0) {
		if (a[i] > b[h]) {
			ans++; l++;
		}
		else h--;
	}
	return ans;
}

int cal_dwar()
{
	int ans = 0;
	int l = 0, h = n - 1;
	FORU(i, 0, n-1) {
		if (a[i] > b[l]) {
			ans++; l++;
		}
		else h--;
	}
	return ans;
}

int main(int argc, char const *argv[])
{
	int ntest;
	scanf("%d", &ntest);
	FORU(t, 1, ntest) {
		scanf("%d", &n);
		REPU(i, 0, n) scanf("%lf", &a[i]);
		REPU(i, 0, n) scanf("%lf", &b[i]);
		sort(a, a + n);
		sort(b, b + n);
		printf("Case #%d: %d %d\n", t, cal_dwar(), cal_war());
	}
	return 0;
}