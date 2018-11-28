#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std;

const int MAXN = 3E3;

int n, K;
double a[MAXN];
double f[MAXN][MAXN], ans;

double calc(vector<double> &b){
	f[0][0] = 1.0;
	for (int i = 0; i < K; ++i){
		f[i + 1][i + 1] = 0.0;
		for (int j = i; j >= 0; --j){
			f[i + 1][j] = f[i][j] * (1 - b[i]);
			f[i + 1][j + 1] += f[i][j] * b[i];
		}
	}
	return f[K][K >> 1];
}

int main(){
	int cas;
	scanf("%d", &cas);
	for (int casi = 1; casi <= cas; ++casi){
		printf("Case #%d: ", casi);

		scanf("%d%d", &n, &K);
		for (int i = 0; i < n; ++i)
			scanf("%lf", &a[i]);
		sort(a, a + n);
		vector<double> b;
		double ans = 0.0;
		for (int i = 0; i <= K; ++i){
			b.clear();
			for (int j = 0; j < i; ++j)
				b.push_back(a[j]);
			for (int j = n - (K - i); j < n; ++j)
				b.push_back(a[j]);
			ans = max(ans, calc(b));
		}
		printf("%.10lf\n", ans);
	}
	return 0;
}

