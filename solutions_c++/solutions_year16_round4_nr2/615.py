#include <stdio.h>
#include <string.h>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;

double x[210];
double y[210];
int top, K;
double d[210][210];

double Do(){
	d[1][0] = 1-y[0];
	d[1][1] = y[0];
	for(int i=2;i<=K;i++){
		d[i][0] = (1-y[i-1]) * d[i-1][0];
		for(int j=0;j<=i;j++){
			d[i][j] = (1-y[i-1]) * d[i-1][j] + y[i-1] * d[i-1][j-1];
		}
	}
	
	double save = d[K][K/2];
	memset(d, 0, sizeof d);
	return save;
}

void solve(int tc){
	printf("Case #%d: ", tc);
	int n;
	scanf("%d%d", &n, &K);
	for(int i=0;i<n;i++)scanf("%lf", x+i);
	sort(x, x+n);
	double ans = 0;
	for(int i=0;i<=K;i++){
		top = 0;
		for(int j=0;j<i;j++)y[top++] = x[j];
		for(int j=0;j<K-i;j++)y[top++] = x[n-1-j];
		ans = max(ans, Do());
	}
	printf("%.10f\n", ans);
}

int main() {
	int Tc; scanf("%d", &Tc);
	for(int tc=1;tc<=Tc;tc++){
		solve(tc);
	}
	return 0;
}