#include <cmath>
#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <string>
#include <bitset>
#include <algorithm>
#include <cstring>
using namespace std;

#define rep(i, a, b) for(int i = (a); i < int(b); ++i)
#define trav(it, v) for(typeof((v).begin()) it = (v).begin(); it != (v).end(); ++it)
#define rtrav(it, v) for(typeof((v).rbegin()) it = (v).rbegin(); it != (v).rend(); ++it)

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;

int main(int argc, char const *argv[]) {
	int T;
	double C, F, X;
	scanf("%d", &T);
	rep(t, 0, T) {
		scanf("%lf%lf%lf", &C, &F, &X);
		double rate = 2, tot = 0;
		while (X / rate > X / (rate + F) + C / rate) {
			tot += C / rate;
			rate += F;
		}
		tot += X / rate;
		printf("Case #%d: %.7lf\n", t+1, tot);
	}
	return 0;
}