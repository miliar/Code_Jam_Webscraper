
#include<bits/stdc++.h>
#define all(x) x.begin(), x.end()
#define pb(x) push_back(x)
#define MAXN 102
#define EPS 1e-3

using namespace std;

long double acum[MAXN][100002];
long double C[MAXN], F[MAXN], X[MAXN];

int main(){

	int tc = 0;
	scanf("%d", &tc);
	
	for(int i = 0; i < tc; i++)cin>>C[i]>>F[i]>>X[i];
	
	for(int i = 0; i < tc; i++){
		for(int j = 1; j < 100000; j++){
			acum[i][j] = acum[i][j - 1] + 1.0/(2 + (j - 1)*F[i]);
		}
	}
	
	long double val, ans;
	int n;
	
	for(int i = 0; i < tc; i++){
		
		val = (F[i] * X[i] - 2 * C[i] - C[i] * F[i])/(C[i] * F[i]);
		n = int(ceil(val) + EPS);
		
		n = max(0, n);
		ans = acum[i][n] * C[i] + X[i]/(2.0 + n * F[i]);
		printf("Case #%d: %.7lf\n", i + 1, double(ans));
	
		
	}

}

