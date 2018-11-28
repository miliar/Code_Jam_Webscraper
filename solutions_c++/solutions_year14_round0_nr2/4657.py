#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <string>
#include <bitset>

typedef long long LL;
#define pb push_back
#define MPII make_pair<int, int>
#define PII pair<int, int>
#define sz(x) (int)x.size()

using namespace std;

template<class T> T abs(T x){if (x < 0) return -x; else return x;}

const double eps = 1e-7;

int main(){
	freopen("B.in", "r", stdin);
	freopen("B.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int Cases = 1; Cases <= T; ++Cases){
		printf("Case #%d: ", Cases);
		double c, f, x;
		scanf("%lf%lf%lf", &c, &f, &x);
		double now = 0, per = 2;
		for (;;){
			double t1 = x / per;
			double t2 = c / per + x / (per + f);
			if (t2 < t1 - eps){
				now += c / per;	
				per += f;
			} else {
				now += x / per;
				break;
			}
		}
		printf("%.7f\n", now);
	}
	return 0;
}

