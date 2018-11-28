#include<cstdio>
#include<cstring>
#include<vector>
#include<algorithm>
using namespace std;

int T, N, K;
double p[222];

double v[222];
double f[222][222]; // 前n个人，有m个1的概率

double calc() {
	memset(f, 0, sizeof f);
	f[0][0] = 1.;
	for(int i=1;i<=K;i++)
		for(int j=0;j<=i;j++) {
			f[i][j] += f[i-1][j] * (1-v[i]);
			if(j) f[i][j] += f[i-1][j-1] * v[i];
		}
	return f[K][K/2];
}

int main() {
	scanf("%d", &T);
	for(int CASE = 1; CASE <= T; CASE++) {
		scanf("%d%d", &N, &K);
		for(int i=0;i<N;i++) scanf("%lf", &p[i]);
		sort(p,p+N);
		
		double ans = 0;
		for(int i=0;i<=K;i++) {
			int x=0;
			for(int j=0;j<i;j++)
				v[++x] = p[j];
			for(int j=N-1;j>=N-(K-i);j--)
				v[++x] = p[j];
			ans = max(ans, calc());
		}
		
		printf("Case #%d: %.12lf\n", CASE, ans);
	}
	
	return 0;
}