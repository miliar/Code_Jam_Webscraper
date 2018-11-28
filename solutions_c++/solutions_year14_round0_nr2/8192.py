#include <cstdio>
#include <cmath>
#include <cstring>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <utility>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <deque>

using namespace std;

typedef long long ll;
typedef vector<int> vecint;
typedef pair<int, int> ppi;
typedef vector< pair<int, int> > vecppi;

#define fill(a,x) memset(a, (x), sizeof(a))
#define tr(container, it) for(typeof(container.begin()) it = container.begin(); it != container.end(); it++)

int read() {   int x;   scanf("%d",&x);   return x;   }
int read(int &x) {  scanf("%d",&x);     return x;   }


const int MAX_N = 100005;
const int oo = int(1e9);

double C, F, X;
double time_limit;



double cal_f(int i, double sum_time) {
	//cout << i << " " << sum_time << "		" << time_limit << endl;
	if (sum_time > X/2 + 100 || i > X+100)
		return oo;
	double g = 2+F*i;
	double t = C/g;
	return min(X/g, t + cal_f(i+1, sum_time+t));
}



int main() {
#ifdef DEBUG
	freopen("B-small-1.in", "r", stdin);
	freopen("B.out", "w", stdout);
#endif
	int nTest = read();
	for (int test_id = 1; test_id <= nTest; ++test_id) {
		scanf("%lf%lf%lf", &C, &F, &X);

		time_limit = X/2;
		double res = cal_f(0, 0);

		printf("Case #%d: %.7lf\n", test_id, res);
	}
	return 0;
}